from martyns_brain import Vector

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
    values = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            values[Vector(i, j)] = char

    part1 = 0
    xmas = "XMAS"
    for x in dict(filter(lambda x: x[1] == xmas[0], values.items())):
        for i, letter in enumerate(xmas[1:]):
            i += 1
            for direction in x.diagonal_neighbours():
                if (x + (direction * i)) == xmas[i]:
                    continue
    print(part1)

    return part1


if __name__ == "__main__":
    assert go(sample_data) == 18
    # print(go(data))
