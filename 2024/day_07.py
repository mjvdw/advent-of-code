from aocd import get_data
from math import prod
from itertools import permutations, zip_longest, chain, product

data = get_data(day=7, year=2024)
sample_data = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def go(data):
    data = [[a for a in x.split(":")] for x in data.splitlines()]
    terms = [[int(b[0]), [int(c) for c in b[1].split()]] for b in data]

    part1 = 0
    for term in terms:
        if is_valid_solution(term[0], term[1]):
            part1 += term[0]

    part2 = 0

    return part1, part2


def is_valid_solution(solution, terms):
    max = prod(terms)
    min = sum(terms)

    if solution <= min or solution >= max:
        possible_operators = ["+", "*"]
        operator_configs = list(product(possible_operators, repeat=len(terms) - 1))

        # for config in operator_configs:
        #     equation = list(chain(*(zip_longest(terms, config))))[:-1]
        # results = {}
        for operators in operator_configs:
            result, expression = evaluate_left_to_right(terms, operators)
            print(solution, result, expression)
            if solution == result:
                return True
            # if result not in results:
            #     results[result] = []
            # results[result].append(expression)

    return False


def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    expression = str(numbers[0])

    for i in range(len(operators)):
        operator = operators[i]
        next_number = numbers[i + 1]
        expression += f" {operator} {next_number}"

        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number

    return result, expression


if __name__ == "__main__":
    print(go(sample_data))
    # assert go(sample_data) == (3749, 0)
    # print(go(data))
