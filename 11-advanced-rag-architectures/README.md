# 11 — Advanced RAG Architectures

> **Status:** Planned (Phase 5) · **Level:** Advanced · **Estimated time:** 12–15 hours

## Overview

Beyond the "retrieve once, then generate" pipeline, researchers and engineers have proposed architectures that decide *when* to retrieve, *critique* what was retrieved, organize knowledge as *graphs* or *trees*, or let an *agent* plan multi-step retrieval. This module explains how these architectures work, what problems they target, and what they cost.

## Why This Module Matters

Advanced architectures can help with multi-hop questions, global "summarize the whole corpus" questions, and noisy retrieval. They also add latency, cost, and failure modes. Knowing them lets you choose one deliberately instead of following trends.

## Prerequisites

- [08 — Advanced Retrieval Techniques](../08-advanced-retrieval-techniques/README.md)
- [10 — RAG Evaluation](../10-rag-evaluation/README.md)

## Planned Lessons

| # | Lesson | Level | Maturity | Status |
|---|---|---|---|---|
| 1 | A taxonomy of RAG architectures | Advanced | — | Planned |
| 2 | Conversational RAG (multi-turn, query condensation) | Advanced | Common practice | Planned |
| 3 | Active retrieval (FLARE) | Advanced | Research | Planned |
| 4 | Self-RAG | Advanced | Research | Planned |
| 5 | Corrective RAG (CRAG) | Advanced | Research | Planned |
| 6 | RAPTOR: hierarchical summarization trees | Advanced | Research | Planned |
| 7 | Graph RAG | Advanced | Emerging | Planned |
| 8 | Agentic RAG | Advanced | Emerging | Planned |
| 9 | Multimodal RAG | Advanced | Emerging | Planned |

**Maturity labels.** *Research* means the method was proposed in a paper, and reported results come from that paper's setting. *Emerging* means it is in active development across tools and research, and terminology and best practices are still settling. *Common practice* means it is widely deployed in engineering. Lessons will report published results only with citations, and will not generalize them beyond the original setting.

## Key References

- Jiang, Z. et al. (2023). *Active Retrieval Augmented Generation* (FLARE). [arXiv:2305.06983](https://arxiv.org/abs/2305.06983)
- Asai, A. et al. (2023). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection.* [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan, S.-Q. et al. (2024). *Corrective Retrieval Augmented Generation.* [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Sarthi, P. et al. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval.* [arXiv:2401.18059](https://arxiv.org/abs/2401.18059)
- Edge, D. et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization.* [arXiv:2404.16130](https://arxiv.org/abs/2404.16130)
- Shi, W. et al. (2023). *REPLUG: Retrieval-Augmented Black-Box Language Models.* [arXiv:2301.12652](https://arxiv.org/abs/2301.12652)

## Navigation

**Previous:** [08 — Advanced Retrieval Techniques](../08-advanced-retrieval-techniques/README.md) · **Next:** [12 — RAG Optimization](../12-rag-optimization/README.md)
