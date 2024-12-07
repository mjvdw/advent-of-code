from martyns_brain import Vector, DIAGONAL_NEIGHBOURS
from collections import defaultdict
from aocd import get_data

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
    xs = dict(filter(lambda x: x[1] == "X", values.items()))
    for x in xs:
        part1 += find_xmas(x, DIAGONAL_NEIGHBOURS, values)

    part2 = 0
    a_s = dict(filter(lambda x: x[1] == "A", values.items()))
    for a in a_s:
        part2 += find_meta_xmas(
            a,
            [Vector(1, 1), Vector(-1, 1), Vector(1, -1), Vector(-1, -1)],
            values,
        )

    return part1, part2


def find_meta_xmas(vector, directions, values):
    letters = []
    letters = "".join([values[vector + d] for d in directions])

    # This doesn't work and I don't understand why.
    # It seems to be picking up scenarios that shouldn't count.
    # Works for sample data, but not for real data.

    # if "".join(sorted(letters)) == "MMSS":
    #     return 1

    # I do understand why this works, but it seems like it should be the same.
    if letters in {"MMSS", "SMSM", "SSMM", "MSMS"}:
        return 1

    return 0


def find_xmas(vector, directions, values, xmas="MAS"):
    words = 0
    for d in directions:
        count = 0
        for i in range(1, len(xmas) + 1):
            if (values[vector + (d * i)]) == xmas[i - 1]:
                count += 1
        if count == len(xmas):
            words += 1

    return words


if __name__ == "__main__":
    data = get_data(day=4, year=2024)
    print(go(sample_data))
    print(go(data))
