from aocd import get_data
from utils import convert_to_2d_array, Vector, Grid
import copy


def parse_input(data):
    return Grid(convert_to_2d_array(data))


def part_a(data):
    input = parse_input(data)

    count = 0

    for y in range(0, input.height):
        for x in range(0, input.width):
            v = Vector(x, y)
            is_roll = input.get_value(v) == "@"

            adj_vectors = input.get_valid_adj_vectors(v)
            adj_values = []
            for adj_vector in adj_vectors:
                adj_value = input.get_value(adj_vector)
                adj_values.append(adj_value)

            if adj_values.count("@") < 4 and is_roll:
                count += 1

    return count


def part_b(data):
    input = parse_input(data)

    count = 0

    def remove_rolls(input):
        rolls_to_remove = []
        initial_grid = copy.deepcopy(input)

        rolls_removed = 0

        for y in range(0, initial_grid.height):
            for x in range(0, initial_grid.width):
                v = Vector(x, y)
                is_roll = initial_grid.get_value(v) == "@"

                adj_vectors = initial_grid.get_valid_adj_vectors(v)
                adj_values = []
                for adj_vector in adj_vectors:
                    adj_value = initial_grid.get_value(adj_vector)
                    adj_values.append(adj_value)

                if adj_values.count("@") < 4 and is_roll:
                    rolls_to_remove.append(v)

        for roll in rolls_to_remove:
            initial_grid.set_value(roll, ".")
            rolls_removed += 1

        return initial_grid, rolls_removed

    removable_rolls_available = True
    while removable_rolls_available:
        result, rolls_removed = remove_rolls(input)

        if result == input:
            removable_rolls_available = False
        else:
            input = result
            count += rolls_removed

    return count


# Import Data and Test Data
data = get_data(year=2025, day=4)

test_data = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def go(data):
    # assert part_a(test_data) == 13
    assert part_b(test_data) == 43
    # return part_a(data)
    return part_b(data)
