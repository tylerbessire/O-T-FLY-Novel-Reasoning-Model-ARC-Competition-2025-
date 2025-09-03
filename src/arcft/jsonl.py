from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping, Any
import orjson


def write_jsonl(path: str | Path, records: Iterable[Mapping[str, Any]]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("wb") as f:
        for rec in records:
            f.write(orjson.dumps(rec))
            f.write(b"\n")

