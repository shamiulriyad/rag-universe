# Prerequisites

This page lists what you need to know and install before each track. You do **not** need everything on day one. Each section says which track needs it.

## Table of Contents

- [Summary](#summary)
- [Programming](#programming)
- [Mathematics](#mathematics)
- [Machine Learning and NLP Concepts](#machine-learning-and-nlp-concepts)
- [Tools and Environment Setup](#tools-and-environment-setup)
- [Self-Check](#self-check)
- [Where to Learn Missing Prerequisites](#where-to-learn-missing-prerequisites)

## Summary

| Area | Beginner | Intermediate | Advanced |
|---|---|---|---|
| Python | Basics | Comfortable | Fluent, including packaging and testing |
| Math | High-school algebra | Linear algebra basics, basic probability | Comfortable reading equations in papers |
| ML / NLP | None | Tokens, embeddings, training vs inference | Transformers, fine-tuning concepts |
| LLM usage | None | Has called an LLM API or run a local model | Familiar with prompting techniques and their limits |
| Tools | Python, a code editor | Git, virtual environments, Jupyter | Docker, a cloud or server environment |

## Programming

**Beginner:**

- Variables, data types, `if` statements, loops.
- Functions and modules.
- Lists, dictionaries, and strings (splitting, joining, slicing).
- Reading and writing files.
- Installing packages with `pip`.

**Intermediate (adds):**

- Classes and dataclasses.
- Virtual environments.
- Basic NumPy: arrays, shapes, element-wise operations, `np.dot`.
- Calling an HTTP API and handling JSON.

**Advanced (adds):**

- Writing tests with `pytest`.
- Asynchronous code (`asyncio`) basics.
- Building a small web API (for example with FastAPI).
- Docker basics.

## Mathematics

You do **not** need to be a mathematician. [Module 02](../02-mathematical-foundations/README.md) teaches the math needed for RAG, step by step. It helps if you are comfortable with:

**Beginner:**

- Arithmetic with negative numbers and decimals.
- Squares and square roots.
- Reading summation notation: $\sum_{i=1}^{n} x_i$ means "add up $x_1$ through $x_n$".

**Intermediate (adds):**

- What a vector is (an ordered list of numbers) and what a matrix is (a table of numbers).
- Logarithms and exponentials ($\log$, $e^x$).
- Basic probability: what $P(A)$ and $P(A \mid B)$ mean.

**Advanced (adds):**

- Matrix multiplication and transposes.
- Expectation and variance.
- Reading notation in research papers.

## Machine Learning and NLP Concepts

**Beginner:** none required. Module 01 explains what you need.

**Intermediate:**

- **Token**: a unit of text (often a word piece) that a model processes.
- **Embedding**: a vector of numbers representing a piece of text.
- **Training vs inference**: learning model weights vs using a trained model.
- **LLM**: a model that generates text by predicting the next token.

These terms and more are defined in the [glossary](glossary.md).

**Advanced:**

- The Transformer architecture at a high level ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)).
- Encoder vs decoder models (for example BERT vs GPT-style models).
- The difference between pre-training, fine-tuning, and prompting.

## Tools and Environment Setup

**Required:**

1. **Python 3.10 or newer.** Check with:

   ```bash
   python --version
   ```

2. **A code editor**, such as VS Code or PyCharm.

3. **Git**, for cloning the repository:

   ```bash
   git clone <repository-url>
   cd rag-universe
   ```

4. **A virtual environment** for each project:

   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```

**Optional:**

- **Jupyter**, for interactive exploration.
- **An LLM API key or a local LLM runtime.** Lessons that need one say so explicitly. Fundamental lessons are designed to run without one.
- **Docker**, used in the production module.

**Hardware:** fundamentals run on any modern laptop. Some embedding and reranking lessons run faster with a GPU, but GPU-free options will be provided.

## Self-Check

Try these before starting. If you can answer them, you are ready for the beginner track.

1. Write a Python function that takes a list of strings and returns the longest one.
2. Given `d = {"a": 1, "b": 2}`, how do you loop over its keys and values?
3. What is $3 \times 4 + 2 \times 5$?
4. What is $\sqrt{9 + 16}$?

<details>
<summary>Answers</summary>

1. `def longest(xs): return max(xs, key=len)`
2. `for key, value in d.items(): ...`
3. $12 + 10 = 22$. This is exactly how a dot product is computed, as you will see in module 02.
4. $\sqrt{25} = 5$. This is the length of the vector $(3, 4)$.

</details>

## Where to Learn Missing Prerequisites

See [resources/courses.md](../resources/courses.md) and [resources/books.md](../resources/books.md) for verified learning resources on Python, linear algebra, and NLP.
