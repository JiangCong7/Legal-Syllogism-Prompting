## Legal Syllogism Prompting
This is code repository for the paper [Legal Syllogism Prompting: Teaching Large Language Models for Legal Judgment Prediction](https://arxiv.org/abs/2307.08321) See also at (https://dl.acm.org/doi/10.1145/3594536.3595170). 

We propose legal syllogism prompting (LoT), a simple prompting method to teach large language models (LLMs) for legal judgment prediction. LoT teaches only that in the legal syllogism the major premise is law, the minor premise is the fact, and the conclusion is judgment. Then the models can produce a syllogism reasoning of the case and give the judgment without any learning, fine-tuning, or examples. On CAIL2018, a Chinese criminal case dataset, we performed zero-shot judgment prediction experiments with GPT-3 models. Our results show that LLMs with LoT achieve better performance than the baseline and chain of thought prompting, the state-of-art prompting method.

## Running the code

First you need to specify your OPENAI key in cail_test.py
```
openaikey = [YOUR_KEY]
```

Considering the large size of CAIL2018 dataset. We provide a random sampled test dataset of CAIL2018 in this repo. You can get the full dataset from CAIL2018(https://github.com/thunlp/CAIL).

- baseline
```
set full_prompt = baseline in cail_test.py
python cail_test.py 
...
```
- cot
```
set full_prompt = cot in cail_test.py
python cail_test.py
...
```
-  legal syllogism
```
set full_prompt = syllogism in cail_test.py
python cail_test.py
...
```
## Working in progress


## Cite our work
```
@inproceedings{jiang2023legal,
  title={Legal syllogism prompting: Teaching large language models for legal judgment prediction},
  author={Jiang, Cong and Yang, Xiaolei},
  booktitle={Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law},
  pages={417--421},
  year={2023}
}
```
