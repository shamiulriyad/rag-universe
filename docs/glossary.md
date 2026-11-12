# Glossary

Plain-language definitions of terms used throughout RAG-Universe. Each entry links to the module where the concept is taught in depth.

This is a **starter glossary**. It grows as lessons are written. To propose a term, open an issue or pull request (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

**Jump to:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [V](#v)

---

## A

**Approximate Nearest Neighbour (ANN) search**: Finding vectors that are *probably* the closest to a query vector, trading a small loss in accuracy for a large gain in speed. Used when the collection is too large for exact search. See [06](../06-vector-databases/README.md).

**Attention**: The mechanism in Transformer models that lets each token weigh how relevant every other token is when building its representation. See [02](../02-mathematical-foundations/README.md).

## B

**BM25**: A ranking function for keyword search that scores documents by query-term frequency, with saturation (repeating a word helps less and less), document-length normalization, and inverse document frequency. A strong, widely used baseline. See [02](../02-mathematical-foundations/README.md) and [07](../07-information-retrieval/README.md).

**Bi-encoder**: A model that encodes the query and the document *separately* into vectors and compares them with a similarity function. Fast, because document vectors can be computed in advance. See [05](../05-embeddings/README.md).

## C

**Chunk**: A piece of a document small enough to embed and to place into an LLM prompt. See [04](../04-document-chunking/README.md).

**Chunk overlap**: The number of characters or tokens shared between consecutive chunks, so that information near a boundary is not lost. See [04](../04-document-chunking/README.md).

**Context window**: The maximum number of tokens an LLM can process in a single request, counting both input and output. See [09](../09-context-engineering-and-generation/README.md).

**Corpus**: The full collection of documents a retrieval system searches over.

**Cosine similarity**: A measure of how similar the *directions* of two vectors are, computed as their dot product divided by the product of their lengths. It ranges from −1 to 1. See [02](../02-mathematical-foundations/README.md).

**Cross-encoder**: A model that reads the query and a document *together* and outputs a relevance score. It is more accurate than a bi-encoder but much slower, so it is typically used for reranking a short list. See [08](../08-advanced-retrieval-techniques/README.md).

## D

**Dense retrieval**: Retrieval that uses embedding vectors (dense vectors, where most values are non-zero) to find semantically similar text. See [07](../07-information-retrieval/README.md).

**Dot product**: The sum of the products of corresponding entries of two vectors. For example, $(1,2)\cdot(3,4) = 1\times3 + 2\times4 = 11$. See [02](../02-mathematical-foundations/README.md).

## E

**Embedding**: A vector of numbers that represents a piece of text (or an image or other data), such that similar meanings produce nearby vectors. See [05](../05-embeddings/README.md).

**Embedding model**: A neural network that converts input text into embeddings. See [05](../05-embeddings/README.md).

**Euclidean distance**: The straight-line distance between two points (vectors). See [02](../02-mathematical-foundations/README.md).

## F

**Faithfulness (groundedness)**: The degree to which a generated answer is supported by the retrieved context, rather than invented. See [10](../10-rag-evaluation/README.md).

**Fine-tuning**: Continuing to train a pre-trained model on additional data to change its behaviour or knowledge. Often compared with RAG. See [01](../01-rag-fundamentals/README.md).

## G

**Generator**: The component of a RAG system, usually an LLM, that produces the final answer from the query and the retrieved context.

**Ground truth**: The known correct answer or set of relevant documents used to evaluate a system. See [10](../10-rag-evaluation/README.md).

## H

**Hallucination**: Output from a language model that is fluent but not supported by its input or by facts. RAG aims to reduce, but does not eliminate, hallucination.

**HNSW (Hierarchical Navigable Small World)**: A graph-based ANN index that searches by moving through layered proximity graphs ([Malkov & Yashunin, 2016](https://arxiv.org/abs/1603.09320)). See [06](../06-vector-databases/README.md).

**Hybrid search**: Combining keyword (sparse) and semantic (dense) retrieval, then merging their results. See [08](../08-advanced-retrieval-techniques/README.md).

## I

**Indexing**: The offline process of preparing documents for search: loading, chunking, embedding, and storing. See [01](../01-rag-fundamentals/README.md).

**Inverted index**: A data structure that maps each term to the list of documents containing it. It is the core of keyword search engines. See [07](../07-information-retrieval/README.md).

## K

**k-Nearest Neighbours (kNN)**: Finding the *k* vectors closest to a query vector. "Exact kNN" compares the query against every vector. See [06](../06-vector-databases/README.md).

## L

**Large Language Model (LLM)**: A neural network, typically a Transformer, trained on large amounts of text to predict the next token. It can generate text in response to a prompt.

## M

**Metadata**: Structured information attached to a chunk, such as source, author, date, or section title. It is used for filtering and citation. See [03](../03-data-ingestion-and-processing/README.md) and [06](../06-vector-databases/README.md).

**MRR (Mean Reciprocal Rank)**: An evaluation metric: the average, over queries, of $1/\text{rank}$ of the first relevant result. See [10](../10-rag-evaluation/README.md).

## N

**nDCG (normalized Discounted Cumulative Gain)**: A ranking metric that rewards placing highly relevant results near the top, normalized so that a perfect ranking scores 1. See [10](../10-rag-evaluation/README.md).

## P

**Parametric knowledge**: Knowledge stored in a model's weights during training. Contrast with **non-parametric knowledge**, which is held in an external store that can be retrieved at query time. The RAG paper by Lewis et al. (2020) frames RAG as combining the two. See [01](../01-rag-fundamentals/README.md).

**Precision@k**: The fraction of the top *k* retrieved items that are relevant. See [10](../10-rag-evaluation/README.md).

**Prompt**: The input text given to an LLM. In RAG it usually contains instructions, the retrieved context, and the user's question. See [09](../09-context-engineering-and-generation/README.md).

## Q

**Query**: The user's question or search request.

**Query transformation**: Rewriting, expanding, or decomposing a query before retrieval to improve results. See [08](../08-advanced-retrieval-techniques/README.md).

## R

**Recall@k**: The fraction of all relevant items that appear in the top *k* retrieved results. See [10](../10-rag-evaluation/README.md).

**Reciprocal Rank Fusion (RRF)**: A method for merging several ranked lists by summing $1/(c + \text{rank})$ for each item, where $c$ is a constant. See [08](../08-advanced-retrieval-techniques/README.md).

**Reranking**: A second-stage step that re-scores a small set of retrieved candidates with a more accurate (and slower) model. See [08](../08-advanced-retrieval-techniques/README.md).

**Retrieval-Augmented Generation (RAG)**: A technique in which relevant information is retrieved from an external source and provided to a language model as context before it generates an answer. See [01](../01-rag-fundamentals/README.md).

**Retriever**: The component of a RAG system that finds relevant chunks for a query. See [07](../07-information-retrieval/README.md).

## S

**Semantic search**: Search based on meaning rather than exact keyword matches, usually implemented with embeddings. See [07](../07-information-retrieval/README.md).

**Softmax**: A function that turns a list of real numbers into probabilities that are positive and sum to 1. See [02](../02-mathematical-foundations/README.md).

**Sparse retrieval**: Retrieval based on term-matching representations (for example TF-IDF or BM25), where most vector entries are zero. See [07](../07-information-retrieval/README.md).

## T

**TF-IDF (Term Frequency–Inverse Document Frequency)**: A weighting scheme that scores a term highly when it is frequent in a document but rare across the corpus. See [02](../02-mathematical-foundations/README.md).

**Token**: The unit of text a language model processes. Often a word or part of a word, depending on the tokenizer.

**Tokenizer**: The algorithm that splits text into tokens and maps them to integer IDs.

**Top-k**: The *k* highest-scoring results returned by a retriever. See [07](../07-information-retrieval/README.md).

## V

**Vector**: An ordered list of numbers, for example $(0.2, -1.3, 0.7)$. Embeddings are vectors. See [02](../02-mathematical-foundations/README.md).

**Vector database**: A system that stores vectors and supports efficient similarity search, usually along with metadata filtering and updates. See [06](../06-vector-databases/README.md).
