from __future__ import annotations

import random
from typing import List, Tuple, Dict, Any

Grid = List[List[int]]


def rotate90(g: Grid) -> Grid:
    return [list(row) for row in zip(*g[::-1])]


def rotate180(g: Grid) -> Grid:
    return [row[::-1] for row in g[::-1]]


def rotate270(g: Grid) -> Grid:
    return [list(row) for row in zip(*g)][::-1]


def flip_h(g: Grid) -> Grid:
    return [row[::-1] for row in g]


def flip_v(g: Grid) -> Grid:
    return g[::-1]


def color_permute(g: Grid) -> Grid:
    # Preserve 0 as background; permute other colors present.
    colors = sorted({v for row in g for v in row if v != 0})
    mapping = {c: c for c in colors}
    if colors:
        perm = colors[:]
        random.shuffle(perm)
        mapping.update({c: p for c, p in zip(colors, perm)})
    return [[0 if v == 0 else mapping.get(v, v) for v in row] for row in g]


TRANSFORMS = [
    ("rot90", rotate90),
    ("rot180", rotate180),
    ("rot270", rotate270),
    ("flip_h", flip_h),
    ("flip_v", flip_v),
]


def apply_combo(g: Grid, ops: List[str], permute_colors: bool) -> Grid:
    out = g
    for op in ops:
        fn = dict(TRANSFORMS)[op]
        out = fn(out)
    if permute_colors:
        out = color_permute(out)
    return out


def augment_pair(inp: Grid, out: Grid, ops: List[str], permute_colors: bool) -> Tuple[Grid, Grid]:
    return apply_combo(inp, ops, permute_colors), apply_combo(out, ops, permute_colors)

