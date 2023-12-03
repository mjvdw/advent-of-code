from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 4
PART = "b"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

parsed = [i for i in data.strip().split("\n")]
pairs = [j.split(",") for j in parsed]
ranges = [(tuple(k[0].split("-")), tuple(k[1].split("-"))) for k in pairs]
sets = [(set(range(int(l[0][0]), int(l[0][1])+1)), set(
    range(int(l[1][0]), int(l[1][1])+1))) for l in ranges]
overlap = [m[0].intersection(m[1])
           for m in sets if m[0].intersection(m[1]) != set()]

answer = len(overlap)

####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
