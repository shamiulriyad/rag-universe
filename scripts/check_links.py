#!/usr/bin/env python3
"""Check Markdown links in the RAG-Universe repository.

By default, verifies every *internal* link in every Markdown file:
  - relative file and folder links point to something that exists;
  - #anchors point to a real heading (GitHub-style slugs), in the same
    file or in the linked Markdown file.

With --external, also requests every http(s) URL and reports failures.

Usage:
    python scripts/check_links.py              # internal links only
    python scripts/check_links.py --external   # internal + external links

Exit code is 1 if any problem is found, 0 otherwise.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# [text](target "optional title") and ![alt](target)
INLINE_LINK_RE = re.compile(r"!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
# [label]: target
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s+.*)?$")


def iter_markdown_files() -> list[Path]:
    files = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def strip_code(text: str) -> list[tuple[int, str]]:
    """Return (line_number, line) pairs with fenced code blocks, HTML comments
    and inline code removed."""
    text = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    result = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        result.append((number, INLINE_CODE_RE.sub("", line)))
    return result


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading-anchor algorithm."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links -> text
    text = re.sub(r"<[^>]+>", "", text)  # HTML tags
    text = text.replace("`", "")
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)  # drop punctuation (keeps unicode letters)
    return text.replace(" ", "-")


@lru_cache(maxsize=None)
def anchors_for(path: Path) -> frozenset[str]:
    text = path.read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    anchors = set()
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = github_slug(match.group(2))
        n = counts.get(slug, 0)
        anchors.add(slug if n == 0 else f"{slug}-{n}")
        counts[slug] = n + 1
    return frozenset(anchors)


def extract_links(path: Path) -> list[tuple[int, str]]:
    links = []
    for number, line in strip_code(path.read_text(encoding="utf-8")):
        for match in INLINE_LINK_RE.finditer(line):
            links.append((number, match.group(1)))
        ref = REF_DEF_RE.match(line)
        if ref:
            links.append((number, ref.group(1)))
    return links


def is_placeholder(target: str) -> bool:
    return "<" in target or ">" in target or "XXXX" in target


def check_internal(path: Path, target: str) -> str | None:
    if target.startswith(("mailto:", "tel:")):
        return None
    file_part, _, anchor = target.partition("#")
    file_part = unquote(file_part)

    if file_part:
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            return f"missing file: {file_part}"
    else:
        resolved = path

    if anchor:
        if resolved.is_dir() or resolved.suffix.lower() != ".md":
            return None
        if anchor.lower() not in anchors_for(resolved):
            return f"missing anchor: #{anchor} in {resolved.relative_to(REPO_ROOT).as_posix()}"
    return None


def check_external(url: str, timeout: float = 20.0) -> str | None:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; markdown-link-checker)"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if response.status < 400:
                    return None
                status = response.status
        except urllib.error.HTTPError as error:
            status = error.code
            if method == "HEAD":
                continue  # some servers reject HEAD; retry with GET
        except Exception as error:  # noqa: BLE001 - report any network failure
            if method == "HEAD":
                continue
            return f"{type(error).__name__}: {error}"
        if method == "GET":
            return f"HTTP {status}"
    return "unreachable"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--external", action="store_true", help="also check http(s) links")
    args = parser.parse_args()

    problems: list[str] = []
    external: dict[str, list[str]] = {}
    files = iter_markdown_files()
    internal_count = 0

    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix()
        for line, target in extract_links(path):
            if is_placeholder(target):
                continue
            if target.startswith(("http://", "https://")):
                external.setdefault(target, []).append(f"{rel}:{line}")
                continue
            internal_count += 1
            error = check_internal(path, target)
            if error:
                problems.append(f"{rel}:{line}: {error}  ->  {target}")

    print(f"Checked {internal_count} internal links in {len(files)} Markdown files.")

    if args.external:
        urls = sorted(external)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check_external, urls))
        for url, error in zip(urls, results):
            if error:
                for location in external[url]:
                    problems.append(f"{location}: {error}  ->  {url}")
        print(f"Checked {len(urls)} unique external URLs.")
    else:
        print(f"Skipped {len(external)} unique external URLs (use --external to check them).")

    if problems:
        print(f"\n{len(problems)} problem(s) found:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print("All links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
