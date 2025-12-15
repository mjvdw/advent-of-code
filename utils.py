import typing


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


def can_convert_to_integer(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
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
        square: bool = True,
        diagonal: bool = True,
    ) -> list:
        if square and diagonal:
            ADJACENT_ADJUSTMENTS = ALL_NEIGHBOURS
        elif not diagonal:
            ADJACENT_ADJUSTMENTS = SQUARE_NEIGHBOURS
        elif not square:
            ADJACENT_ADJUSTMENTS = DIAGONAL_NEIGHBOURS
        else:
            raise Exception(
                "You must include at least horizontal or diagonal coordinates."
            )

        adj_coords = []
        for adj in ADJACENT_ADJUSTMENTS:
            adj_x = self.x + adj.x
            adj_y = self.y + adj.y
            if (adj_x >= 0) and (adj_y >= 0):
                coord = Vector(adj_x, adj_y)
                adj_coords.append(coord)

        return adj_coords

    def move(self, adjustment_coords):
        self.x = self.x + adjustment_coords.x
        self.y = self.y + adjustment_coords.y


SQUARE_NEIGHBOURS = (
    Vector(0, -1),
    Vector(0, 1),
    Vector(-1, 0),
    Vector(1, 0),
)

DIAGONAL_NEIGHBOURS = (
    Vector(-1, -1),
    Vector(1, -1),
    Vector(-1, 1),
    Vector(1, 1),
)

ALL_NEIGHBOURS = SQUARE_NEIGHBOURS + DIAGONAL_NEIGHBOURS


class Grid(object):
    def __init__(self, input_2d_array):
        self.input_2d_array = input_2d_array

    def get_value(self, vector: Vector):
        return self.input_2d_array[vector.y][vector.x]

    def get_valid_adj_vectors(self, vector: Vector):
        all_adj_vectors = vector.get_adjacent_coordinates()
        valid_adj_vectors = []
        for adj_vector in all_adj_vectors:
            if adj_vector.x < len(self.input_2d_array[0]) and adj_vector.y < len(
                self.input_2d_array
            ):
                valid_adj_vectors.append(adj_vector)

        return valid_adj_vectors

    def get_adj_values(self, vector: Vector):
        valid_adj_vectors = self.get_valid_adj_vectors(vector)
        values = []
        for v in valid_adj_vectors:
            values.append(self.input_2d_array[v.y][v.x])

        return values

    @property
    def height(self):
        return len(self.input_2d_array)

    @property
    def width(self):
        return len(self.input_2d_array[0])

    def set_value(self, vector, value):
        self.input_2d_array[vector.y][vector.x] = value

    def __repr__(self) -> str:
        rep_string = ""
        for row in self.input_2d_array:
            rep_string += "\n" + str().join(row)

        return rep_string

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Grid):
            return NotImplemented
        return self.input_2d_array == value.input_2d_array
