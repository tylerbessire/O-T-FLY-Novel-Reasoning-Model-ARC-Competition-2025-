from __future__ import annotations

import json
import random
from pathlib import Path
from typing import List, Tuple

import typer

from arcft.dataset import load_json, iter_training_examples
from arcft.augment import TRANSFORMS, augment_pair
from arcft.jsonl import write_jsonl
from arcft.prompts import SYSTEM_MESSAGE_META, build_user_prompt_meta


app = typer.Typer(add_completion=False, help="Create augmented ARC SFT JSONL via geometric and color transforms.")


@app.command()
def main(
    train_challenges: Path = typer.Option(..., exists=True, readable=True),
    train_solutions: Path = typer.Option(..., exists=True, readable=True),
    out: Path = typer.Option(..., help="Output JSONL"),
    per_example: int = typer.Option(2, help="Augmented samples per original test example"),
    permute_colors: bool = typer.Option(True, help="Randomly permute non-zero colors"),
    seed: int = typer.Option(0, help="RNG seed for reproducibility"),
):
    random.seed(seed)
    tc = load_json(train_challenges)
    ts = load_json(train_solutions)

    # Pre-enumerate transforms
    ops_names = [name for name, _ in TRANSFORMS]

    records = []
    for tid, train_pairs, test_in, test_out in iter_training_examples(tc, ts):
        for _ in range(per_example):
            k = random.randint(1, min(3, len(ops_names)))
            ops = random.sample(ops_names, k=k)
            aug_train = [augment_pair(i, o, ops, permute_colors) for (i, o) in train_pairs]
            aug_test_in, aug_test_out = augment_pair(test_in, test_out, ops, permute_colors)

            user = build_user_prompt_meta(f"{tid}|aug:{'+'.join(ops)}", aug_train, aug_test_in)
            rec = {
                "messages": [
                    {"role": "system", "content": SYSTEM_MESSAGE_META},
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": json.dumps(aug_test_out)},
                ]
            }
            records.append(rec)

    write_jsonl(out, records)
    typer.echo(f"Wrote {len(records)} augmented examples to {out}")


if __name__ == "__main__":
    app()

