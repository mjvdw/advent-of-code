# Couldn't figure this one out for the life of me.
# Had the right idea, but just no idea how to implement it.
# Took a hint from Martyn (https://gitlab.com/martynsmith/advent-of-code-2022/blob/main/day7.py)
# to use pathlib, but I've never heard of it before.
# Decided to get on with my life and just see what Martyn did.
# This is essentially Martyn's answer, but I wrote it out
# to understand, rather than just copy-paste, and to make myself
# feel better about it!


from pathlib import Path
from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 7
PART = "a"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

total_size = 0
parsed = data.strip().split("\n")
cwd = Path("/")
directories = {cwd}
files = {}

for line in parsed:
    if line.startswith("$ cd "):
        cwd = (cwd / line[5:]).resolve()
        directories.add(cwd)
    elif line.startswith("$ ls"):
        pass
    else:
        size, filename = line.split(" ")
        if size == 'dir':
            pass
        else:
            size = int(size)
            files[cwd / filename] = size

answer = 0
for directory in directories:
    total = 0
    for file, size in files.items():
        if str(file).startswith(str(directory)):
            total += size
    if total <= 1e5:
        answer += total


####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
