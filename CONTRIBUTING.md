# Contributing to RAG-Universe

Thank you for helping make RAG-Universe a reliable place to learn Retrieval-Augmented Generation. This guide explains what we accept, how to write content that fits the repository, and how reviews work.

By participating you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Reporting Errors](#reporting-errors)
- [Before You Start Writing](#before-you-start-writing)
- [Content Standards](#content-standards)
- [Mathematics Standards](#mathematics-standards)
- [Diagram Standards](#diagram-standards)
- [Python Code Standards](#python-code-standards)
- [Citations and Sources](#citations-and-sources)
- [File and Folder Conventions](#file-and-folder-conventions)
- [Pull Request Process](#pull-request-process)
- [Review Checklist](#review-checklist)

## Ways to Contribute

| Contribution | How |
|---|---|
| Fix a typo or small error | Open a pull request directly. |
| Report a technical inaccuracy | Open a **Content error** issue. |
| Report a broken link | Open a **Broken link** issue, or fix it in a pull request. |
| Propose a new topic | Open a **Topic request** issue first. Do not start writing until it is accepted. |
| Write a planned lesson | Comment on the related issue or roadmap item to avoid duplicate work, then follow this guide. |
| Add a paper review | Use the [paper review template](templates/paper-review-template.md). |
| Add an experiment or reproduction | Use the [experiment template](templates/experiment-template.md). |
| Improve diagrams | Follow the [diagram conventions](diagrams/README.md). |

## Reporting Errors

Technical accuracy is this project's most important property. If you find something wrong, such as an incorrect formula, a misattributed paper, an outdated API, or a misleading explanation, please open an issue with the **Content error** template. Include:

- The file and section.
- What is wrong.
- What you believe is correct, with a source (paper, official documentation) if possible.

## Before You Start Writing

1. Check [ROADMAP.md](ROADMAP.md) to confirm the topic is planned and see which module owns it.
2. Check the [Topic Ownership](ROADMAP.md#topic-ownership) table. If a concept already has a home module, link to it instead of re-explaining it.
3. Copy the [topic template](templates/topic-template.md) into the correct module folder.
4. Change the lesson's status in `ROADMAP.md` and the module `README.md` to **In progress** in the same pull request.

## Content Standards

**Audience**

- State the level (Beginner, Intermediate, Advanced) and prerequisites at the top of every lesson.
- Never assume a beginner knows advanced terminology. Define each term on first use, or link to the [glossary](docs/glossary.md).
- Keep beginner and advanced material distinguishable. Put advanced detail in a clearly labelled section, or in a separate lesson.

**Structure**

- Follow the [topic template](templates/topic-template.md). Remove sections that do not apply. Do not pad lessons with sections that add nothing.
- Use one `#` heading per file (the title), then `##` and `###` in order. Do not skip levels.
- Add a table of contents to lessons longer than about five sections.
- Use relative links for everything inside the repository.

**Style**

- Clear, direct language. Short paragraphs.
- Use emojis and decorative images sparingly. Use them only when they help the reader.
- Explain *why*, not only *how*. State trade-offs and limitations.
- Distinguish **established** techniques from **experimental** ones. If a technique is recent or its benefits are not consistently replicated, say so.

**Status honesty**

- Do not mark content **Complete** until it has been reviewed.
- Unfinished sections must be marked, for example: `> Status: In progress — exercises not yet written.`

## Mathematics Standards

- Write equations in LaTeX using GitHub's math syntax: `$...$` inline and `$$...$$` for display.
- Define every symbol the first time it appears.
- Every formula that matters in practice gets a **worked example** with small numbers (for example 3-dimensional vectors) that a reader can verify by hand.
- Where possible, include a few lines of NumPy that reproduce the worked example, so readers can check the arithmetic.
- State assumptions, for example "vectors are L2-normalized".

## Diagram Standards

- Prefer original diagrams in **Mermaid**, embedded directly in Markdown. Use **SVG** when Mermaid cannot express the diagram.
- Every diagram needs a short text explanation nearby. A diagram should not be the only place where information appears.
- External images must have a stable source, a compatible license, and visible attribution. Do not add decorative or unverified images.
- See [diagrams/README.md](diagrams/README.md) for naming and storage conventions.

## Python Code Standards

- Target **Python 3.10+**.
- Keep examples small, modular, and readable. Prefer clarity over cleverness.
- **Fundamentals first:** core lessons use the standard library and NumPy. Introduce frameworks (LangChain, LlamaIndex, etc.) only when they help explain a real implementation, and only after the from-scratch version exists.
- List dependencies with pinned versions in a `requirements.txt` next to the code, and mention them in the lesson.
- Make examples reproducible: fix random seeds, avoid hidden state, and document any downloaded models or datasets (name, version, source).
- Never commit API keys or secrets. Read them from environment variables and document which variables are needed.
- Add tests (`pytest`) for reusable functions when practical.
- Explain the important lines of code in the lesson text. Do not drop in code without explanation.

Code placement inside a module:

```text
NN-module-name/
├── README.md
├── lesson-name.md
└── code/
    └── lesson-name/
        ├── requirements.txt
        ├── example.py
        └── test_example.py
```

## Citations and Sources

- Prefer **original research papers** and **official documentation** over blog posts.
- For papers, include authors (first author + "et al." when more than two), year, title, venue if known, and a stable link (arXiv abstract page, DOI, or proceedings page).
- Verify every link before adding it.
- **Never invent** benchmarks, numbers, quotes, results, or citations. If you report a number from a paper, cite the table or section it came from.
- If you ran an experiment yourself, report the setup with the [experiment template](templates/experiment-template.md) so others can reproduce it.

## File and Folder Conventions

- File and folder names: lowercase, hyphen-separated (`cosine-similarity.md`).
- Module folders keep their numeric prefix (`05-embeddings/`). Do not renumber existing modules, because that breaks links.
- Each module `README.md` contains the overview, the lesson table with statuses, and navigation links.

## Pull Request Process

1. Fork the repository and create a branch: `content/<module>-<topic>`, `fix/<short-description>`, or `docs/<short-description>`.
2. Make focused changes. Use one lesson or one fix per pull request where possible.
3. Run the link checker locally:

   ```bash
   python scripts/check_links.py
   ```

4. Update `ROADMAP.md`, the module `README.md`, and `CHANGELOG.md` (under **Unreleased**) if status changed.
5. Open a pull request and complete the template.
6. A maintainer reviews for technical accuracy, clarity, and consistency. Expect questions. Accuracy reviews are thorough by design.

## Review Checklist

Reviewers check that:

- [ ] Technical content is correct and sources are cited and verified.
- [ ] No invented benchmarks, numbers, or citations.
- [ ] Level and prerequisites are stated. Terms are defined or linked to the glossary.
- [ ] Math has defined symbols and a worked example.
- [ ] Code runs on Python 3.10+, has pinned dependencies, and is explained.
- [ ] Diagrams are original or properly attributed, and explained in text.
- [ ] Internal links pass `scripts/check_links.py`.
- [ ] Status labels are accurate in the lesson, module README, and ROADMAP.
- [ ] No duplication of a topic owned by another module.
