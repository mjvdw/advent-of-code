import utils
from itertools import chain

sample_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

sample_data_2 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

sample_data_3 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


class Location(object):
    HORIZONTAL = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    TURN_CHARACTERS = ["F", "7", "L", "J"]
    STRAIGHT_CHARACTERS = ["|", "-"]
    NON_GROUND_CHARACTERS = TURN_CHARACTERS + STRAIGHT_CHARACTERS
    GROUND = ["."]

    DIRECTIONS = {
        "up-left": (-1, -1),
        "up": (0, -1),
        "up-right": (1, -1),
        "left": (-1, 0),
        "right": (1, 0),
        "down-left": (-1, 1),
        "down": (0, 1),
        "down-right": (1, 1),
    }

    MOVES = {
        "F": ["down", "right"],
        "7": ["down", "left"],
        "L": ["up", "right"],
        "J": ["up", "left"],
        "|": ["up", "down"],
        "-": ["left", "right"],
        "S": ["up", "down", "left", "right"],
    }

    def __init__(self, x, y, data: list[list]) -> None:
        self.data = data
        self.x = x
        self.y = y

        self.last_move = None

    @property
    def value(self):
        return self.data[self.y][self.x]

    def take_step(self) -> None:
        next_move = tuple()

        if self.value == "S":
            valid_move_options = []
            adj_coords = self.HORIZONTAL

            for x, y in adj_coords:
                value = self.data[self.y + y][self.x + x]
                if value in self.NON_GROUND_CHARACTERS:
                    moves = [self.DIRECTIONS[m] for m in self.MOVES[value]]
                    possible_moves = [n for n in moves if (-x, -y) != (n[0], n[1])]
                    if len(possible_moves) == 1:
                        valid_move_options.append(possible_moves[0])

            if len(valid_move_options) != 2:
                raise Exception("This may not be a loop, something's gone wrong.")

            # Arbitrarily pick a direction - shouldn't ultimately matter.
            next_move = valid_move_options[1]

        elif self.value in self.NON_GROUND_CHARACTERS:
            valid_move_options = [self.DIRECTIONS[m] for m in self.MOVES[self.value]]
            valid_move_options.remove(self.last_move)
            next_move = valid_move_options[0]
        else:
            raise Exception("It looks like you're outside the loop.")

        self.last_move = (-next_move[0], -next_move[1])
        self.x += next_move[0]
        self.y += next_move[1]
        return (self.x, self.y)


def go(data):
    # data = sample_data_2
    data = utils.convert_to_2d_array(data)

    # Find starting vector.
    start = None
    for i, line in enumerate(data):
        if "S" in line:
            start = utils.Vector(x=line.index("S"), y=i)

    start_location = Location(start.x, start.y, data)
    tracker = Location(start.x, start.y, data)

    all_coords = set(
        chain.from_iterable(
            [[(x, y) for x in range(len(data[y]))] for y in range(len(data))]
        )
    )
    loop = get_loop(start_location, tracker)
    non_loop = all_coords - set(loop)

    answer = 0
    for coords in non_loop:
        if is_inside_loop(coords, loop, data):
            data[coords[1]][coords[0]] = "X"
            answer += 1

    for line in data:
        s = ""
        for l in line:
            s += l
        print(s)

    print("Answer", answer, answer <= 1447 and answer > 550)
    return answer


def get_loop(start_location: Location, tracker: Location) -> list[tuple]:
    loop = [(start_location.x, start_location.y)]

    loop_complete = False
    while not loop_complete:
        loop.append(tracker.take_step())
        loop_complete = (tracker.x, tracker.y) == (start_location.x, start_location.y)

    return loop


def is_inside_loop(
    vector: tuple[int, int],
    loop: list[tuple[int, int]],
    data: list[tuple],
) -> bool:
    crossings = 0
    move = (0, -1)

    last_turn_character = ""
    while vector[0] >= 0 and vector[1] >= 0:
        if vector in loop:
            value = data[vector[1]][vector[0]]
            if value in Location.TURN_CHARACTERS and last_turn_character:
                match value:
                    case "F":
                        if last_turn_character == "J":
                            crossings += 1
                    case "L":
                        if last_turn_character == "7":
                            crossings += 1
                    case "7":
                        if last_turn_character == "L":
                            crossings += 1
                    case "J":
                        if last_turn_character == "F":
                            crossings += 1
                last_turn_character = ""
            elif value in Location.TURN_CHARACTERS and not last_turn_character:
                last_turn_character = value
            elif value == "-":
                crossings += 1
            elif value == "S":
                one_left = data[vector[1]][vector[0] - 1]
                one_right = data[vector[1]][vector[0] + 1]
                if last_turn_character == "J" and (
                    one_right == "J" or one_right == "7" or one_right == "-"
                ):
                    crossings += 1
                elif last_turn_character == "L" and (
                    one_left == "F" or one_left == "L" or one_left == "-"
                ):
                    crossings += 1
                last_turn_character = ""

        vector = (vector[0] + move[0], vector[1] + move[1])

    return crossings % 2 == 1 and crossings >= 1
