from aocd import get_data


def parse_input(data: str):
    return


def part_a(data):
    input = [
        {"operator": eq[-1:], "values": [i for i in eq[0:-1]]}
        for eq in [list(row) for row in zip(*[r.split() for r in data.splitlines()])]
    ]

    count = 0
    for eq in input:
        eq_str = f"{eq['operator'][0]}".join(eq["values"])
        count += eval(eq_str)

    return count


def part_b(data):
    input = data.splitlines()

    operators_str = input[-1]

    class Operator:
        operator: str
        start: int

        def __repr__(self):
            return self.operator + f"({self.start})"

    operators: list[Operator] = []

    cur = 0
    op = Operator()
    for i in range(1, len(operators_str)):
        if operators_str[i] != " ":
            op.operator = operators_str[cur]
            op.start = cur
            operators.append(op)
            cur = i
            op = Operator()

    last_op = Operator()
    last_op.operator = operators_str.rstrip()[-1]
    last_op.start = len(operators_str.rstrip()) - 1
    operators.append(last_op)

    values = []

    for j in range(0, len(operators)):
        op = operators[j]
        row_values = []

        end = operators[j + 1].start - 1 if j != len(operators) - 1 else len(input[0])
        for k in range(op.start, end):
            num = ""
            for row in input[:-1]:
                num += row[k]
            row_values.append(num.strip())

        values.append(row_values)

    count = 0
    for eq, v in zip(operators, values):
        eq_str = eq.operator.join(v)
        count += eval(eq_str)

    return count


# Import Data and Test Data
data = get_data(year=2025, day=4)

test_data = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """


def go(data):
    # assert part_a(test_data) == 4277556
    assert part_b(test_data) == 3263827
    # return part_a(data)
    return part_b(data)
