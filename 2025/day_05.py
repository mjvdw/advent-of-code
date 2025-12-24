from aocd import get_data


def parse_input(data: str) -> tuple[list, list]:
    ranges = []
    ids = []

    for line in data.splitlines():
        if "-" in line:
            # Just in case they're not in order.
            values = (int(line.split("-")[0]), int(line.split("-")[1]))
            ranges.append((min(values), max(values)))
        elif line:
            ids.append(int(line))

    return ranges, ids


def part_a(data):
    ranges, ids = parse_input(data)

    count = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                count += 1
                break

    return count


def part_b(data):
    ranges, _ = parse_input(data)

    # Merge ranges to avoid double counting.
    ranges.sort()
    merged_ranges = []

    cur_lower, cur_upper = ranges[0]

    for lower, upper in ranges[1:]:
        if lower <= cur_upper:
            cur_upper = max(upper, cur_upper)
        else:
            merged_ranges.append((cur_lower, cur_upper))
            cur_lower, cur_upper = lower, upper

    merged_ranges.append((cur_lower, cur_upper))

    # Simple subtraction to identify size of ranges, then add them up.
    count = 0
    for mr in merged_ranges:
        count += mr[1] - mr[0] + 1

    return count


# Import Data and Test Data
data = get_data(year=2025, day=5)

test_data = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def go(data):
    # assert part_a(test_data) == 3
    assert part_b(test_data) == 14
    # return part_a(data)
    return part_b(data)
