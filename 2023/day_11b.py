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

SCALE_FACTOR = 1000000


def go(data):
    # data = sample_data
    data = data.splitlines()

    # Create reference grid.
    reference_grid = get_reference_grid(data)

    # Locate galaxies in original grid.
    galaxies = locate_galaxies(data, reference_grid)

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


def get_reference_grid(start_grid: list[str]) -> list[int]:
    reference_grid = [
        [[x, y] for x, _ in enumerate(start_grid[y])] for y, _ in enumerate(start_grid)
    ]

    # Expand rows (y)
    new_line_indexes = []
    for i, line in enumerate(start_grid):
        if set(line) == {"."}:
            new_line_indexes.append(i)

    inserted_rows = 0
    for y in range(len(start_grid)):
        if y in new_line_indexes:
            inserted_rows += SCALE_FACTOR - 1

        for x in range(len(start_grid[y])):
            reference_grid[y][x][1] += inserted_rows

    # Expand columns (x)
    new_col_indexs = []
    for k in range(len(start_grid[0])):
        column = []
        for i in range(len(start_grid)):
            column.append(start_grid[i][k])
        if set(column) == {"."}:
            new_col_indexs.append(k)

    inserted_cols = 0
    for x in range(len(start_grid[0])):
        if x in new_col_indexs:
            inserted_cols += SCALE_FACTOR - 1
        for y in range(len(start_grid[y])):
            reference_grid[y][x][0] += inserted_cols

    return reference_grid


def locate_galaxies(grid: list[str], reference_grid: list[list]) -> set[list[int, int]]:
    galaxies = []

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
            galaxies.append([reference_grid[y][x][0], reference_grid[y][x][1]])

    return galaxies
