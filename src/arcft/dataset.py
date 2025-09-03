from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


TaskId = str
Grid = List[List[int]]


def load_json(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_training_examples(
    train_challenges: Dict[str, Any],
    train_solutions: Dict[str, Any],
) -> Iterable[Tuple[TaskId, List[Tuple[Grid, Grid]], Grid, Grid]]:
    """
    Yields per-test-item examples from the training split.

    For each task id, this emits one example per test item:
    (task_id, train_pairs, test_input, test_output)
    where train_pairs is a list of (input_grid, output_grid).
    """
    for tid, spec in train_challenges.items():
        trains = spec.get("train", [])
        tests = spec.get("test", [])
        gt_tests = train_solutions.get(tid, [])
        if len(tests) != len(gt_tests):
            # Skip malformed entries
            continue
        train_pairs: List[Tuple[Grid, Grid]] = [
            (ex["input"], ex["output"]) for ex in trains
        ]
        for test_ex, gt_out in zip(tests, gt_tests):
            yield tid, train_pairs, test_ex["input"], gt_out


def iter_eval_examples(
    eval_challenges: Dict[str, Any],
    eval_solutions: Dict[str, Any],
) -> Iterable[Tuple[TaskId, List[Tuple[Grid, Grid]], Grid, Grid]]:
    """
    Yields per-test-item examples from the evaluation split.
    Same shape as iter_training_examples.
    """
    for tid, spec in eval_challenges.items():
        trains = spec.get("train", [])
        tests = spec.get("test", [])
        gt_tests = eval_solutions.get(tid, [])
        if len(tests) != len(gt_tests):
            continue
        train_pairs: List[Tuple[Grid, Grid]] = [
            (ex["input"], ex["output"]) for ex in trains
        ]
        for test_ex, gt_out in zip(tests, gt_tests):
            yield tid, train_pairs, test_ex["input"], gt_out


def grids_equal(a: Grid, b: Grid) -> bool:
    if len(a) != len(b):
        return False
    return all(row_a == row_b for row_a, row_b in zip(a, b))

