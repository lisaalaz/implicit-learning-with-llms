# LLMs can *implicitly* learn from mistakes in-context
This repository contains all the prompts used in the paper <a href="" target="_blank">LLMs can *implicitly* learn from mistakes in-context</a>.

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
@misc{alazrakietal2025,
      title={LLMs can implicitly learn from mistakes in-context}, 
      author={Lisa Alazraki and Maximilian Mozes and Jon Ander Campos and Yi Chern Tan and Marek Rei and Max Bartolo},
      year={2025},
      eprint={},
      archivePrefix={},
      primaryClass={},
      url={}, 
}
````