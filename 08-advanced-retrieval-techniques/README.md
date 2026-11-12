# 08 — Advanced Retrieval Techniques

> **Status:** Planned (Phase 5) · **Level:** Advanced · **Estimated time:** 10–12 hours

## Overview

Basic retrieval embeds the query, takes the top-k chunks, and stops. This module covers techniques that improve on that baseline. You will combine keyword and semantic search, rerank candidates with stronger models, rewrite queries, and diversify results.

## Why This Module Matters

These techniques are among the most commonly applied improvements to a baseline RAG system. Each one also adds latency, cost, or complexity, and its benefit depends on your data. Every lesson in this module therefore measures the technique against the baseline instead of assuming it helps.

## Prerequisites

- [07 — Information Retrieval](../07-information-retrieval/README.md)
- [10 — RAG Evaluation](../10-rag-evaluation/README.md) (retrieval metrics lessons), which you need to measure improvements.

## Planned Lessons

| # | Lesson | Level | Maturity | Status |
|---|---|---|---|---|
| 1 | Hybrid search: combining sparse and dense retrieval | Advanced | Established | Planned |
| 2 | Reciprocal Rank Fusion | Advanced | Established | Planned |
| 3 | Reranking with cross-encoders | Advanced | Established | Planned |
| 4 | Query rewriting and multi-query retrieval | Advanced | Emerging | Planned |
| 5 | Hypothetical Document Embeddings (HyDE) | Advanced | Emerging | Planned |
| 6 | Maximal Marginal Relevance (MMR) | Advanced | Established | Planned |
| 7 | Parent-document and sentence-window retrieval | Advanced | Common practice | Planned |
| 8 | Late-interaction retrieval (ColBERT) | Advanced | Established | Planned |
| 9 | Query routing | Advanced | Emerging | Planned |
| 10 | Contextual compression | Advanced | Emerging | Planned |

**Maturity labels.** *Established* means the technique is well studied, with peer-reviewed evidence and broad adoption. *Common practice* means it is widely used in engineering but has less formal study. *Emerging* means it is recent, its benefits vary across settings, and it should be validated on your own data.

## Key References

- Cormack, G. V., Clarke, C. L. A., & Büttcher, S. (2009). *Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods.* SIGIR 2009.
- Carbonell, J., & Goldstein, J. (1998). *The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries.* SIGIR 1998.
- Nogueira, R., & Cho, K. (2019). *Passage Re-ranking with BERT.* [arXiv:1901.04085](https://arxiv.org/abs/1901.04085)
- Khattab, O., & Zaharia, M. (2020). *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT.* [arXiv:2004.12832](https://arxiv.org/abs/2004.12832)
- Gao, L. et al. (2022). *Precise Zero-Shot Dense Retrieval without Relevance Labels* (HyDE). [arXiv:2212.10496](https://arxiv.org/abs/2212.10496)
- Ma, X. et al. (2023). *Query Rewriting for Retrieval-Augmented Large Language Models.* [arXiv:2305.14283](https://arxiv.org/abs/2305.14283)
- Chen, T. et al. (2023). *Dense X Retrieval: What Retrieval Granularity Should We Use?* [arXiv:2312.06648](https://arxiv.org/abs/2312.06648)

## Navigation

**Previous (core path):** [10 — RAG Evaluation](../10-rag-evaluation/README.md) · **Next:** [11 — Advanced RAG Architectures](../11-advanced-rag-architectures/README.md)
