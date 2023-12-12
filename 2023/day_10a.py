import utils
import copy

sample_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


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
            next_move = valid_move_options[0]

        elif self.value in self.NON_GROUND_CHARACTERS:
            valid_move_options = [self.DIRECTIONS[m] for m in self.MOVES[self.value]]
            valid_move_options.remove(self.last_move)
            next_move = valid_move_options[0]
        else:
            raise Exception("It looks like you're outside the loop.")

        self.last_move = (-next_move[0], -next_move[1])
        self.x += next_move[0]
        self.y += next_move[1]


def go(data):
    # data = sample_data
    data = utils.convert_to_2d_array(data)

    # Find starting vector.
    start = None
    for i, line in enumerate(data):
        if "S" in line:
            start = utils.Vector(x=line.index("S"), y=i)

    start_location = Location(start.x, start.y, data)
    tracker = Location(start.x, start.y, data)

    answer = get_loop_length(start_location, tracker) // 2
    print(answer)
    return answer


def get_loop_length(start_location: Location, tracker: Location) -> int:
    steps = 0

    loop_complete = False
    while not loop_complete:
        tracker.take_step()
        steps += 1
        loop_complete = (tracker.x, tracker.y) == (start_location.x, start_location.y)

    return steps
