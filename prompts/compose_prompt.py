import sys
from examples import icl_examples
from instructions import task_instructions
from templates import prompt_templates

def compose_prompt(strategy: str, task_type: str, examples_origin: str,
                   question_or_context: str, answer_or_step: str = None) -> str:
    """Composes a prompt for a current question/context and (optionally) answer
       or step, given a prompting strategy, task type and dataset.

    Args:
        strategy: The desidired prompting strategy. Options are 'cot',
            'cot_plus', 'explicit', 'implicit'.
        task type: The type of task to solve. Options are 'label_ans',
            'label_step', 'edit', 'solve'.
        dataset: Name of the dataset. We use 'gsm8k', 'asdiv', 'aqua', 'prm800k'.
        question_or_context: The current dataset question or context (i.e., the
            question concatenated with a partial answer).
        answer_or_step: The answer to the current question, or the next
            reasoning step for the current context.
                   
    Returns:
        The complete prompt for the given arguments, ready to pass to an LLM.
    """
    strategy_ops = ['cot', 'cot_plus', 'explicit', 'implicit']
    task_ops = ['label_ans', 'label_step', 'edit', 'solve']
    origins = ['gsm8k', 'asdiv', 'aqua', 'prm800k']
    assert strategy in strategy_ops, "strategy must be one of 'cot', 'cot_plus', 'explicit', 'implicit'."
    assert task_type in task_ops, "task_type must be one of 'label_ans', 'label_step', 'edit', 'solve'."
    assert examples_origin in origins, "examples_origin must be one of 'gsm8k', 'asdiv', 'aqua', 'prm800k'."
    if task_type in ['label_ans', 'label_step', 'edit']:
        assert answer_or_step is not None, "answer_or_step must be specified for this task."

    examples_id = f"{examples_origin}_{strategy}_examples"
    task_id = "solve_cot" if (
                               task_type == "solve" and strategy == "cot"
                             ) else task_type
    examples_with_instruction = "{}\n\n\n\n{}".format(
                                                icl_examples[examples_id],
                                                task_instructions[task_id]
                                                )
    if examples_origin != "prm800k" and "label" not in task_type:
        examples_with_instruction += " Express the final numerical answer as an integer or floating point number."
    prompt = prompt_templates[f"{task_id}_template"].format(
                                                examples_with_instruction,
                                                question_or_context,
                                                answer_or_step)
    return prompt


if __name__ == "__main__":
    print(compose_prompt(*sys.argv[1:]))






