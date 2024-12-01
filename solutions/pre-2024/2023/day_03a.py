import utils

sample_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

ADJACENT_ADJUSTMENTS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


class Part(object):
    def __init__(self, value: int, coords: list[tuple]) -> None:
        self.value = value
        self.coords = coords

    def is_valid(self, data: list[list]) -> bool:
        adj_coords = self._get_adjacent_coords(data=data)
        adj_values = [data[a[0]][a[1]] for a in adj_coords]
        symbols = [s for s in adj_values if s != "."]
        return len(symbols) > 0

    def _get_adjacent_coords(self, data: list[list]) -> list[tuple]:
        adj_coords = []
        for c in self.coords:
            for adj in ADJACENT_ADJUSTMENTS:
                coord = (c[0] + adj[0], c[1] + adj[1])
                if (
                    (not coord in self.coords)
                    and (not coord in adj_coords)
                    and (coord[0] >= 0)
                    and (coord[1] >= 0)
                    and (coord[0] < len(data))
                    and (coord[1] < len(data[0]))
                ):
                    adj_coords.append(coord)

        return adj_coords


def go(data):
    # data = sample_data
    parsed = utils.convert_to_2d_array(data)

    number = ""
    coords = []
    parts = []

    y = 0
    while y < len(parsed):
        x = 0
        while x < len(parsed[y]):
            cell = parsed[y][x]

            if utils.can_convert_to_integer(cell):
                number += cell
                coords.append((y, x))
            elif number:
                part = Part(value=int(number), coords=coords)
                parts.append(part)
                number = ""
                coords = []
            x += 1
        y += 1

    valid_parts = [p.value for p in parts if p.is_valid(parsed)]
    answer = sum(valid_parts)
    print(answer)
    return answer
