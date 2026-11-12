# Tools and Frameworks

Open-source libraries and systems used or discussed in RAG-Universe. Links point to the official source repositories or project sites, checked on 2026-11-12.

**Policy:** fundamental lessons use only the Python standard library and NumPy. Libraries are introduced in the module where they help explain a real implementation. This list is descriptive, not an endorsement. Check each project's license and maintenance status before using it.

## Numerical Computing and Models

| Tool | What it is | Introduced in |
|---|---|---|
| [NumPy](https://github.com/numpy/numpy) | N-dimensional arrays and linear algebra for Python | [02](../02-mathematical-foundations/README.md) |
| [Hugging Face Transformers](https://github.com/huggingface/transformers) | Pre-trained Transformer models and tokenizers | [05](../05-embeddings/README.md) |
| [Sentence Transformers](https://www.sbert.net/) | Library for sentence embeddings and cross-encoders | [05](../05-embeddings/README.md), [08](../08-advanced-retrieval-techniques/README.md) |
| [tiktoken](https://github.com/openai/tiktoken) | Fast BPE tokenizer used with OpenAI models | [04](../04-document-chunking/README.md), [09](../09-context-engineering-and-generation/README.md) |

## Document Loading and Parsing

| Tool | What it is | Introduced in |
|---|---|---|
| [pypdf](https://github.com/py-pdf/pypdf) | Pure-Python PDF reader | [03](../03-data-ingestion-and-processing/README.md) |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Partitioning and extraction for many document types | [03](../03-data-ingestion-and-processing/README.md) |

## Sparse Retrieval

| Tool | What it is | Introduced in |
|---|---|---|
| [rank_bm25](https://github.com/dorianbrown/rank_bm25) | Small Python implementation of BM25 variants | [07](../07-information-retrieval/README.md) |
| [OpenSearch](https://github.com/opensearch-project/OpenSearch) | Search engine with BM25 and vector search | [08](../08-advanced-retrieval-techniques/README.md), [13](../13-production-rag/README.md) |

## Vector Search Libraries and Databases

| Tool | What it is | Introduced in |
|---|---|---|
| [FAISS](https://github.com/facebookresearch/faiss) | Library for efficient similarity search and clustering of dense vectors | [06](../06-vector-databases/README.md) |
| [hnswlib](https://github.com/nmslib/hnswlib) | Header-only HNSW implementation with Python bindings | [06](../06-vector-databases/README.md) |
| [Chroma](https://github.com/chroma-core/chroma) | Embedding database | [06](../06-vector-databases/README.md) |
| [Qdrant](https://github.com/qdrant/qdrant) | Vector database | [06](../06-vector-databases/README.md) |
| [Weaviate](https://github.com/weaviate/weaviate) | Vector database | [06](../06-vector-databases/README.md) |
| [Milvus](https://github.com/milvus-io/milvus) | Vector database | [06](../06-vector-databases/README.md) |
| [pgvector](https://github.com/pgvector/pgvector) | Vector similarity search extension for PostgreSQL | [06](../06-vector-databases/README.md), [13](../13-production-rag/README.md) |

## RAG and LLM Application Frameworks

| Tool | What it is | Introduced in |
|---|---|---|
| [LangChain](https://github.com/langchain-ai/langchain) | Framework for composing LLM applications | [09](../09-context-engineering-and-generation/README.md) and later |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Data framework for LLM applications | [09](../09-context-engineering-and-generation/README.md) and later |
| [Haystack](https://github.com/deepset-ai/haystack) | Framework for building search and RAG pipelines | [09](../09-context-engineering-and-generation/README.md) and later |

## Evaluation

| Tool | What it is | Introduced in |
|---|---|---|
| [Ragas](https://github.com/explodinggradients/ragas) | Evaluation toolkit for RAG pipelines | [10](../10-rag-evaluation/README.md) |
| [MTEB](https://github.com/embeddings-benchmark/mteb) | Benchmark for text embedding models | [05](../05-embeddings/README.md), [10](../10-rag-evaluation/README.md) |
| [BEIR](https://github.com/beir-cellar/beir) | Heterogeneous IR benchmark | [10](../10-rag-evaluation/README.md) |

## Local LLM Runtimes

| Tool | What it is | Introduced in |
|---|---|---|
| [Ollama](https://github.com/ollama/ollama) | Run open-weight LLMs locally | [09](../09-context-engineering-and-generation/README.md) |

---

**Other resources:** [Books](books.md) · [Courses](courses.md) · [Videos](videos.md) · [Datasets](datasets.md)
