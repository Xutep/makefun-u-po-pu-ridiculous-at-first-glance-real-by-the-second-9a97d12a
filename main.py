"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre-but-sellable startup idea to
/output/entry.txt. The sentence names the odd thing being sold (goat
herds rented out as lawn mowers), who pays for it (tech campuses),
and the money ($800 a month per herd).

Deterministic, standard library only: the same sentence is written
on every run.
"""

import os

SENTENCE = (
    "We rent herds of goats to mow corporate lawns: tech campuses pay "
    "$800 a month per herd, the goats eat the grass, fertilize it, and "
    "staff get a lunchtime petting zoo."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError(
            "sentence must be 1-200 characters, got %d" % len(SENTENCE)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
