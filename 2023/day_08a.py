sample_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def go(data):
    # data = sample_data
    instructions = data.splitlines()[0]
    network = {}
    for line in data.splitlines()[2:]:
        network[line.split()[0]] = {
            "L": line.split("(")[1].split(",")[0].strip(),
            "R": line.split("(")[1].split(",")[1][:-1].strip(),
        }

    location = "AAA"
    n = 0

    while location != "ZZZ":
        index = n % len(instructions)
        n += 1

        instruction = instructions[index]
        location = network[location][instruction]

    answer = n
    print("Answer:", answer)
    return answer
