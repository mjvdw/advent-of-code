from aocd import get_data


def parse_input(data):
    return [battery for battery in [list(bank) for bank in data.splitlines()]]


def part_a(data):
    input = parse_input(data)

    joltages = []

    for bank in input:
        joltage_str = ""
        index = 0
        for battery in range(0, 2):
            integers = map(str, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
            for i in integers:
                if i in bank[index : -1 if battery == 0 else None]:
                    index = list.index(bank, i) + 1
                    joltage_str += i
                    break

        joltages.append(int(joltage_str))

    return sum(joltages)


def part_b(data):
    input = parse_input(data)

    joltages = []

    for bank in input:
        joltage_str = ""
        index = 0
        for battery in range(0, 12):
            integers = map(str, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
            for i in integers:
                upper_index = min(len(bank) - 11 + battery, len(bank))
                search_part = bank[index:upper_index]
                if i in search_part:
                    index = list.index(bank[index:], i) + 1 + index
                    joltage_str += i
                    break

        joltages.append(int(joltage_str))

    return sum(joltages)


# Import Data and Test Data
data = get_data(year=2025, day=3)

test_data = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


def go(data):
    # assert part_a(test_data) == 357
    assert part_b(test_data) == 3121910778619
    # return part_a(data)
    return part_b(data)
