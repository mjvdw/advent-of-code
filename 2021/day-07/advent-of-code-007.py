from os import truncate


def get_positions_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()[0].split(",")
        content = list(map(lambda x: int(x), content))
        return content


def part_one():
    positions = get_positions_from_file()    
    fuel_movements = []

    # Working goes here.
    max_position = max(positions)
    min_position = min(positions)

    for i in range(min_position, max_position + 1):
        fuel_used = 0
        for position in positions:
            fuel_used += abs(position - i)

        fuel_movements.append(fuel_used)

    min_fuel_used = min(fuel_movements)
    print("Answer", min_fuel_used)


def part_two():
    positions = get_positions_from_file()
    fuel_movements = []

    # Working goes here.
    max_position = max(positions)
    min_position = min(positions)

    for i in range(min_position, max_position + 1):
        fuel_used = 0
        for position in positions:
            distance = abs(position - i)
            fuel_used += abs((distance * (distance + 1))/2)

        fuel_movements.append(fuel_used)

    min_fuel_used = min(fuel_movements)
    print("Answer", min_fuel_used)


if __name__ == "__main__":
    part_one()
    part_two()