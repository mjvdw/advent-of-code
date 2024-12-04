from aocd import get_data
import re

data = get_data(year=2024, day=3)


def part_a(data):
    lines = data.splitlines()

    result = 0
    for line in lines:
        # Find all parts of the data that are in the format
        # mul(x,y) where x and y are integers between 1 and 3 digits.
        # Use re.findall() to find all of these parts.
        results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        result += sum(int(x) * int(y) for x, y in results)
    return result


def part_b(data):
    lines = data.splitlines()
    result = 0
    multiply = True

    for line in lines:
        commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        values = []
        for c in commands:
            if c == "do()":
                multiply = True
                continue
            elif c == "don't()":
                multiply = False
                continue

            if multiply:
                values.append(re.findall(r"\d{1,3}", c))

        result += sum(int(x) * int(y) for x, y in values)

    return result


test_data = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

test_data2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def go(data):
    return part_b(data)


if __name__ == "__main__":
    # assert part_a(test_data) == 161
    # assert part_b(test_data2) == 48
    print(part_a(data))
    print(part_b(data))
