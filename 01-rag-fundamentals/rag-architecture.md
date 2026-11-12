# RAG Architecture

> **Status:** Planned (Phase 2) · **Level:** Beginner
>
> This page is a placeholder. It lists the planned scope so contributors and learners know what is coming. The lesson content has not been written yet.

## Planned Learning Objectives

After this lesson, you will be able to:

- Draw the architecture of a basic RAG system.
- Name each component and describe its responsibility: loader, chunker, embedding model, vector index, retriever, prompt builder, and generator.
- Distinguish the offline indexing pipeline from the online query pipeline.
- Recognize where advanced techniques (reranking, query transformation, hybrid search) plug in.

## Planned Outline

1. The two pipelines: indexing (offline) and querying (online).
2. Component-by-component tour, with a link to the module that covers each component in depth.
3. Data flow: what goes in and out of each component.
4. "Naive", "advanced", and "modular" RAG as a way to organize techniques (following Gao et al., 2023).
5. Extension points for later modules.
6. Summary and exercises.

## Planned References

- Lewis, P. et al. (2020). [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- Gao, Y. et al. (2023). *Retrieval-Augmented Generation for Large Language Models: A Survey.* [arXiv:2312.10997](https://arxiv.org/abs/2312.10997)

---

**Previous:** [RAG vs Fine-tuning](rag-vs-fine-tuning.md) · [Back to module 01](README.md) · **Next:** [The Complete RAG Workflow](rag-workflow.md)
