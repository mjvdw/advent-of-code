def get_movements():
    movements = []

    with open('puzzle-input.txt') as f:
        movements_str = f.readlines()
        for m in movements_str:
            movements.append(m.strip("\n").split(" "))

    return movements


def print_answer(depth, horizontal):
    print("Depth:", depth)
    print("Horizontal:", horizontal)

    answer = depth * horizontal
    print("Answer:", answer)


def part_one():
    movements = get_movements()
    depth = 0
    horizontal = 0

    for movement in movements:
        direction = movement[0]
        distance = int(movement[1])

        if direction == "up":
            depth = depth - distance
        elif direction == "down":
            depth = depth + distance
        elif direction == "forward":
            horizontal = horizontal + distance
        else:
            print("There's something else going on here.")

    print_answer(depth, horizontal)


def part_two():
    movements = get_movements()
    depth = 0
    horizontal = 0
    aim = 0

    for movement in movements:
        direction = movement[0]
        distance = int(movement[1])

        if direction == "up":
            aim = aim - distance
        elif direction == "down":
            aim = aim + distance
        elif direction == "forward":
            horizontal = horizontal + distance
            depth = depth + (aim * distance)
        else:
            print("There's something else going on here.")

    print_answer(depth, horizontal)

    # Tried 10158456 - too low


if __name__ == "__main__":
    #part_one()
    part_two()