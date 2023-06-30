# Automatic Model Selection with Large Language Models for Reasoning

![Automatic selection model](selection-model.png)

This repository contains code, prompts and dataset for the paper: [Automatic Model Selection with Large Language Models for Reasoning](https://arxiv.org/pdf/2305.14333.pdf). We propose to perform model selection to combine two distinct methods, CoT and PAL. The proposed algorithm is illusrated in the above figure.

## News

* 🔥 We achieved the new SOTA results on GSM8K, with accuracy of 96.8% using GPT-4 and Self-Concsistency (K=15).
* 📣 We released the code and data.

## Setup

To beigin with, you need to have an OpenAI [API Key](https://platform.openai.com/account/api-keys). As OpenAI has discountinued public access to Codex, you can apply for [research access](https://openai.com/form/researcher-access-program) to Codex (code-davinci-002). Alternatively, you may opt to use other backbones like ChatGPT and GPT-4.

**Dataset**: Our experiments use seven arithmetic datasets and one date understanding dataset, all of which are located in the `dataset` folder. You may also download these datasets from their respective online sources and format them accordingly.

**Package requirement:** ``pip install openai``

## Running

You can run the code using the following command. We provide an example here that conducts experiments on the arithmetic dataset.

```
python src/selection_math.py --start [start index] --end [end index] --dataset [dataset name] --backbone [ChatGPT or GPT-4] --cot_temperature [0 for greedy decoding, 0.5 for SC] --pal_temperature [0 for greedy decoding, 0.8 for SC] --sc_num [1 for greedy decoding. Others indicate SC samples.] --output_dir [output dir name] --key [OpenAI API Key]
```

Alternatively, you may utilize the script in the `scripts` directory:

* For greedy decoding: ``sh scripts/{codex chatgpt gpt4}/run_{dataset}.sh``
* For self-consistency: ``sh scripts/{codex chatgpt gpt4}/run_gsm8k_sc.sh``

**Note**: Please ensure that you define `EXEHOME` and `APIKEY` in the script before execution.

OpenAI has [rate limits](https://platform.openai.com/docs/guides/rate-limits) for free trail users, which will affect the execution time. To circumvent this, you can upgrade your account with payment methods.

## Evaluating

After running experiments, you can use the following command to evaluate the results:

``sh evaluate_{math date}.sh``

Please ensure that `INPUTPATH` is defined in the script prior to execution.

## Inquiries

Thank you for your interest! Should you have any questions, please reach out to [xu.zhao@u.nus.edu](mailto:xu.zhao@u.nus.edu).

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
