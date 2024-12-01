from functools import reduce

sample_data = """Time:      7  15   30
Distance:  9  40  200"""


def get_distance(time_held: int, duration: int):
    distance = time_held * (duration - time_held)
    return distance


def go(data):
    # data = sample_data

    parsed = data.splitlines()
    times = [t for t in parsed[0].split(":")[1].split()]
    time = ""
    for t_str in times:
        time += t_str
    time = int(time)

    distance_records = [t for t in parsed[1].split(":")[1].split()]
    distance_record = ""
    for d_str in distance_records:
        distance_record += d_str
    distance_record = int(distance_record)

    answer = 0
    for i in range(time):
        if get_distance(i, time) > distance_record:
            answer += 1

    print(answer)
    return answer
