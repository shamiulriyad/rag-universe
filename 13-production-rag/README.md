# 13 — Production RAG

> **Status:** Planned (Phase 6) · **Level:** Advanced · **Estimated time:** 10–12 hours

## Overview

This module takes a RAG system from a notebook to a service that real users depend on. It covers serving, keeping the index up to date, monitoring quality over time, securing the system against prompt injection and data leakage, enforcing access control, and scaling.

## Why This Module Matters

Production adds problems that do not appear in prototypes. Documents change, users ask unexpected questions, retrieved content can contain malicious instructions, and users may only be allowed to see some documents. Each of these needs a deliberate design.

## Prerequisites

- [10 — RAG Evaluation](../10-rag-evaluation/README.md)
- [12 — RAG Optimization](../12-rag-optimization/README.md)
- Basic familiarity with web APIs and Docker (see [prerequisites](../docs/prerequisites.md)).

## Planned Lessons

| # | Lesson | Level | Status |
|---|---|---|---|
| 1 | Reference architecture for production RAG | Advanced | Planned |
| 2 | Serving RAG behind an API | Advanced | Planned |
| 3 | Incremental indexing and document updates | Advanced | Planned |
| 4 | Observability and monitoring | Advanced | Planned |
| 5 | Security: prompt injection and data leakage | Advanced | Planned |
| 6 | Access control and multi-tenancy | Advanced | Planned |
| 7 | Privacy and compliance considerations | Advanced | Planned |
| 8 | Scaling and deployment | Advanced | Planned |
| 9 | Continuous evaluation and regression testing | Advanced | Planned |

## Key References

- Greshake, K. et al. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.* [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)
- OWASP Top 10 for Large Language Model Applications: [genai.owasp.org](https://genai.owasp.org/)

## Navigation

**Previous:** [12 — RAG Optimization](../12-rag-optimization/README.md) · **Next:** [14 — Research and Paper Reproduction](../14-research-and-paper-reproduction/README.md)
