from collections import Counter
from pathlib import Path
import os

# IN_FILE = os.path.join("AOC2023","inputs","202307.sample.txt")
IN_FILE = os.path.join("202307.in")

data_raw = Path(__file__).with_name(IN_FILE).read_text().splitlines()

print(
    sum(
        (rank0 + 1) * bid
        for rank0, (*_, bid) in enumerate(
            sorted(
                (
                    max(Counter(hand).values()) - len(set(hand)), *map("23456789TQKAJ".index, hand), int(str_bid),
                )
                for hand, str_bid in map(str.split, data_raw)
            )
        )
    )
)