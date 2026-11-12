# 07 — Information Retrieval

> **Status:** Planned (Phase 4) · **Level:** Intermediate · **Estimated time:** 6–8 hours

## Overview

Retrieval is the "R" in RAG. This module covers the two main families of retrieval: **sparse** (keyword-based, such as BM25) and **dense** (embedding-based). It also covers how to select the top-k results and how retrieval typically fails.

## Why This Module Matters

If the right chunk is not retrieved, the LLM cannot use it. Retrieval quality limits answer quality. Knowing both sparse and dense retrieval, and when each one fails, prepares you for the hybrid methods in [module 08](../08-advanced-retrieval-techniques/README.md).

## Prerequisites

- [02 — Mathematical Foundations](../02-mathematical-foundations/README.md): TF-IDF, BM25, cosine similarity.
- [06 — Vector Databases](../06-vector-databases/README.md)

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Information retrieval basics: queries, documents, relevance | Beginner | Planned |
| 2 | Inverted indexes | Intermediate | Planned |
| 3 | Sparse retrieval with BM25 (implementation) | Intermediate | Planned |
| 4 | Dense retrieval with bi-encoders | Intermediate | Planned |
| 5 | Top-k selection and score thresholds | Intermediate | Planned |
| 6 | Retrieval failure modes | Intermediate | Planned |

## Key References

- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval.* [Online edition](https://nlp.stanford.edu/IR-book/)
- Karpukhin, V. et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering.* [arXiv:2004.04906](https://arxiv.org/abs/2004.04906)
- Thakur, N. et al. (2021). *BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models.* [arXiv:2104.08663](https://arxiv.org/abs/2104.08663)

## Navigation

**Previous:** [06 — Vector Databases](../06-vector-databases/README.md) · **Next (core path):** [09 — Context Engineering and Generation](../09-context-engineering-and-generation/README.md) · **Next (specialization):** [08 — Advanced Retrieval Techniques](../08-advanced-retrieval-techniques/README.md)
