# 05 — Embeddings

> **Status:** Planned (Phase 4) · **Level:** Intermediate · **Estimated time:** 6–8 hours

## Overview

Embeddings turn text into vectors so that texts with similar meanings end up close together. This module explains what embeddings are, how sentence-embedding models are trained and used, and how to choose a model for a RAG system.

## Why This Module Matters

In dense retrieval, the embedding model decides what "similar" means. A model that does not fit your domain or language will retrieve the wrong chunks, however good the rest of the pipeline is.

## Prerequisites

- [02 — Mathematical Foundations](../02-mathematical-foundations/README.md): vectors, dot product, cosine similarity.
- [04 — Document Chunking](../04-document-chunking/README.md)

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | What is an embedding? | Beginner | Planned |
| 2 | From word vectors to sentence embeddings | Intermediate | Planned |
| 3 | Generating embeddings with sentence-transformers | Intermediate | Planned |
| 4 | Normalization and choosing a similarity function | Intermediate | Planned |
| 5 | Choosing an embedding model | Intermediate | Planned |
| 6 | Multilingual and domain-specific embeddings | Intermediate | Planned |
| 7 | Fine-tuning embedding models (introduction) | Advanced | Planned |

## Key References

- Mikolov, T. et al. (2013). *Efficient Estimation of Word Representations in Vector Space.* [arXiv:1301.3781](https://arxiv.org/abs/1301.3781)
- Devlin, J. et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.* [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- Muennighoff, N. et al. (2022). *MTEB: Massive Text Embedding Benchmark.* [arXiv:2210.07316](https://arxiv.org/abs/2210.07316)

## Navigation

**Previous:** [04 — Document Chunking](../04-document-chunking/README.md) · **Next:** [06 — Vector Databases](../06-vector-databases/README.md)
