# 02 — Mathematical Foundations

> **Status:** Planned (Phase 3) · **Level:** Beginner → Intermediate · **Estimated time:** 10–15 hours

## Overview

Retrieval is mathematics. Every time a RAG system decides that a chunk is "relevant", it is comparing numbers: dot products, cosine similarities, BM25 scores, softmax probabilities. This module teaches that math from first principles, with small numerical examples you can verify by hand and NumPy code that reproduces each calculation.

## Why This Module Matters

Without the math, retrieval is a black box. You cannot tell why a chunk was retrieved, why a relevant one was missed, or whether to use cosine similarity or the dot product. With it, you can debug and design retrieval systems with confidence.

## Prerequisites

- [01 — RAG Fundamentals](../01-rag-fundamentals/README.md)
- High-school algebra: squares, square roots, fractions. See [prerequisites](../docs/prerequisites.md#mathematics).

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Vectors and vector spaces | Beginner | Planned |
| 2 | Matrices and matrix multiplication | Beginner | Planned |
| 3 | The dot product | Beginner | Planned |
| 4 | Norms and Euclidean distance | Beginner | Planned |
| 5 | Cosine similarity | Beginner | Planned |
| 6 | Probability and statistics essentials | Intermediate | Planned |
| 7 | Softmax and temperature | Intermediate | Planned |
| 8 | The attention mechanism | Intermediate | Planned |
| 9 | Embedding spaces: geometry and intuition | Intermediate | Planned |
| 10 | Similarity search: the math of nearest neighbours | Intermediate | Planned |
| 11 | TF-IDF scoring | Beginner | Planned |
| 12 | BM25 scoring | Intermediate | Planned |

Every lesson includes a worked numerical example, a diagram where it helps, and a NumPy implementation.

**Scope note:** this module owns the *formulas*. Evaluation metric formulas (Precision@k, MRR, nDCG) are taught in [10 — RAG Evaluation](../10-rag-evaluation/README.md). Building a BM25 search system is covered in [07 — Information Retrieval](../07-information-retrieval/README.md).

## Key References

- Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning.* Cambridge University Press. [mml-book.github.io](https://mml-book.github.io/)
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval.* Cambridge University Press. [Online edition](https://nlp.stanford.edu/IR-book/)
- Robertson, S., & Zaragoza, H. (2009). *The Probabilistic Relevance Framework: BM25 and Beyond.* Foundations and Trends in Information Retrieval, 3(4).
- Vaswani, A. et al. (2017). *Attention Is All You Need.* [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

## Navigation

**Previous:** [01 — RAG Fundamentals](../01-rag-fundamentals/README.md) · **Next:** [03 — Data Ingestion and Processing](../03-data-ingestion-and-processing/README.md)
