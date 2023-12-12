from itertools import combinations

sample_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def go(data):
    # data = sample_data
    data = data.splitlines()

    # Expand grid.
    expanded_grid = expand_grid(data)

    # Locate galaxies.
    galaxies = locate_galaxies(expanded_grid)

    # List all pairs.
    pairs = list(combinations(galaxies, 2))

    # Calculate shortest path for each pair.
    answer = 0
    for pair in pairs:
        vertical_distance = abs(pair[0][1] - pair[1][1])
        horizontal_distance = abs(pair[0][0] - pair[1][0])
        answer += vertical_distance + horizontal_distance

    print(answer)
    return answer


def expand_grid(start_grid: list[str]) -> list[str]:
    expanded_grid = start_grid

    # Expand rows
    new_line_indexes = []
    for i, line in enumerate(start_grid):
        if set(line) == {"."}:
            new_line_indexes.append(i)

    inserted_rows = 0
    for j in new_line_indexes:
        expanded_grid.insert(j + inserted_rows, "." * len(start_grid[0]))
        inserted_rows += 1

    # Expand columns
    new_col_indexs = []
    for k in range(len(start_grid[0])):
        column = []
        for i in range(len(start_grid)):
            column.append(start_grid[i][k])
        if set(column) == {"."}:
            new_col_indexs.append(k)

    inserted_cols = 0
    for l in new_col_indexs:
        for i, line in enumerate(expanded_grid):
            new_line = line[: l + inserted_cols] + "." + line[l + inserted_cols :]
            expanded_grid[i] = new_line
        inserted_cols += 1

    return expanded_grid


def locate_galaxies(grid: list[str]) -> set[tuple[int, int]]:
    galaxies = set()

    for y, line in enumerate(grid):
        index = 0
        all_x = []
        while index < len(line):
            index = line.find("#", index)
            if index == -1:
                break
            all_x.append(index)
            index += 1

        for x in all_x:
            galaxies.add((x, y))

    return galaxies
