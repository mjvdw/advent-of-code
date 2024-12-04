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
        adj_coords = utils.get_adjacent_coordinates(coords=self.coords, data=data)
        adj_values = [data[a[0]][a[1]] for a in adj_coords]
        symbols = [s for s in adj_values if s != "."]
        return len(symbols) > 0


class Gear(object):
    def __init__(self, coords: tuple) -> None:
        self.coords = coords
        self.part_values = []

    def is_valid_gear(self, data: list[list]) -> bool:
        adj_parts = self._get_adjacent_parts(data)
        if len(adj_parts) == 2:
            return True
        else:
            return False

    def _get_adjacent_parts(self, data: list[list]) -> list[Part]:
        adj_coords = utils.get_adjacent_coordinates(coords=[self.coords], data=data)

        possible_adj_part_coords = []
        for c in adj_coords:
            if utils.can_convert_to_integer(data[c[0]][c[1]]):
                possible_adj_part_coords.append(c)

        number = ""
        coords = []
        parts = []

        y = 0
        while y < len(data):
            x = 0
            while x < len(data[y]):
                cell = data[y][x]

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

        adj_parts = []
        for part in parts:
            for possible in possible_adj_part_coords:
                if (possible in part.coords) and (part not in adj_parts):
                    adj_parts.append(part)

        return adj_parts

    def get_ratio(self, data: list[list]) -> int:
        adj_parts = self._get_adjacent_parts(data)
        ratio = 1
        for p in adj_parts:
            ratio = ratio * p.value
        return ratio


def go(data):
    # data = sample_data
    parsed = utils.convert_to_2d_array(data)

    gears = []

    y = 0
    while y < len(parsed):
        x = 0
        while x < len(parsed[y]):
            cell = parsed[y][x]

            if cell == "*":
                gear = Gear(coords=(y, x))
                gears.append(gear)
            x += 1
        y += 1

    gear_ratios = [g.get_ratio(parsed) for g in gears if g.is_valid_gear(parsed)]
    answer = sum(gear_ratios)
    print(answer)
    return answer
