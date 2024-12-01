from functools import reduce

sample_data = """Time:      7  15   30
Distance:  9  40  200"""


def get_distance(time_held: int, duration: int):
    distance = time_held * (duration - time_held)
    return distance


def go(data):
    # data = sample_data

    parsed = data.splitlines()
    times = [int(t) for t in parsed[0].split(":")[1].split()]
    distance_records = [int(t) for t in parsed[1].split(":")[1].split()]
    ways_to_win = []

    for i in range(len(times)):
        count = 0
        for j in range(times[i]):
            if get_distance(j, times[i]) > distance_records[i]:
                count += 1

        ways_to_win.append(count)

    answer = reduce((lambda x, y: x * y), ways_to_win)
    print(answer)
    return answer
