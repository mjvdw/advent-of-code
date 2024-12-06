from aocd import get_data
from martyns_brain import Vector, get_bounds

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
    grid = {}
    guard = Vector(0, 0)
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            grid[Vector(x, y)] = char
            if char == "^":
                guard = Vector(x, y)

    grid, _ = walk(grid, guard)
    # grid now contains the path of the guard marked with "X"

    part1 = len([a for a in filter(lambda x: x[1] == "X", grid.items())])

    obstructions = [a[0] for a in filter(lambda x: x[1] == "X", grid.items())]
    obstructions.remove(guard)

    part2 = 0
    for obstruction in obstructions:
        print("Obstruction:", obstruction)
        new_grid = grid.copy()
        new_grid[obstruction] = "#"
        _, looped = walk(new_grid, guard)
        if looped:
            part2 += 1

        print("Obstruction:", obstruction, "Looped:", looped)

    return part1, part2


def walk(grid, guard):
    d_index = 0
    directions = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]
    _, end = get_bounds(grid.keys())
    obstructions_seen = []
    looped = False
    while guard.y <= end.y and guard.x <= end.x:
        grid[guard] = "X"
        next_step = guard + directions[d_index]
        try:
            if grid[next_step] == "#":
                if (next_step, d_index) in obstructions_seen:
                    looped = True
                    break
                obstructions_seen.append((next_step, d_index))
                d_index = d_index + 1 if d_index < 3 else 0
                continue
        except KeyError:
            break
        guard = next_step

    return grid, looped


if __name__ == "__main__":
    data = get_data(day=6, year=2024)
    # print(go(sample_data))
    print(go(data))
