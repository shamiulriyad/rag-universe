# 04 — Document Chunking

> **Status:** Planned (Phase 4) · **Level:** Beginner → Intermediate · **Estimated time:** 5–7 hours

## Overview

Documents are usually too long to embed as a single vector or to place whole into a prompt. Chunking splits them into smaller pieces. The choice of chunk size, overlap, and boundaries has a direct effect on what can be retrieved.

## Why This Module Matters

Chunks that are too large dilute the signal, because one vector has to represent many topics. Chunks that are too small lose the context needed to answer a question. Boundaries that cut through a sentence or a table destroy meaning. Chunking is one of the highest-impact settings in a RAG system.

## Prerequisites

- [03 — Data Ingestion and Processing](../03-data-ingestion-and-processing/README.md)
- Helpful: the idea of tokens (see [glossary](../docs/glossary.md#t)).

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Why chunking matters | Beginner | Planned |
| 2 | Fixed-size chunking and overlap | Beginner | Planned |
| 3 | Recursive character chunking | Beginner | Planned |
| 4 | Sentence- and paragraph-based chunking | Beginner | Planned |
| 5 | Structure-aware chunking (Markdown, HTML, code) | Intermediate | Planned |
| 6 | Semantic chunking | Intermediate | Planned |
| 7 | Token-aware chunking | Intermediate | Planned |
| 8 | Comparing chunking strategies experimentally | Intermediate | Planned |

**Note:** there is no universally best chunk size. Lesson 8 shows how to choose one empirically for your own data, using the evaluation methods from [module 10](../10-rag-evaluation/README.md).

## Navigation

**Previous:** [03 — Data Ingestion and Processing](../03-data-ingestion-and-processing/README.md) · **Next:** [05 — Embeddings](../05-embeddings/README.md)
