from aocd import get_data


def parse_input(data):
    return [
        tuple(map(int, line.split("-"))) for line in data.split(",") if line.strip()
    ]


def part_a(data):
    input = parse_input(data)

    invalid_ids = []

    for group in input:
        id = group[0]
        while id <= group[1]:
            num_digits = int(len(str(id)))

            # If the ID is an odd number of digits, it cannot be made solely of two repeating numbers.
            if num_digits % 2 != 0:
                id += 1
                continue

            # Compare the first half of the ID with the second half.
            if str(id)[0 : int(num_digits / 2)] == str(id)[int((num_digits / 2)) :]:
                invalid_ids.append(id)
                id += 10 ** int(num_digits / 2)
                continue

            id += 1

    return sum(invalid_ids)


def part_b(data):
    input = parse_input(data)

    invalid_ids = set()

    for group in input:
        id = group[0]
        while id <= group[1]:
            num_digits = int(len(str(id)))

            for group_size in range(1, int(num_digits / 2) + 1):
                repeating_unit = str(id)[0:group_size]
                repeats = num_digits / group_size

                if float.is_integer(repeats):
                    if int(str(repeating_unit) * int(repeats)) == int(id):
                        invalid_ids.add(id)
                        continue

            id += 1

    return sum(invalid_ids)


# Import Data and Test Data
data = get_data(year=2025, day=2)

test_data = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def go(data):
    # assert part_a(test_data) == 1227775554
    assert part_b(test_data) == 4174379265
    # return part_a(data)
    return part_b(data)
