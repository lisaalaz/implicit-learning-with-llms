# No Need for Explanations: LLMs can *implicitly* learn from mistakes in-context
This repository contains all the prompts used in the paper <a href="https://arxiv.org/abs/2502.08550" target="_blank">No Need for Explanations: LLMs can *implicitly* learn from mistakes in-context</a>.

---

Run `create_prompt.py` to create a new prompt with the following arguments (in this order): 
- the desired prompting strategy (`cot`, `cot_plus`, `explicit`, or `implicit`), 
- a task type (`label_ans`, `label_step`, `edit`, `solve`), 
- a dataset of origin for the few-shot examples (`gsm8k`, `asdiv`, `aqua`, `prm800k`), 
- a math reasoning question
- a pre-generated step-by-step answer (optional, not needed for the `solve` task type).

For example, to create and view a prompt for solving a given question using few-shot examples from the GSM8K dataset and the implicit learning prompting strategy, run:

```bash
>> python3 compose_prompt.py implicit solve gsm8k $QUESTION
```

---

## Citation

If you use this repository, please cite our work:

````bibtex
@inproceedings{alazraki-etal-2025-need,
    title = "No Need for Explanations: {LLM}s can implicitly learn from mistakes in-context",
    author = "Alazraki, Lisa and Mozes, Maximilian and Campos, Jon Ander and Yi-Chern, Tan and Rei, Marek and Bartolo, Max",
    editor = "Christodoulopoulos, Christos and Chakraborty, Tanmoy and Rose, Carolyn and Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.1686/",
    doi = "10.18653/v1/2025.emnlp-main.1686",
    pages = "33191--33215",
    ISBN = "979-8-89176-332-6",
}
````
