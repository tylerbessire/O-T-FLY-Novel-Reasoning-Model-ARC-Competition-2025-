from __future__ import annotations

from pathlib import Path
import typer
from openai import OpenAI
from dotenv import load_dotenv


app = typer.Typer(add_completion=False, help="Create an OpenAI fine-tuning job from a JSONL file")


@app.command()
def main(
    jsonl_path: Path = typer.Option(..., exists=True, readable=True, help="Training JSONL (chat format)"),
    base_model: str = typer.Option(..., help="Base model to finetune"),
    suffix: str = typer.Option("arcft", help="Suffix for the fine-tuned model name"),
    n_epochs: int = typer.Option(3, help="Number of epochs"),
):
    load_dotenv()
    client = OpenAI()

    file = client.files.create(
        file=open(jsonl_path, "rb"),
        purpose="fine-tune"
    )
    typer.echo(f"Uploaded file: {file.id}")

    job = client.fine_tuning.jobs.create(
        training_file=file.id,
        model=base_model,
        suffix=suffix,
        hyperparameters={"n_epochs": n_epochs},
    )
    typer.echo(f"Created job: {job.id}  status={job.status}")


if __name__ == "__main__":
    app()
