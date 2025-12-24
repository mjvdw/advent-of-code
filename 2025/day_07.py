from aocd import get_data
from utils import Grid, Vector
import copy


def parse_input(data: str):
    return Grid([list(row) for row in data.splitlines()])


def part_a(data):
    manifold = parse_input(data)
    start = Vector(manifold.input_2d_array[0].index("S"), 0)

    count = 0
    down = (0, 1)
    beams = [start]

    for _ in manifold.input_2d_array:
        new_beams = []
        for beam in beams:
            if beam.y == len(manifold.input_2d_array) - 1:
                break
            beam.move(down)
            if manifold.get_value(beam) == "^":
                # Replace with left and right beam.
                left = Vector(beam.x - 1, beam.y)
                right = Vector(beam.x + 1, beam.y)
                new_beams.extend([left, right])
                count += 1
            else:
                new_beams.append(beam)

        # Remove duplicates once the whole row has been calculated.
        beams = list(set(new_beams))

    return count


def part_b(data):
    manifold = parse_input(data)

    row_cur = [1 if x == "S" else 0 for x in manifold.input_2d_array[0]]

    for i in range(1, manifold.height):
        row = manifold.input_2d_array[i]
        prev_row = copy.deepcopy(row_cur)

        splitter_indexes = [j for j, v in enumerate(row) if v == "^"]
        if not splitter_indexes:
            continue

        new_timelines = [(s - 1, s, s + 1) for s in splitter_indexes]
        for nt in range(0, len(new_timelines)):
            left, split, right = new_timelines[nt]
            row_cur[split] = 0
            row_cur[left] += prev_row[split]
            row_cur[right] += prev_row[split]

    timelines = sum(row_cur)
    return timelines


# Import Data and Test Data
data = get_data(year=2025, day=7)

test_data = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def go(data):
    # assert part_a(test_data) == 21
    assert part_b(test_data) == 40
    # return part_a(data)
    return part_b(data)
