# Datasets

Public datasets and benchmarks used for retrieval and RAG experiments. Each entry links to the official dataset page and the paper that introduced it. Links were checked on 2026-11-12.

**License note:** licenses and terms of use differ between datasets, and some restrict commercial use. Always check the official page before using a dataset, and record its license in your experiment report (see the [experiment template](../templates/experiment-template.md)).

## Question Answering

| Dataset | Description | Paper | Official page |
|---|---|---|---|
| SQuAD | Reading-comprehension questions on Wikipedia paragraphs | Rajpurkar et al. (2016), [arXiv:1606.05250](https://arxiv.org/abs/1606.05250) | [rajpurkar.github.io/SQuAD-explorer](https://rajpurkar.github.io/SQuAD-explorer/) |
| TriviaQA | Trivia questions with evidence documents | Joshi et al. (2017), [arXiv:1705.03551](https://arxiv.org/abs/1705.03551) | [nlp.cs.washington.edu/triviaqa](https://nlp.cs.washington.edu/triviaqa/) |
| Natural Questions | Real Google search queries answered from Wikipedia | Kwiatkowski et al. (2019), TACL | [ai.google.com/research/NaturalQuestions](https://ai.google.com/research/NaturalQuestions) |
| HotpotQA | Multi-hop questions requiring reasoning over several documents | Yang et al. (2018), [arXiv:1809.09600](https://arxiv.org/abs/1809.09600) | [hotpotqa.github.io](https://hotpotqa.github.io/) |

## Passage Retrieval

| Dataset | Description | Paper | Official page |
|---|---|---|---|
| MS MARCO | Large-scale passage and document ranking from Bing queries | Bajaj et al. (2016), [arXiv:1611.09268](https://arxiv.org/abs/1611.09268) | [microsoft.github.io/msmarco](https://microsoft.github.io/msmarco/) |

## Fact Verification

| Dataset | Description | Paper | Official page |
|---|---|---|---|
| FEVER | Claims to verify against Wikipedia evidence | Thorne et al. (2018), [arXiv:1803.05355](https://arxiv.org/abs/1803.05355) | [fever.ai](https://fever.ai/) |

## Benchmark Suites

| Benchmark | Description | Paper | Official page |
|---|---|---|---|
| BEIR | Zero-shot IR evaluation across diverse domains | Thakur et al. (2021), [arXiv:2104.08663](https://arxiv.org/abs/2104.08663) | [github.com/beir-cellar/beir](https://github.com/beir-cellar/beir) |
| KILT | Knowledge-intensive tasks grounded in one Wikipedia snapshot | Petroni et al. (2020), [arXiv:2009.02252](https://arxiv.org/abs/2009.02252) | [github.com/facebookresearch/KILT](https://github.com/facebookresearch/KILT) |
| MTEB | Benchmark covering many embedding tasks, including retrieval | Muennighoff et al. (2022), [arXiv:2210.07316](https://arxiv.org/abs/2210.07316) | [github.com/embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) |

## Choosing a Dataset for Learning

- **Start small.** For lessons, a few hundred documents and a few dozen labelled questions are enough to show clear effects and still run on a laptop.
- **Match the task.** Use single-hop QA (SQuAD, Natural Questions) for basic retrieval, and HotpotQA for multi-hop retrieval.
- **Watch for contamination.** Popular benchmarks may appear in LLM training data, which can inflate generation scores.

---

**Other resources:** [Books](books.md) · [Courses](courses.md) · [Videos](videos.md) · [Tools and Frameworks](tools-and-frameworks.md)
