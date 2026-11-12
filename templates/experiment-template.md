<!--
EXPERIMENT TEMPLATE: how to use
1. Save next to the experiment code, e.g. <module>/code/<experiment-name>/EXPERIMENT.md
   or for paper reproductions: 14-research-and-paper-reproduction/<experiment-name>/EXPERIMENT.md
2. Fill in every section before reporting results. Someone else must be able to rerun this.
3. Report the results you actually obtained, including negative or inconclusive ones.
4. Delete this comment block.
-->

# Experiment: <Short Descriptive Title>

> **Author:** <GitHub username> · **Date:** <YYYY-MM-DD> · **Status:** <Planned | Running | Complete>

## Question

<The single question this experiment answers. Example: "Does adding a cross-encoder reranker improve Recall@5 over dense retrieval alone on dataset X?">

## Hypothesis

<What you expect, and why.>

## Setup

### Data

| Field | Value |
|---|---|
| Dataset | <Name, version, link> |
| License | <Dataset license> |
| Subset / size | <e.g. 500 queries, 10,000 passages> |
| Preprocessing | <Steps applied> |

### System Configuration

| Component | Baseline | Variant |
|---|---|---|
| Chunking | <...> | <...> |
| Embedding model | <name + version> | <...> |
| Index | <...> | <...> |
| Retriever / top-k | <...> | <...> |
| Reranker | <None> | <...> |
| LLM (if any) | <name + version> | <...> |

Change **one** variable at a time relative to the baseline, unless the question explicitly requires otherwise.

### Environment

| Field | Value |
|---|---|
| Python | <version> |
| Key packages | <see requirements.txt> |
| Hardware | <CPU/GPU, RAM> |
| Random seed(s) | <...> |

## Metrics

<Which metrics, and why they answer the question. Link to definitions in [module 10](../10-rag-evaluation/README.md).>

## How to Reproduce

```bash
pip install -r requirements.txt
python run_experiment.py --config config.yaml
```

## Results

| System | <Metric 1> | <Metric 2> | Latency (p50) |
|---|---|---|---|
| Baseline | <...> | <...> | <...> |
| Variant | <...> | <...> | <...> |

<If you ran multiple seeds, report the mean and spread. State the number of runs.>

## Analysis

<What the results show, and what they do not show. Was the difference larger than run-to-run variation?>

## Threats to Validity

- <Small sample size, dataset contamination, a single domain, a single model, etc.>

## Conclusion

<Answer the question in one or two sentences. "Inconclusive" is a valid answer.>

## Related

- Paper(s): <links>
- Module(s): <links>
