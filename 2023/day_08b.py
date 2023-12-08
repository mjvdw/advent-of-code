import math

sample_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def lcm(numbers):
    """Find lowest common multiple of a list of numbers.

    Args:
        numbers (list): The list of numbers to find the lowest common multiple of.
    """

    def lcm_pair(a, b):
        return abs(a * b) // math.gcd(a, b)

    if not numbers or len(numbers) == 0:
        return 0

    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm_pair(lcm_result, numbers[i])

    return lcm_result


def go(data):
    # data = sample_data
    instructions = data.splitlines()[0]
    network = {}
    for line in data.splitlines()[2:]:
        network[line.split()[0]] = {
            "L": line.split("(")[1].split(",")[0].strip(),
            "R": line.split("(")[1].split(",")[1][:-1].strip(),
        }

    locations = [l for l in network.keys() if l[-1] == "A"]
    path_lengths = []

    for location in locations:
        n = 0
        while location[-1] != "Z":
            index = n % len(instructions)
            n += 1
            instruction = instructions[index]
            location = network[location][instruction]
        path_lengths.append(n)

    answer = lcm(path_lengths)

    print("Answer:", answer)
    return answer
