# Research Papers

> **Status:** Starter reading list complete. Paper reviews planned (Phase 7).

A curated, verified reading list for RAG and the information retrieval research it builds on. Every entry links to a stable source (an arXiv abstract page where available). arXiv identifiers, titles, first authors, and years were checked against the arXiv API when the list was compiled (2026-11-12).

## Table of Contents

- [How to Use This List](#how-to-use-this-list)
- [Start Here](#start-here)
- [Foundations: Language Models and Representations](#foundations-language-models-and-representations)
- [Retrieval](#retrieval)
- [Vector Search](#vector-search)
- [Retrieval-Augmented Language Models](#retrieval-augmented-language-models)
- [Advanced RAG Methods](#advanced-rag-methods)
- [Context Use and Generation](#context-use-and-generation)
- [Evaluation and Benchmarks](#evaluation-and-benchmarks)
- [Security](#security)
- [Paper Reviews](#paper-reviews)
- [Adding a Paper](#adding-a-paper)

## How to Use This List

- **Year** is the year of first public release (usually the arXiv v1 date). Conference versions may appear the following year.
- **Module** links to where the paper is discussed in this repository.
- Papers are listed for their influence or teaching value. Inclusion does not mean the method is the best choice today.

## Start Here

If you read only three papers:

1. Lewis et al. (2020): the paper that named RAG.
2. Karpukhin et al. (2020): dense passage retrieval, the retriever design behind much of modern RAG.
3. Gao et al. (2023): a broad survey of RAG techniques.

## Foundations: Language Models and Representations

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2013 | Efficient Estimation of Word Representations in Vector Space | Mikolov et al. | [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) | [05](../05-embeddings/README.md) |
| 2017 | Attention Is All You Need | Vaswani et al. | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | [02](../02-mathematical-foundations/README.md) |
| 2018 | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | Devlin et al. | [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) | [05](../05-embeddings/README.md) |
| 2019 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Reimers & Gurevych | [arXiv:1908.10084](https://arxiv.org/abs/1908.10084) | [05](../05-embeddings/README.md) |
| 2022 | Matryoshka Representation Learning | Kusupati et al. | [arXiv:2205.13147](https://arxiv.org/abs/2205.13147) | [12](../12-rag-optimization/README.md) |

## Retrieval

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 1998 | The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries | Carbonell & Goldstein | SIGIR 1998 | [08](../08-advanced-retrieval-techniques/README.md) |
| 2009 | The Probabilistic Relevance Framework: BM25 and Beyond | Robertson & Zaragoza | Foundations and Trends in IR 3(4) | [02](../02-mathematical-foundations/README.md), [07](../07-information-retrieval/README.md) |
| 2009 | Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods | Cormack, Clarke & Büttcher | SIGIR 2009 | [08](../08-advanced-retrieval-techniques/README.md) |
| 2019 | Passage Re-ranking with BERT | Nogueira & Cho | [arXiv:1901.04085](https://arxiv.org/abs/1901.04085) | [08](../08-advanced-retrieval-techniques/README.md) |
| 2020 | Dense Passage Retrieval for Open-Domain Question Answering | Karpukhin et al. | [arXiv:2004.04906](https://arxiv.org/abs/2004.04906) | [07](../07-information-retrieval/README.md) |
| 2020 | ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT | Khattab & Zaharia | [arXiv:2004.12832](https://arxiv.org/abs/2004.12832) | [08](../08-advanced-retrieval-techniques/README.md) |
| 2022 | Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE) | Gao et al. | [arXiv:2212.10496](https://arxiv.org/abs/2212.10496) | [08](../08-advanced-retrieval-techniques/README.md) |
| 2023 | Query Rewriting for Retrieval-Augmented Large Language Models | Ma et al. | [arXiv:2305.14283](https://arxiv.org/abs/2305.14283) | [08](../08-advanced-retrieval-techniques/README.md) |
| 2023 | Dense X Retrieval: What Retrieval Granularity Should We Use? | Chen et al. | [arXiv:2312.06648](https://arxiv.org/abs/2312.06648) | [04](../04-document-chunking/README.md), [08](../08-advanced-retrieval-techniques/README.md) |

## Vector Search

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2016 | Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs | Malkov & Yashunin | [arXiv:1603.09320](https://arxiv.org/abs/1603.09320) | [06](../06-vector-databases/README.md) |
| 2017 | Billion-scale similarity search with GPUs | Johnson, Douze & Jégou | [arXiv:1702.08734](https://arxiv.org/abs/1702.08734) | [06](../06-vector-databases/README.md) |
| 2024 | The Faiss library | Douze et al. | [arXiv:2401.08281](https://arxiv.org/abs/2401.08281) | [06](../06-vector-databases/README.md), [12](../12-rag-optimization/README.md) |

## Retrieval-Augmented Language Models

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2020 | REALM: Retrieval-Augmented Language Model Pre-Training | Guu et al. | [arXiv:2002.08909](https://arxiv.org/abs/2002.08909) | [01](../01-rag-fundamentals/README.md) |
| 2020 | **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** | Lewis et al. | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) | [01](../01-rag-fundamentals/README.md) |
| 2020 | Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering (FiD) | Izacard & Grave | [arXiv:2007.01282](https://arxiv.org/abs/2007.01282) | [09](../09-context-engineering-and-generation/README.md) |
| 2021 | Improving language models by retrieving from trillions of tokens (RETRO) | Borgeaud et al. | [arXiv:2112.04426](https://arxiv.org/abs/2112.04426) | [11](../11-advanced-rag-architectures/README.md) |
| 2023 | REPLUG: Retrieval-Augmented Black-Box Language Models | Shi et al. | [arXiv:2301.12652](https://arxiv.org/abs/2301.12652) | [11](../11-advanced-rag-architectures/README.md) |
| 2023 | **Retrieval-Augmented Generation for Large Language Models: A Survey** | Gao et al. | [arXiv:2312.10997](https://arxiv.org/abs/2312.10997) | [01](../01-rag-fundamentals/README.md) |

## Advanced RAG Methods

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2023 | Active Retrieval Augmented Generation (FLARE) | Jiang et al. | [arXiv:2305.06983](https://arxiv.org/abs/2305.06983) | [11](../11-advanced-rag-architectures/README.md) |
| 2023 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | Asai et al. | [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) | [11](../11-advanced-rag-architectures/README.md) |
| 2024 | Corrective Retrieval Augmented Generation (CRAG) | Yan et al. | [arXiv:2401.15884](https://arxiv.org/abs/2401.15884) | [11](../11-advanced-rag-architectures/README.md) |
| 2024 | RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval | Sarthi et al. | [arXiv:2401.18059](https://arxiv.org/abs/2401.18059) | [11](../11-advanced-rag-architectures/README.md) |
| 2024 | From Local to Global: A Graph RAG Approach to Query-Focused Summarization | Edge et al. | [arXiv:2404.16130](https://arxiv.org/abs/2404.16130) | [11](../11-advanced-rag-architectures/README.md) |

## Context Use and Generation

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2023 | Lost in the Middle: How Language Models Use Long Contexts | Liu et al. | [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) | [09](../09-context-engineering-and-generation/README.md) |

## Evaluation and Benchmarks

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2002 | Cumulated Gain-Based Evaluation of IR Techniques | Järvelin & Kekäläinen | ACM TOIS 20(4) | [10](../10-rag-evaluation/README.md) |
| 2020 | KILT: a Benchmark for Knowledge Intensive Language Tasks | Petroni et al. | [arXiv:2009.02252](https://arxiv.org/abs/2009.02252) | [10](../10-rag-evaluation/README.md) |
| 2021 | BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models | Thakur et al. | [arXiv:2104.08663](https://arxiv.org/abs/2104.08663) | [10](../10-rag-evaluation/README.md) |
| 2022 | MTEB: Massive Text Embedding Benchmark | Muennighoff et al. | [arXiv:2210.07316](https://arxiv.org/abs/2210.07316) | [05](../05-embeddings/README.md), [10](../10-rag-evaluation/README.md) |
| 2023 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) | [10](../10-rag-evaluation/README.md) |
| 2023 | Ragas: Automated Evaluation of Retrieval Augmented Generation | Es et al. | [arXiv:2309.15217](https://arxiv.org/abs/2309.15217) | [10](../10-rag-evaluation/README.md) |
| 2023 | ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | Saad-Falcon et al. | [arXiv:2311.09476](https://arxiv.org/abs/2311.09476) | [10](../10-rag-evaluation/README.md) |

## Security

| Year | Paper | Authors | Link | Module |
|---|---|---|---|---|
| 2023 | Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Greshake et al. | [arXiv:2302.12173](https://arxiv.org/abs/2302.12173) | [13](../13-production-rag/README.md) |

## Paper Reviews

No reviews have been written yet. Reviews will be stored in this folder as `YYYY-short-name.md` (for example `2020-rag-lewis.md`) using the [paper review template](../templates/paper-review-template.md).

## Adding a Paper

1. Confirm the paper is relevant to a module in the [roadmap](../ROADMAP.md).
2. Verify the title, authors, year, and link from the original source.
3. Add it to the correct table, sorted by year.
4. Do not add claims about results here. Results belong in a paper review, with table or section references.
