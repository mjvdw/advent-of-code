from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 6
PART = "a"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

answer = 0
parsed = [*data]

for i in range(3, len(parsed)+1):
    unique = set(parsed[i-4:i])
    if len(unique) == 4:
        answer = i
        break


####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
