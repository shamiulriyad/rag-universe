# RAG-Universe Roadmap

This document is the single source of truth for **what exists, what is being written, and what is planned**. It is updated whenever content status changes.

## Table of Contents

- [Status Labels](#status-labels)
- [Development Principles](#development-principles)
- [Phase Overview](#phase-overview)
- [Phase 1 — Initial Foundation](#phase-1--initial-foundation)
- [Phase 2 — RAG Fundamentals](#phase-2--rag-fundamentals)
- [Phase 3 — Mathematical Foundations](#phase-3--mathematical-foundations)
- [Phase 4 — Core RAG Components](#phase-4--core-rag-components)
- [Phase 5 — Advanced RAG](#phase-5--advanced-rag)
- [Phase 6 — Evaluation and Production](#phase-6--evaluation-and-production)
- [Phase 7 — Research and Projects](#phase-7--research-and-projects)
- [Topic Ownership](#topic-ownership)
- [Proposing Changes to the Roadmap](#proposing-changes-to-the-roadmap)

## Status Labels

| Label | Meaning |
|---|---|
| **Planned** | Scope is defined. No lesson content yet. |
| **In progress** | Content exists but is incomplete or not yet reviewed. |
| **Complete** | Written, technically reviewed, links verified, exercises included where relevant. |

A lesson is never marked **Complete** until it has been reviewed for correctness. A checked box (`[x]`) in this file means **Complete**.

## Development Principles

1. **One phase at a time.** A new phase begins only when it is explicitly started by the maintainers.
2. **Baseline before advanced.** Every advanced technique is compared against a simple baseline.
3. **From scratch before frameworks.** Core ideas are implemented with plain Python/NumPy before libraries are introduced.
4. **Verified sources only.** No invented benchmarks, results, or citations.
5. **One home per concept.** Each concept is taught in exactly one module; other modules link to it (see [Topic Ownership](#topic-ownership)).

## Phase Overview

| Phase | Scope | Modules | Status |
|---|---|---|---|
| 1 | Initial foundation | Repository structure, docs, templates | Complete |
| 2 | RAG fundamentals | [01](01-rag-fundamentals/README.md) | Planned |
| 3 | Mathematical foundations | [02](02-mathematical-foundations/README.md) | Planned |
| 4 | Core RAG components | [03](03-data-ingestion-and-processing/README.md), [04](04-document-chunking/README.md), [05](05-embeddings/README.md), [06](06-vector-databases/README.md), [07](07-information-retrieval/README.md), [09](09-context-engineering-and-generation/README.md) | Planned |
| 5 | Advanced RAG | [08](08-advanced-retrieval-techniques/README.md), [11](11-advanced-rag-architectures/README.md) | Planned |
| 6 | Evaluation and production | [10](10-rag-evaluation/README.md), [12](12-rag-optimization/README.md), [13](13-production-rag/README.md) | Planned |
| 7 | Research and projects | [14](14-research-and-paper-reproduction/README.md), [projects](practical-projects/README.md), [papers](research-papers/README.md) | Planned |

> Note on ordering: module 10 (evaluation) is developed in Phase 6, but a minimal evaluation lesson is introduced in Phase 4 so that core components can be measured from the start.

## Phase 1 — Initial Foundation

Status: **Complete**

- [x] Repository folder structure
- [x] Root `README.md`
- [x] `ROADMAP.md`
- [x] `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`
- [x] [Learning path](docs/learning-path.md)
- [x] [Prerequisites](docs/prerequisites.md)
- [x] [How to use this repository](docs/how-to-use-this-repository.md)
- [x] [Glossary](docs/glossary.md) (starter set)
- [x] Content templates: [topic](templates/topic-template.md), [paper review](templates/paper-review-template.md), [experiment](templates/experiment-template.md)
- [x] GitHub issue templates and pull request template
- [x] Module index files (`README.md` in every module)
- [x] Verified starter reading list in [research-papers](research-papers/README.md)
- [x] Internal link checker ([scripts/check_links.py](scripts/check_links.py)) and CI workflow

## Phase 2 — RAG Fundamentals

Status: **Planned** · Module: [01 — RAG Fundamentals](01-rag-fundamentals/README.md)

- [ ] [What is RAG?](01-rag-fundamentals/what-is-rag.md)
- [ ] [Why RAG?](01-rag-fundamentals/why-rag.md)
- [ ] [RAG vs Fine-tuning](01-rag-fundamentals/rag-vs-fine-tuning.md)
- [ ] [RAG Architecture](01-rag-fundamentals/rag-architecture.md)
- [ ] [The Complete RAG Workflow](01-rag-fundamentals/rag-workflow.md)
- [ ] Minimal "RAG in 50 lines" example (plain Python, no framework)
- [ ] Glossary expanded with all terms used in module 01

## Phase 3 — Mathematical Foundations

Status: **Planned** · Module: [02 — Mathematical Foundations](02-mathematical-foundations/README.md)

- [ ] Vectors and vector spaces
- [ ] Matrices and matrix multiplication
- [ ] Dot product
- [ ] Norms and Euclidean distance
- [ ] Cosine similarity
- [ ] Probability and statistics essentials
- [ ] Softmax and temperature
- [ ] The attention mechanism
- [ ] Embedding spaces (geometry and intuition)
- [ ] Similarity search: the math of nearest neighbours
- [ ] TF-IDF scoring
- [ ] BM25 scoring

Every lesson in this phase includes a worked numerical example small enough to verify by hand, plus a NumPy implementation that reproduces it.

## Phase 4 — Core RAG Components

Status: **Planned**

**[03 — Data Ingestion and Processing](03-data-ingestion-and-processing/README.md)**
- [ ] Document formats and loaders
- [ ] Text extraction challenges (PDF layout, tables, scanned documents)
- [ ] Cleaning and normalization
- [ ] Metadata extraction
- [ ] Deduplication
- [ ] Designing an ingestion pipeline

**[04 — Document Chunking](04-document-chunking/README.md)**
- [ ] Why chunking matters
- [ ] Fixed-size chunking and overlap
- [ ] Recursive character chunking
- [ ] Sentence- and paragraph-based chunking
- [ ] Structure-aware chunking (Markdown, HTML, code)
- [ ] Semantic chunking
- [ ] Token-aware chunking
- [ ] Comparing chunking strategies

**[05 — Embeddings](05-embeddings/README.md)**
- [ ] What is an embedding?
- [ ] From word vectors to sentence embeddings
- [ ] Generating embeddings with sentence-transformers
- [ ] Normalization and similarity choice
- [ ] Choosing an embedding model
- [ ] Multilingual and domain-specific embeddings
- [ ] Fine-tuning embedding models (introduction)

**[06 — Vector Databases](06-vector-databases/README.md)**
- [ ] Exact nearest-neighbour search
- [ ] Approximate nearest-neighbour search
- [ ] Index types: Flat, IVF, HNSW, PQ
- [ ] Hands-on with FAISS
- [ ] Metadata filtering
- [ ] Choosing a vector database

**[07 — Information Retrieval](07-information-retrieval/README.md)**
- [ ] Information retrieval basics
- [ ] Inverted indexes
- [ ] Sparse retrieval with BM25
- [ ] Dense retrieval with bi-encoders
- [ ] Top-k selection and score thresholds
- [ ] Retrieval failure modes

**[09 — Context Engineering and Generation](09-context-engineering-and-generation/README.md)**
- [ ] Building the RAG prompt
- [ ] Context window budgets
- [ ] Context ordering and the "lost in the middle" effect
- [ ] Citations and grounding
- [ ] Handling missing or insufficient context
- [ ] Generation parameters

**Cross-cutting**
- [ ] Minimal evaluation lesson (hit rate and Recall@k on a small labelled set)
- [ ] End-to-end baseline RAG pipeline combining modules 03–07 and 09

## Phase 5 — Advanced RAG

Status: **Planned**

**[08 — Advanced Retrieval Techniques](08-advanced-retrieval-techniques/README.md)**
- [ ] Hybrid search
- [ ] Reciprocal Rank Fusion
- [ ] Reranking with cross-encoders
- [ ] Query rewriting and multi-query retrieval
- [ ] Hypothetical Document Embeddings (HyDE)
- [ ] Maximal Marginal Relevance (MMR)
- [ ] Parent-document and sentence-window retrieval
- [ ] Late-interaction retrieval (ColBERT)
- [ ] Query routing
- [ ] Contextual compression

**[11 — Advanced RAG Architectures](11-advanced-rag-architectures/README.md)**
- [ ] A taxonomy of RAG architectures
- [ ] Conversational RAG
- [ ] Active retrieval (FLARE)
- [ ] Self-RAG
- [ ] Corrective RAG (CRAG)
- [ ] RAPTOR (hierarchical summarization trees)
- [ ] Graph RAG
- [ ] Agentic RAG
- [ ] Multimodal RAG

## Phase 6 — Evaluation and Production

Status: **Planned**

**[10 — RAG Evaluation](10-rag-evaluation/README.md)**
- [ ] Why and what to evaluate
- [ ] Retrieval metrics: Hit rate, Precision@k, Recall@k
- [ ] Ranking metrics: MRR and nDCG
- [ ] Generation metrics: faithfulness and answer relevance
- [ ] LLM-as-a-judge: methods and limitations
- [ ] Building an evaluation dataset
- [ ] Evaluation frameworks (RAGAS and others)
- [ ] Public benchmarks (BEIR, MTEB, KILT)
- [ ] Human evaluation

**[12 — RAG Optimization](12-rag-optimization/README.md)**
- [ ] Profiling a RAG pipeline
- [ ] Tuning chunking and retrieval parameters
- [ ] ANN index parameter tuning
- [ ] Caching strategies
- [ ] Vector compression and quantization
- [ ] Matryoshka embeddings and dimension reduction
- [ ] Cost optimization

**[13 — Production RAG](13-production-rag/README.md)**
- [ ] Reference architecture
- [ ] Serving RAG behind an API
- [ ] Incremental indexing and document updates
- [ ] Observability and monitoring
- [ ] Security: prompt injection and data leakage
- [ ] Access control and multi-tenancy
- [ ] Privacy and compliance considerations
- [ ] Scaling and deployment
- [ ] Continuous evaluation and regression testing

## Phase 7 — Research and Projects

Status: **Planned**

**[14 — Research and Paper Reproduction](14-research-and-paper-reproduction/README.md)**
- [ ] How to read a research paper
- [ ] Designing reproducible experiments
- [ ] Ablation studies
- [ ] Experiment tracking
- [ ] Reporting results honestly

**[Practical Projects](practical-projects/README.md)**
- [ ] P1: Minimal RAG from scratch
- [ ] P2: Document Q&A over PDFs
- [ ] P3: Hybrid search assistant with reranking
- [ ] P4: RAG with an evaluation harness
- [ ] P5: Production-style RAG service
- [ ] P6: Graph RAG mini-project

**[Research Papers](research-papers/README.md)**
- [x] Verified starter reading list
- [ ] Paper reviews (using the [paper review template](templates/paper-review-template.md))
- [ ] Reproduction reports (using the [experiment template](templates/experiment-template.md))

## Topic Ownership

To avoid duplicate lessons, each concept has one home module. Other modules link to it instead of re-teaching it.

| Concept | Home module | Linked from |
|---|---|---|
| Cosine similarity, dot product, Euclidean distance | 02 | 05, 06, 07 |
| TF-IDF and BM25 **scoring formulas** | 02 | 07 |
| BM25 **as a retrieval system** (inverted index, implementation) | 07 | 08 |
| Softmax and attention | 02 | 05, 09 |
| Embedding models | 05 | 06, 07 |
| ANN index structures (HNSW, IVF, PQ) | 06 | 12 |
| Metadata filtering | 06 | 07, 13 |
| Reranking | 08 | 11, 12 |
| Evaluation metric definitions | 10 | 08, 12, 14 |
| Prompt injection and security | 13 | 09 |

## Proposing Changes to the Roadmap

Open an issue using the **Topic request** template. New topics are added only when they fit the learning path and do not duplicate an existing topic. See [CONTRIBUTING.md](CONTRIBUTING.md).
