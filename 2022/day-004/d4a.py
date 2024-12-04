from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 4
PART = "a"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

count = 0

parsed = [i for i in data.strip().split("\n")]
pairs = [j.split(",") for j in parsed]
ranges = [(tuple(k[0].split("-")), tuple(k[1].split("-"))) for k in pairs]
sets = [(set(range(int(l[0][0]), int(l[0][1])+1)), set(
    range(int(l[1][0]), int(l[1][1])+1))) for l in ranges]

for s in sets:
    print(s)
    if s[0].issubset(s[1]) or s[1].issubset(s[0]):
        print("######: ISSUBSET")
        count += 1

answer = count
print(answer)

####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
