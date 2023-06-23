# Automatic Model Selection with Large Language Models for Reasoning

This repository contains code, prompts and data for the paper: [Automatic Model Selection with Large Language Models for Reasoning](https://arxiv.org/pdf/2305.14333.pdf).

<div align="center">
<img src="selection-model.png" alt="Automatic selection model" align=center />
</div>


## Setup

You need to firstly have an OpenAI API Key. As OpenAI has discountinued public access to Codex, you can apply for the [research access](https://openai.com/form/researcher-access-program) to Codex (code-davinci-002). You can also use other backbones such as ChatGPT and GPT-4.

Package requirement: ``pip install openai``

## Dataset

7 arithmatic datasets and 1 date understanding dataset used in our experiments are in the folder ``dataset``. You can also download these datasets online and convert them into the corresponding format.

## Running

Run experiments via ``sh scripts/{codex chatgpt gpt4}/run_{dataset}.sh`` for greedy decoding. Run experiments via ``sh scripts/{codex chatgpt gpt4}/run_gsm8k_sc.sh`` for self-consistency.

- ``-sc_num``: It represents sampled paths. 1 indicates greedy decoding, while others indicate self-consistency paths.

Before running, please define EXEHOME, APIKEY accordingly in the script.

**Note**: OpenAI has [rate limitation]() for free trail users, which will affect the running time. You can update the account with payment methods.

## Evaluating

After running experiments, you can use ``sh evaluate_{math date}.sh`` to evaluate the results.

Before running, please define INPUTPATH in the script.

## Question

Thanks for your attention! Feel free to contact xu.zhao@u.nus.edu if you have any questions.

## Citation

```bibtex
@misc{zhao2023automatic,
      title={Automatic Model Selection with Large Language Models for Reasoning}, 
      author={Xu Zhao and Yuxi Xie and Kenji Kawaguchi and Junxian He and Qizhe Xie},
      year={2023},
      eprint={2305.14333},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
