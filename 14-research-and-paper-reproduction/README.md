# 14 — Research and Paper Reproduction

> **Status:** Planned (Phase 7) · **Level:** Advanced · **Estimated time:** Ongoing

## Overview

RAG moves quickly, and new techniques appear in papers long before they appear in tutorials. This module teaches you to read RAG papers critically, reproduce their key results on a small scale, and report your findings honestly, including when a result does not reproduce.

## Why This Module Matters

Reproducing a paper is the most reliable way to understand it. It also shows you which reported gains depend on specific datasets, models, or settings, which matters before you adopt a technique in production.

## Prerequisites

- [10 — RAG Evaluation](../10-rag-evaluation/README.md)
- [11 — Advanced RAG Architectures](../11-advanced-rag-architectures/README.md)

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | How to read a research paper | Advanced | Planned |
| 2 | Designing reproducible experiments | Advanced | Planned |
| 3 | Ablation studies | Advanced | Planned |
| 4 | Experiment tracking | Advanced | Planned |
| 5 | Reporting results honestly (including negative results) | Advanced | Planned |

## Planned Reproductions

Reproductions use the [experiment template](../templates/experiment-template.md) and are scaled down to run on modest hardware. A reduced-scale reproduction is labelled as such and is never presented as matching the paper's full setup.

| Paper | Focus | Status |
|---|---|---|
| Karpukhin et al. (2020), DPR | Dense vs BM25 retrieval on a small QA subset | Planned |
| Gao et al. (2022), HyDE | Zero-shot retrieval with hypothetical documents | Planned |
| Liu et al. (2023), Lost in the Middle | Effect of context position on answer accuracy | Planned |

## Contributing Reviews and Reproductions

- Paper reviews: [paper review template](../templates/paper-review-template.md), stored in [research-papers/](../research-papers/README.md).
- Experiments: [experiment template](../templates/experiment-template.md).

## Navigation

**Previous:** [13 — Production RAG](../13-production-rag/README.md) · **See also:** [Practical Projects](../practical-projects/README.md), [Research Papers](../research-papers/README.md)
