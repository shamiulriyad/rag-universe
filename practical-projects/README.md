# Practical Projects

> **Status:** Planned (Phase 7; P1 may be delivered earlier alongside Phase 2)

Projects combine several modules into a complete, working system. Each project lists the modules it depends on, the skills it practises, and how to know you have succeeded.

## How Projects Work

- Each project lives in its own folder: `practical-projects/pN-project-name/`.
- Every project includes a `README.md` (goal, requirements, steps, evaluation), pinned dependencies, and a reference solution.
- Every project defines **success criteria** that can be measured, for example "Recall@5 ≥ the baseline on the provided test set", so you can tell whether you are done.
- Try the project yourself before reading the reference solution.

## Project List

| # | Project | Level | Requires modules | Status |
|---|---|---|---|---|
| P1 | **Minimal RAG from scratch**: a complete pipeline in plain Python and NumPy, no frameworks | Beginner | 01–05 | Planned |
| P2 | **Document Q&A over PDFs**: ingestion, chunking, dense retrieval, and cited answers | Intermediate | 03–07, 09 | Planned |
| P3 | **Hybrid search assistant with reranking**: BM25 + dense + RRF + cross-encoder, measured against the baseline | Advanced | 07, 08, 10 | Planned |
| P4 | **RAG with an evaluation harness**: a labelled test set, retrieval and generation metrics, regression reports | Intermediate | 09, 10 | Planned |
| P5 | **Production-style RAG service**: API, incremental indexing, monitoring, access control | Advanced | 10, 12, 13 | Planned |
| P6 | **Graph RAG mini-project**: entity extraction, graph construction, and graph-based retrieval on a small corpus | Advanced | 10, 11 | Planned |

## Project README Template

New projects follow this outline:

1. Goal
2. What you will practise (with links to modules)
3. Requirements (hardware, dependencies, API keys if any)
4. Dataset (source, license, size)
5. Step-by-step milestones
6. Success criteria
7. Stretch goals
8. Reference solution notes

## Navigation

[Learning Path](../docs/learning-path.md#checkpoint-projects) · [ROADMAP](../ROADMAP.md#phase-7--research-and-projects)
