from aocd import get_data

data = get_data(year=2024, day=4)

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


class Vector(object):
    HORIZONTAL = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    ADJACENT_ADJUSTMENTS = []

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_adjacent_coordinates(
        self,
        horizontal: bool = True,
        diagonal: bool = True,
    ) -> list:
        if horizontal and diagonal:
            ADJACENT_ADJUSTMENTS = self.HORIZONTAL + self.DIAGONAL
        elif not diagonal:
            ADJACENT_ADJUSTMENTS = self.HORIZONTAL
        elif not horizontal:
            ADJACENT_ADJUSTMENTS = self.DIAGONAL
        else:
            raise Exception(
                "You must include at least horizontal or diagonal coordinates."
            )

        adj_coords = []
        for adj in ADJACENT_ADJUSTMENTS:
            adj_x = self.x + adj[0]
            adj_y = self.y + adj[1]
            if (adj_x >= 0) and (adj_y >= 0):
                coord = (adj_x, adj_y)
                adj_coords.append(coord)

        return adj_coords

    def move(self, adjustment_coords) -> tuple[int]:
        self.x = self.x + adjustment_coords.x
        self.y = self.y + adjustment_coords.y


def go(data):
    data = [[*line] for line in data.splitlines()]
    # data = data.splitlines()

    # Identify all the X's, add coords to a list.
    valid_x_coords = []
    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            if letter == "X":
                valid_x_coords.append(Vector(x, y))

    print(valid_x_coords)

    # Identify all the M's that are adjacent to a valud X, add coords to a list.
    valid_m_coords = []
    for v in valid_x_coords:
        adj = v.get_adjacent_coordinates()
        print(adj)
        for a in adj:
            if data[a[0]][a[1]] == "M":
                valid_m_coords.append(a)

    print(len(valid_m_coords))

    # Identify all the A's that are adjacent to a valid M in the opposite direction from the X, add coords to a list.

    # Identify all the S's that are adjacent to a valid A, in the opposite direction from the A, add coords to a list.


if __name__ == "__main__":
    assert go(sample_data) == 18
    # print(go(data))
