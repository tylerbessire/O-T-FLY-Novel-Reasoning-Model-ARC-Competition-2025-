from __future__ import annotations

from typing import List, Tuple

Grid = List[List[int]]


SYSTEM_MESSAGE = (
    "You are an ARC-AGI grid transformer. Given training input/output "
    "pairs and one test input grid, you must output the test output grid "
    "as a JSON array of arrays of integers. Do not include any text or "
    "explanations. Output only the JSON array."
)

SYSTEM_MESSAGE_META = (
    "You are an ARC-AGI meta-reasoner. Infer abstract rules from training "
    "input/output pairs, hypothesize general transformations, then apply them "
    "to the test input. Think through hypotheses internally. Do not reveal any "
    "intermediate reasoning. Output only the final test output grid as a JSON "
    "array of arrays of integers."
)


def format_grid(g: Grid) -> str:
    # Compact JSON-ish formatting for the prompt; model returns JSON only.
    return "[" + ", ".join("[" + ", ".join(str(v) for v in row) + "]" for row in g) + "]"


def build_user_prompt(task_id: str, train_pairs: List[Tuple[Grid, Grid]], test_input: Grid) -> str:
    lines: List[str] = []
    lines.append(f"Task: {task_id}")
    lines.append("Training examples:")
    for i, (inp, out) in enumerate(train_pairs, 1):
        lines.append(f"- Example {i} input: {format_grid(inp)}")
        lines.append(f"- Example {i} output: {format_grid(out)}")
    lines.append("Test input:")
    lines.append(format_grid(test_input))
    lines.append("Return only the JSON array of the test output grid.")
    return "\n".join(lines)


def build_user_prompt_meta(task_id: str, train_pairs: List[Tuple[Grid, Grid]], test_input: Grid) -> str:
    lines: List[str] = []
    lines.append(f"Task: {task_id}")
    lines.append("Goal: infer a general rule from the training pairs that maps input→output, then apply it to the test input.")
    lines.append("Training pairs (input then output):")
    for i, (inp, out) in enumerate(train_pairs, 1):
        lines.append(f"- Input {i}: {format_grid(inp)}")
        lines.append(f"- Output {i}: {format_grid(out)}")
    lines.append("Test input:")
    lines.append(format_grid(test_input))
    lines.append("Think silently. Return only the JSON array of the test output grid.")
    return "\n".join(lines)
