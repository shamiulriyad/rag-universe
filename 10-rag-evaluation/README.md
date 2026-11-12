# 10 — RAG Evaluation

> **Status:** Planned (Phase 6; a minimal evaluation lesson ships in Phase 4) · **Level:** Intermediate → Advanced · **Estimated time:** 8–10 hours

## Overview

How do you know whether a change made your RAG system better? This module covers how to evaluate retrieval (did we find the right chunks?) and generation (is the answer correct and supported by the context?). It includes the math behind each metric, how to build an evaluation dataset, and the limits of automated evaluation.

## Why This Module Matters

Without evaluation, every change is a guess. Evaluation turns RAG from trial-and-error into engineering, and it is a prerequisite for the advanced, optimization, and production modules.

## Prerequisites

- [09 — Context Engineering and Generation](../09-context-engineering-and-generation/README.md), so that you have a working baseline to evaluate.
- [02 — Mathematical Foundations](../02-mathematical-foundations/README.md): probability and statistics essentials.

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Why and what to evaluate | Intermediate | Planned |
| 2 | Retrieval metrics: Hit rate, Precision@k, Recall@k | Intermediate | Planned |
| 3 | Ranking metrics: MRR and nDCG | Intermediate | Planned |
| 4 | Generation metrics: faithfulness and answer relevance | Intermediate | Planned |
| 5 | LLM-as-a-judge: methods and limitations | Advanced | Planned |
| 6 | Building an evaluation dataset | Intermediate | Planned |
| 7 | Evaluation frameworks (RAGAS and others) | Advanced | Planned |
| 8 | Public benchmarks: BEIR, MTEB, KILT | Advanced | Planned |
| 9 | Human evaluation | Advanced | Planned |

Each metric lesson includes the formula, a worked example on a small ranked list, and a from-scratch Python implementation.

## Key References

- Järvelin, K., & Kekäläinen, J. (2002). *Cumulated Gain-Based Evaluation of IR Techniques.* ACM Transactions on Information Systems, 20(4).
- Es, S. et al. (2023). *Ragas: Automated Evaluation of Retrieval Augmented Generation.* [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
- Saad-Falcon, J. et al. (2023). *ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems.* [arXiv:2311.09476](https://arxiv.org/abs/2311.09476)
- Zheng, L. et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)
- Thakur, N. et al. (2021). *BEIR.* [arXiv:2104.08663](https://arxiv.org/abs/2104.08663)
- Petroni, F. et al. (2020). *KILT: a Benchmark for Knowledge Intensive Language Tasks.* [arXiv:2009.02252](https://arxiv.org/abs/2009.02252)

## Navigation

**Previous:** [09 — Context Engineering and Generation](../09-context-engineering-and-generation/README.md) · **Next:** [08 — Advanced Retrieval Techniques](../08-advanced-retrieval-techniques/README.md) (advanced track) or [12 — RAG Optimization](../12-rag-optimization/README.md)
