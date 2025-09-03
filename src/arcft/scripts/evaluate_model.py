from __future__ import annotations

import json
import os
from dataclasses import dataclass
import re
from typing import List, Tuple

import typer
from tqdm import tqdm

from openai import OpenAI
from dotenv import load_dotenv

from arcft.dataset import load_json, iter_eval_examples, grids_equal, Grid
from arcft.prompts import SYSTEM_MESSAGE, SYSTEM_MESSAGE_META, build_user_prompt, build_user_prompt_meta


app = typer.Typer(add_completion=False, help="Evaluate a chat model on ARC evaluation split")


@dataclass
class Stats:
    total: int = 0
    correct: int = 0

    @property
    def acc(self) -> float:
        return (self.correct / self.total) if self.total else 0.0


def _looks_like_grid(obj) -> bool:
    if not isinstance(obj, list) or not obj:
        return False
    if not all(isinstance(r, list) and r for r in obj):
        return False
    # Rows must be equal length
    w = len(obj[0])
    if any(len(r) != w for r in obj):
        return False
    # Elements must be ints
    try:
        for r in obj:
            for v in r:
                int(v)
    except Exception:
        return False
    return True


def parse_grid(text: str) -> Grid | None:
    try:
        obj = json.loads(text)
    except Exception:
        # Try to extract first JSON array-of-arrays from text
        # Simple heuristic: find candidate substrings that start with '[' and end with ']'
        candidates = re.findall(r"\[.*?\]", text, flags=re.DOTALL)
        for cand in candidates:
            try:
                obj = json.loads(cand)
            except Exception:
                continue
            if _looks_like_grid(obj):
                return [[int(v) for v in row] for row in obj]
        return None
    if not _looks_like_grid(obj):
        return None
    return [[int(v) for v in row] for row in obj]


@app.command()
def main(
    model: str = typer.Option(..., help="Base or fine-tuned model id"),
    challenges: str = typer.Option(..., help="arc-agi_evaluation_challenges.json"),
    solutions: str = typer.Option(..., help="arc-agi_evaluation_solutions.json"),
    limit: int = typer.Option(50, help="Max examples to evaluate (0 = all)"),
    temperature: float = typer.Option(0.0, help="Sampling temperature"),
    timeout: int = typer.Option(60, help="Request timeout seconds"),
    samples: int = typer.Option(1, help="Number of samples per item; majority vote"),
    mode: str = typer.Option("plain", help="Prompting mode: plain | meta"),
):
    load_dotenv()
    client = OpenAI()

    eval_ch = load_json(challenges)
    eval_sol = load_json(solutions)

    stats = Stats()

    examples = list(iter_eval_examples(eval_ch, eval_sol))
    if limit and limit > 0:
        examples = examples[:limit]

    for tid, train_pairs, test_in, test_out in tqdm(examples, desc="Evaluating"):
        if mode == "meta":
            sys_msg = SYSTEM_MESSAGE_META
            user = build_user_prompt_meta(tid, train_pairs, test_in)
        else:
            sys_msg = SYSTEM_MESSAGE
            user = build_user_prompt(tid, train_pairs, test_in)
        texts: list[str] = []
        for _ in range(max(1, samples)):
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": user},
                    ],
                    temperature=temperature,
                    timeout=timeout,
                )
                texts.append(resp.choices[0].message.content or "")
            except Exception:
                texts.append("")

        # Parse and majority vote by serialized JSON
        parsed: list[Grid] = [g for g in (parse_grid(t) for t in texts) if g is not None]
        if parsed:
            from collections import Counter
            def key(g: Grid) -> str:
                return json.dumps(g, separators=(",", ":"))
            c = Counter(key(g) for g in parsed)
            best_key, _ = c.most_common(1)[0]
            pred = json.loads(best_key)
        else:
            pred = None

        stats.total += 1
        if pred is not None and grids_equal(pred, test_out):
            stats.correct += 1

    typer.echo(f"Total: {stats.total}  Correct: {stats.correct}  Acc: {stats.acc:.3f}")


if __name__ == "__main__":
    app()
