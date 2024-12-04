import numpy as np

sample_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

sample_data_answer = 2


def go(data):
    # data = sample_data

    histories = [[int(i) for i in h.split()] for h in data.splitlines()]

    answer = 0

    for history in histories:
        differences = [history]
        while len(set(differences[-1])) > 1:
            differences.append([x for x in np.diff(differences[-1])])

        i = 0
        next_value = differences[-1][0]
        while i < len(differences) - 1:
            next_value = differences[-i - 2][0] - next_value
            i += 1

        answer += next_value

    print(answer)
    return answer
