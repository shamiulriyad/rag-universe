# 06 — Vector Databases

> **Status:** Planned (Phase 4) · **Level:** Intermediate · **Estimated time:** 6–8 hours

## Overview

Once you have millions of embeddings, comparing a query against every one of them becomes too slow. This module explains exact and approximate nearest-neighbour search, the index structures that make search fast (Flat, IVF, HNSW, PQ), and how vector databases add storage, filtering, and updates on top of them.

## Why This Module Matters

The index determines the latency, memory use, and recall of retrieval. Approximate indexes can silently miss relevant results if their parameters are poorly configured, so you need to understand what they trade away.

## Prerequisites

- [05 — Embeddings](../05-embeddings/README.md)
- [02 — Mathematical Foundations](../02-mathematical-foundations/README.md): distances and similarity.

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Exact nearest-neighbour search | Intermediate | Planned |
| 2 | Approximate nearest-neighbour search: the speed/recall trade-off | Intermediate | Planned |
| 3 | Index types: Flat, IVF, HNSW, Product Quantization | Intermediate | Planned |
| 4 | Hands-on with FAISS | Intermediate | Planned |
| 5 | Metadata filtering | Intermediate | Planned |
| 6 | Choosing a vector database | Intermediate | Planned |

Lesson 6 will compare vector databases by **criteria** (deployment model, filtering, scalability, licensing) rather than by unverified performance claims.

## Key References

- Malkov, Y. A., & Yashunin, D. A. (2016). *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs.* [arXiv:1603.09320](https://arxiv.org/abs/1603.09320)
- Johnson, J., Douze, M., & Jégou, H. (2017). *Billion-scale similarity search with GPUs.* [arXiv:1702.08734](https://arxiv.org/abs/1702.08734)
- FAISS documentation and source: [github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss)

## Navigation

**Previous:** [05 — Embeddings](../05-embeddings/README.md) · **Next:** [07 — Information Retrieval](../07-information-retrieval/README.md)
