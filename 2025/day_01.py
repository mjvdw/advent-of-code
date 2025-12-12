from aocd import get_data


def parse_input(data):
    return [
        (direction, amount)
        for direction, amount in [
            (line[0], int(line[1:])) for line in data.splitlines()
        ]
    ]


def part_a(data):
    input = parse_input(data)
    current_value = 50
    num_zeros = 0

    for direction, amount in input:
        # Convert amount into an effective amount within 0-99 range
        amount = amount % 100

        if direction == "L":
            # Decrease value, but not below 0 - loop back to 99.
            current_value -= amount
            if current_value < 0:
                current_value += 100

        elif direction == "R":
            # Increase value, but not above 99 - loop back to 0.

            current_value += amount
            if current_value > 99:
                current_value -= 100

        if current_value == 0:
            num_zeros += 1

    return num_zeros


def part_b(data):
    input = parse_input(data)
    current_value = 50
    num_zeros = 0

    for direction, amount in input:
        if direction == "L":
            # Decrease value, but not below 0 - loop back to 99.
            for _ in range(amount):
                current_value -= 1
                if current_value < 0:
                    current_value = 99

                if current_value == 0:
                    num_zeros += 1

        elif direction == "R":
            # Increase value, but not above 99 - loop back to 0.
            for _ in range(amount):
                current_value += 1
                if current_value > 99:
                    current_value = 0

                if current_value == 0:
                    num_zeros += 1

    return num_zeros


# Import Data and Test Data
data = get_data(year=2025, day=1)

test_data = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def go(data):
    return part_b(data)


if __name__ == "__main__":
    # assert part_a(test_data) == 3
    assert part_b(test_data) == 6
    # print(part_a(data))
    print(part_b(data))
