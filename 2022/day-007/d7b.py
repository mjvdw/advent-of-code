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
PART = "b"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

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

current_used = 0
for directory in directories:
    total = 0
    for file, size in files.items():
        if str(file).startswith(str(directory)):
            total += size

    if directory == Path("/"):
        current_used = total

total_disk_space = 70000000
max_used = total_disk_space - 30000000
need_to_delete = current_used - max_used

for dir in directories:
    # Calculate the size of each directory.
    total = 0
    for file, size in files.items():
        if str(file).startswith(str(dir)):
            total += size

    # total_disk_space records the smallest sized directory so far.
    # The second check is to see whether the current directory being
    # considered is bigger or smaller. If it's bigger, the condition
    # fails and it moves on. The last directory to pass this
    # condition will be the smallest directory that is also
    # larger than (or equal to) the amount of data that needs to be
    # deleted.
    if total >= need_to_delete and total < total_disk_space:
        total_disk_space = total


answer = total_disk_space
print(answer)

####################################################################################
c.rule("Finished")

# submit(year=YEAR, day=DAY, part=PART, answer=answer)
