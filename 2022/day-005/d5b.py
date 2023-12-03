from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 5
PART = "b"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

# PARSE STARTING POSITION
start_data, move_data = data.split("\n\n")
parsed_start = [i[1::2][0::2] for i in start_data.strip().split("\n")]
positions = []

for x in range(0, len(parsed_start)-1):
    positions.append(list())
    for y in range(0, len(parsed_start[x])):
        block = parsed_start[x][y]
        positions[x].append(block)

# [G]                 [D] [R]
# [W]         [V]     [C] [T] [M]
# [L]         [P] [Z] [Q] [F] [V]
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9

positions = [list(x) for x in list(zip(*positions))]
for stack in positions:
    while " " in stack:
        stack.remove(" ")

# PARSE MOVES
parsed_moves = move_data.strip().split("\n")
moves = [x.split(" ")[1::2] for x in parsed_moves]


# RUN MOVES
for move in moves:
    num, start, dest = int(move[0]), int(move[1])-1, int(move[2])-1
    stack_to_move = positions[start][:num]
    positions[dest] = stack_to_move + positions[dest]
    positions[start] = positions[start][num:]


top_chars = [x[0] for x in positions]
answer = ""
for t in top_chars:
    answer += t

####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
