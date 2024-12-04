import string
import time
from enum import Enum, IntEnum, auto

from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 3
PART = "b"


c = Console()
start_time = time.perf_counter()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

parsed = [i for i in data.strip().split("\n")]
groups = [parsed[j:j + 3] for j in range(0, len(parsed), 3)]
badges = [next(iter(set(k[0]) & set(k[1]) & set(k[2]))) for k in groups]
priorities = [string.ascii_letters.index(k) + 1 for k in badges]

answer = sum(priorities)
print(answer)

####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
