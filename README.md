ARC Fine-Tuning Toolkit (arcft)

This repo contains utilities to prepare supervised fine-tuning (SFT) data and evaluate chat models on the ARC-AGI tasks using the JSON files included here.

What’s included
- Data loader for ARC JSON files
- Prompt builder that asks for only the final grid as JSON
- JSONL preparation CLI for OpenAI fine-tuning
- Evaluation CLI to compute accuracy vs. ground truth
- Augmentation CLI to synthesize transformed tasks (rot/flip/color)

Quick start
1) Create a virtual env and install:
   - python -m venv .venv && source .venv/bin/activate
   - pip install -e .

2) Prepare SFT data from training split:
   - arcft-prep --train-challenges arc-agi_training_challenges.json \
                --train-solutions arc-agi_training_solutions.json \
                --out data/ft/train.jsonl

   Meta-learning flavored prompts:
   - arcft-prep --train-challenges arc-agi_training_challenges.json \
                --train-solutions arc-agi_training_solutions.json \
                --mode meta \
                --out data/ft/train_meta.jsonl

3) (Optional) Create a fine-tuning job with OpenAI:
   - See scripts in arcft/scripts/create_finetune_job.py or use the OpenAI CLI.

4) Evaluate a base or fine-tuned model on evaluation split:
   - export OPENAI_API_KEY=... 
   - arcft-eval --model YOUR_MODEL_ID \
                --challenges arc-agi_evaluation_challenges.json \
                --solutions arc-agi_evaluation_solutions.json \
                --mode meta \
                --samples 3 \
                --temperature 0.2 \
                --limit 50

Notes
- The prompts constrain outputs to be strictly JSON arrays of ints (no prose), which simplifies parsing and scoring.
- The evaluator tolerates extra text by extracting the first valid JSON grid if present, so you can use meta prompts while still scoring strictly on the final grid.
- To aim beyond simple SFT, consider a tool-augmented solver that proposes and verifies transformations; SFT can still help the model emit better hypotheses.

Augmenting data
- Geometric/color transforms help induce generalization:
  - arcft-augment --train-challenges arc-agi_training_challenges.json \
                  --train-solutions arc-agi_training_solutions.json \
                  --out data/ft/train_aug.jsonl --per-example 3
