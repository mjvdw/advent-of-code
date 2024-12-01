from aocd import get_data


def parse(data):
    left = []
    right = []

    for line in data.splitlines():
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

    return left, right


def part_a(data):
    # Split into two lists.
    left, right = parse(data)

    # Sort lists.
    left.sort()
    right.sort()

    diffs = [abs(a - b) for a, b in zip(left, right)]
    result = sum(diffs)

    return result


def part_b(data):
    left, right = parse(data)

    result = 0

    for item in left:
        result += item * sum(1 for r in right if r == item)

    return result


# Import Data and Test Data
data = get_data(year=2024, day=1)

test_data = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


if __name__ == "__main__":
    assert part_a(test_data) == 11
    assert part_b(test_data) == 31
    print(part_a(data))
    print(part_b(data))
