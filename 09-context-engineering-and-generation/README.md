# 09 — Context Engineering and Generation

> **Status:** Planned (Phase 4) · **Level:** Intermediate · **Estimated time:** 5–7 hours

## Overview

Retrieval finds the evidence. Generation turns it into an answer. This module covers what happens between the two: how to build the prompt, how much context to include, in what order, and how to make the model cite its sources and admit when the context does not contain the answer.

## Why This Module Matters

Even with perfect retrieval, a poorly constructed prompt can lead the model to ignore the context, mix in unsupported claims, or bury the relevant chunk where the model is less likely to use it. Context engineering turns good retrieval into faithful answers.

## Prerequisites

- [07 — Information Retrieval](../07-information-retrieval/README.md)
- Experience calling an LLM, through an API or locally.

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Building the RAG prompt | Intermediate | Planned |
| 2 | Context window budgets: counting and allocating tokens | Intermediate | Planned |
| 3 | Context ordering and the "lost in the middle" effect | Intermediate | Planned |
| 4 | Citations and grounding | Intermediate | Planned |
| 5 | Handling missing or insufficient context | Intermediate | Planned |
| 6 | Generation parameters: temperature, top-p, max tokens | Intermediate | Planned |

Prompt-injection risks from retrieved content are introduced here and covered in depth in [13 — Production RAG](../13-production-rag/README.md).

## Key References

- Liu, N. F. et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- Izacard, G., & Grave, E. (2020). *Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering* (Fusion-in-Decoder). [arXiv:2007.01282](https://arxiv.org/abs/2007.01282)

## Navigation

**Previous:** [07 — Information Retrieval](../07-information-retrieval/README.md) · **Next:** [10 — RAG Evaluation](../10-rag-evaluation/README.md)
