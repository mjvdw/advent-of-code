from martyns_brain import Vector, DIAGONAL_NEIGHBOURS
from collections import defaultdict

sample_data = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def go(data):
    data = [[*line] for line in data.splitlines()]
    values = defaultdict(str)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            values[Vector(i, j)] = char

    part1 = 0

    for x in dict(filter(lambda x: x[1] == "x", values.items())):
        print("Something")
        part1 += find_xmas(x, DIAGONAL_NEIGHBOURS, values, "MAS")

    print(part1)

    return part1


def find_xmas(vector, directions, values, xmas):
    for i in range(1, len(xmas)):
        valid_directions = []
        for d in directions:
            if (values[vector + (d * i)]) == xmas[i]:
                valid_directions.append(d)

    return 1


if __name__ == "__main__":
    assert go(sample_data) == 18
    # print(go(data))
