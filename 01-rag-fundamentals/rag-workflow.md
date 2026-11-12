# The Complete RAG Workflow

> **Status:** Planned (Phase 2) · **Level:** Beginner
>
> This page is a placeholder. It lists the planned scope so contributors and learners know what is coming. The lesson content has not been written yet.

## Planned Learning Objectives

After this lesson, you will be able to:

- Trace a single question through every step of a RAG pipeline, with concrete intermediate values.
- Build a minimal RAG pipeline in plain Python, without any framework.
- Identify which step to inspect when an answer is wrong.

## Planned Outline

1. The example corpus: a handful of short documents.
2. Step 1: load and clean.
3. Step 2: chunk.
4. Step 3: embed (first with a toy bag-of-words vector, then with a real embedding model).
5. Step 4: store and index.
6. Step 5: embed the question and retrieve the top-k chunks, showing the similarity scores.
7. Step 6: build the prompt.
8. Step 7: generate the answer.
9. Debugging: where things go wrong at each step.
10. Exercises and a mini project.

## Planned Code

A minimal, framework-free implementation in `code/rag-workflow/`, with pinned dependencies and tests.

---

**Previous:** [RAG Architecture](rag-architecture.md) · [Back to module 01](README.md) · **Next module:** [02 — Mathematical Foundations](../02-mathematical-foundations/README.md)
