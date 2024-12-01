def open_input(filename):
    raw_data = ""
    with open(filename) as file:
        raw_data = file.read()

    data = raw_data.split("\n\n")

    return data


def get_list_of_totals(data):

    elf_calories = []
    for d in data:
        elf = []
        for e in d.split("\n"):
            elf.append(int(e))
        elf_calories.append(elf)

    elf_calorie_totals = []
    for elf in elf_calories:
        elf_calorie_totals.append(sum(elf))

    return elf_calorie_totals


def part_one(input_file):
    totals = get_list_of_totals(open_input(input_file))
    return max(totals)


def part_two(input_file):
    totals = get_list_of_totals(open_input(input_file))
    totals.sort()
    return totals[-1] + totals[-2] + totals[-3]


def sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return(sum)


if __name__ == "__main__":
    input_file = "input.txt"

    answer_one = part_one(input_file)
    print(answer_one)
    # ANSWER 1: 68802

    answer_two = part_two(input_file)
    print(answer_two)
    # ANSWER 2: 205370
