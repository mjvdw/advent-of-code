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
