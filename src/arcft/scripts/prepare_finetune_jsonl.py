from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple

import typer

from arcft.dataset import Grid, load_json, iter_training_examples
from arcft.jsonl import write_jsonl
from arcft.prompts import SYSTEM_MESSAGE, SYSTEM_MESSAGE_META, build_user_prompt, build_user_prompt_meta


app = typer.Typer(add_completion=False, help="Prepare OpenAI chat fine-tune JSONL from ARC training split.")


@app.command()
def main(
    train_challenges: Path = typer.Option(..., exists=True, readable=True, help="arc-agi_training_challenges.json"),
    train_solutions: Path = typer.Option(..., exists=True, readable=True, help="arc-agi_training_solutions.json"),
    out: Path = typer.Option(..., help="Output JSONL path"),
    limit: int = typer.Option(0, help="Optional cap on number of examples (0 = all)"),
    mode: str = typer.Option("plain", help="Prompting mode: plain | meta"),
):
    tc = load_json(train_challenges)
    ts = load_json(train_solutions)

    records = []
    count = 0
    for tid, train_pairs, test_in, test_out in iter_training_examples(tc, ts):
        if mode == "meta":
            sys_msg = SYSTEM_MESSAGE_META
            user = build_user_prompt_meta(tid, train_pairs, test_in)
        else:
            sys_msg = SYSTEM_MESSAGE
            user = build_user_prompt(tid, train_pairs, test_in)
        # Prepare a minimal chat example with strict output target
        rec = {
            "messages": [
                {"role": "system", "content": sys_msg},
                {"role": "user", "content": user},
                {"role": "assistant", "content": json.dumps(test_out)},
            ]
        }
        records.append(rec)
        count += 1
        if limit and count >= limit:
            break

    write_jsonl(out, records)
    typer.echo(f"Wrote {count} examples to {out}")


if __name__ == "__main__":
    app()
