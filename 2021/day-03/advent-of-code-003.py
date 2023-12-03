OXYGEN = "OXYGEN"
CO2 = "CO2"


def get_values():
    values = []

    with open('puzzle-input.txt') as f:
        values_str = f.readlines()
        for v in values_str:
            values.append(v.strip("\n"))

    return values


def convert_binary_to_number(binary):
    number = 0

    # Reversed so that the first digit is in the "one" positions, second is in the "two", third
    # is "four", fourth is "eight", etc. Could also do the pow() funciton in reverse as well.
    reverse_binary = binary[::-1]

    for n in range(len(binary)):
        if reverse_binary[n] == "1":
            number = number + pow(2,n)

    return number


def invert(binary):
    inverted = ""

    for n in binary:
        if n == "1":
            inverted = inverted + "0"
        elif n == "0":
            inverted = inverted + "1"
    
    return inverted


def count_at_position(n, values, t):
    one = 0
    zero = 0

    for value in values:
        for bit in value[n]:
            if bit == "1":
                one += 1
            elif bit == "0":
                zero += 1

    if t == OXYGEN:
        if one > zero:
            return "1"
        elif zero > one:
            return "0"
        else: 
            return "1"
    else:
        if one > zero:
            return "0"
        elif zero > one:
            return "1"
        else: 
            return "0"


def part_one():
    values = get_values()
    binary = ""

    for n in range(len(values[0])):
        binary = binary + count_at_position(n, values, OXYGEN)

    gamma = convert_binary_to_number(binary)
    epsilon = convert_binary_to_number(invert(binary))
    answer = gamma * epsilon
    
    print("Answer:", answer)


def part_two():
    values = get_values()

    def get_binary_result(values, t):
        result_binary = ""
        for n in range(len(values[0])):
            result_binary += count_at_position(n, values, t)
            if len(values) == 1: break
            values = list(filter(lambda x: x.startswith(result_binary), values))
    
        return values[0]
    
    oxygen_generator = convert_binary_to_number(get_binary_result(values, OXYGEN))
    co2_scrubber = convert_binary_to_number(get_binary_result(values, CO2))
    answer = oxygen_generator * co2_scrubber
    
    print("Answer:", answer)


if __name__ == "__main__":
    part_one()
    part_two()