# How to Use This Repository

This page explains how RAG-Universe is organized, how lessons are structured, and how to get the most out of it. Reading it takes about five minutes.

## Table of Contents

- [Repository Layout](#repository-layout)
- [How a Module Is Organized](#how-a-module-is-organized)
- [How a Lesson Is Structured](#how-a-lesson-is-structured)
- [Levels and Status Labels](#levels-and-status-labels)
- [Reading the Math](#reading-the-math)
- [Reading the Diagrams](#reading-the-diagrams)
- [Running the Code](#running-the-code)
- [Suggested Study Habits](#suggested-study-habits)
- [Getting Help](#getting-help)

## Repository Layout

| Folder | What you will find |
|---|---|
| `docs/` | Orientation material: this guide, the [learning path](learning-path.md), [prerequisites](prerequisites.md), and the [glossary](glossary.md). |
| `01-…` to `14-…` | The learning modules, numbered in recommended order. |
| `practical-projects/` | End-to-end projects that combine several modules. |
| `research-papers/` | A curated reading list and paper reviews. |
| `resources/` | Books, courses, videos, tools, and datasets. |
| `diagrams/` | Diagram conventions and shared diagram sources. |
| `templates/` | Templates contributors use to write new content. |
| `scripts/` | Maintenance tools, such as the link checker. |

## How a Module Is Organized

Every module folder has a `README.md` that contains:

1. **Overview**: what the module covers and why it matters for RAG.
2. **Level and prerequisites**: what you should know before starting.
3. **Lesson table**: every lesson in order, with its level and status.
4. **Key references**: the most important papers or documentation for the module.
5. **Navigation**: links to the previous and next modules.

Lessons are Markdown files inside the module folder. When a lesson has code, it lives in `code/<lesson-name>/` inside the same module.

## How a Lesson Is Structured

Lessons follow a consistent format based on the [topic template](../templates/topic-template.md). A lesson uses only the sections that are relevant to it:

1. Learning Objectives
2. Prerequisites
3. What is this concept?
4. Why is it needed in RAG?
5. How does it work internally?
6. Mathematical Foundations
7. Step-by-step explanation
8. Visual diagrams
9. Python implementation
10. Practical examples
11. Advantages and limitations
12. Common mistakes
13. Performance considerations
14. Exercises
15. Mini project
16. Further reading and research papers
17. Summary

Because the order is always the same, you can skip a section and return to it later. For example, you can read **Summary** first to preview a lesson, or go straight to **Exercises** to test yourself.

## Levels and Status Labels

**Levels** tell you who a lesson is written for:

| Level | Assumes |
|---|---|
| Beginner | Basic Python only. Every term is explained. |
| Intermediate | Python, basic ML/NLP, and experience calling an LLM. |
| Advanced | Comfort with the core RAG pipeline, and interest in research, optimization, or production. |

**Status labels** tell you whether content is ready:

| Status | Meaning |
|---|---|
| Planned | The topic is scoped but not yet written. |
| In progress | Some content exists but is incomplete or not yet reviewed. |
| Complete | Written, reviewed, and link-checked. |

If a lesson you need is still Planned, the module README and the [research papers list](../research-papers/README.md) point to reliable external material in the meantime.

## Reading the Math

Equations are written in LaTeX, and GitHub renders them. Every symbol is defined when it first appears, and important formulas come with a worked example using small numbers. Work through the examples with pen and paper. This is the fastest way to build intuition.

If an equation does not render, view the file on GitHub rather than in a plain-text viewer.

## Reading the Diagrams

Most diagrams are written in [Mermaid](https://mermaid.js.org/), which GitHub renders automatically. Each diagram has a text explanation next to it. See [diagrams/README.md](../diagrams/README.md) for the conventions.

## Running the Code

Code lessons will include a `requirements.txt`. The general workflow is:

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 2. Install the lesson's dependencies
pip install -r <module>/code/<lesson>/requirements.txt

# 3. Run the example
python <module>/code/<lesson>/example.py
```

Lessons that call a hosted LLM API say so explicitly, list the environment variables they need, and, where practical, offer a local alternative. Fundamental lessons are designed to run without any API key.

## Suggested Study Habits

- **Type the code yourself** instead of copying it.
- **Do the exercises.** They are designed to expose common misunderstandings.
- **Change one thing at a time** in experiments, such as chunk size, top-k, or the embedding model, and observe the effect.
- **Read at least one original paper per module.** The reading list tells you where to start.
- **Keep notes in your own words.** If you cannot explain a concept simply, revisit the lesson.

## Getting Help

- If something is unclear or incorrect, open an issue. See [CONTRIBUTING.md](../CONTRIBUTING.md#reporting-errors).
- If a term is unfamiliar, check the [glossary](glossary.md).
- If you are unsure what to study next, see the [learning path](learning-path.md).
