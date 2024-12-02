from aocd import get_data

data: str = get_data(year=2024, day=2)


def part_a(data: str) -> int:
    reports: list[int][int] = [[int(y) for y in x.split()] for x in data.splitlines()]
    return count_safe_reports(reports)


def part_b(data: str) -> int:
    reports: list[int][int] = [[int(y) for y in x.split()] for x in data.splitlines()]
    return count_safe_reports(dampen_reports(reports))


def dampen_reports(reports: list[list[int]]) -> list[list[int]]:
    dampened_reports = []

    for report in reports:
        report_versions = []
        for index, _ in enumerate(report):
            report_versions.append(report[:index] + report[index + 1 :])
        dampened_reports.append(report_versions)

    return dampened_reports


def is_safe(report: list[int]) -> bool:
    diffs = get_level_diffs(report)

    trending_up = all(diff > 0 for diff in diffs)
    trending_down = all(diff < 0 for diff in diffs)
    always_trending = any(diff != 0 for diff in diffs)
    safe_trend = all(abs(diff) <= 3 for diff in diffs)

    return (trending_up or trending_down) and always_trending and safe_trend


def get_level_diffs(report: list[int]) -> list[int]:
    return [
        report[index + 1] - value
        for index, value in enumerate(report)
        if index < len(report) - 1
    ]


def count_safe_reports(reports: list[list[int]] | list[list[list[int]]]) -> int:
    safe = 0
    for report in reports:
        # If report is a tuple containing two list[int], make sure at least one of the values is safe.
        # Otherwise, check if the report is safe.
        if all(
            isinstance(item, list)
            and all(isinstance(sub_item, int) for sub_item in item)
            for item in report
        ):
            safe += 1 if any([is_safe(r) for r in report]) else 0
        else:
            safe += 1 if is_safe(report) else 0

    return safe


test_data = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    print(part_a(data))
    print(part_b(data))
