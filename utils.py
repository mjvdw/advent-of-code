from typing import NamedTuple


def convert_to_2d_array(input: str):
    """Generate a 2-dimensional array from an input.
    Input must be a string, split by the `\n` character.

    Args:
        input (str): The string to convert to a 2-dimensional array.

    Returns:
        list: A list of lists of strings representing the 2-dimensional array.
    """
    array = input.splitlines()
    array = [[*line] for line in array]
    return array


def can_convert_to_integer(value: any) -> bool:
    try:
        int(value)
        return True
    except:
        return False


def get_adjacent_coordinates(coords: tuple, data: list[list]) -> list[tuple]:
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

    adj_coords = []
    for c in coords:
        for adj in ADJACENT_ADJUSTMENTS:
            coord = (c[0] + adj[0], c[1] + adj[1])
            if (
                (not coord in coords)
                and (not coord in adj_coords)
                and (coord[0] >= 0)
                and (coord[1] >= 0)
                and (coord[0] < len(data))
                and (coord[1] < len(data[0]))
            ):
                adj_coords.append(coord)

    return adj_coords


class Vector(NamedTuple):
    x: int
    y: int
