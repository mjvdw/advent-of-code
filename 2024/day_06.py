from aocd import get_data
from collections import defaultdict
from martyns_brain import Vector, get_bounds, print_grid

sample_data = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def go(data: str) -> int | str:
    grid = defaultdict(str)
    guard = Vector(0, 0)
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            grid[Vector(x, y)] = char
            if char == "^":
                guard = Vector(x, y)

    d_index = 0
    directions = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]
    _, end = get_bounds(grid.keys())
    while guard.y <= end.y and guard.x <= end.x:
        part1 = len([_ for _ in filter(lambda x: x[1] == "X", grid.items())])
        next_step = guard + directions[d_index]
        if grid[next_step] == "#":
            d_index = d_index + 1 if d_index < 3 else 0
            continue
        guard = next_step
        grid[guard] = "X"

    print_grid(grid)
    print(part1)
    return part1


if __name__ == "__main__":
    data = get_data(day=6, year=2024)
    # print(data)
    # go(sample_data)
    go(data)
