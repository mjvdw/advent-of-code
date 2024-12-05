from itertools import pairwise

sample_data = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def go(data: str) -> int | str:
    rules = [[int(y) for y in x.split("|")] for x in data.split("\n\n")[0].splitlines()]
    updates = [
        [int(a) for a in z.split(",")] for z in data.split("\n\n")[1].splitlines()
    ]

    part1 = 0
    sorted = [u for u in updates if is_sorted(u, rules)]
    for u in sorted:
        part1 += u[len(u) // 2]

    part2 = 0
    sorted = [sort(u, rules) for u in updates if not is_sorted(u, rules)]
    for u in sorted:
        part2 += u[len(u) // 2]

    print(sorted)
    print(part2)

    return part2


def is_sorted(update: list[int], rules: list[list[int]]) -> bool:
    for i, u in enumerate(update):
        left = update[:i]
        for r in rules:
            if r[0] == u:
                if r[1] not in left:
                    continue
                else:
                    return False

    return True


def sort(update: list[int], rules: list[list[int]]) -> list[int]:
    while not is_sorted(update, rules):
        for i, pair in enumerate(pairwise(update)):
            for r in rules:
                if r[0] == pair[0] or r[0] == pair[1]:
                    if r[1] == pair[0]:
                        update[i], update[i + 1] = update[i + 1], update[i]
                        break

    return update


if __name__ == "__main__":
    go(sample_data)
