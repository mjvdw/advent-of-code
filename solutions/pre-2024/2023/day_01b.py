sample_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def go(data):
    # data = sample_data

    data = data.splitlines()
    coords = []

    words_to_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for line in data:

        valid_keys = []

        print("OLD: ", line)
        for key, value in words_to_numbers.items():

            indexes = find_substring_indexes(line, key)
            for i in indexes:
                if i >= 0:
                    valid_keys.append([i, key, value])
        
        for char in line:
            y = None
            try:
                y = int(char)
            except:
                pass
                
            if y:
                indexes = find_substring_indexes(line, char)
                for i in indexes:
                    if i >= 0:
                        valid_keys.append([i, char, char])

        sorted_keys = sorted(valid_keys)
        print(sorted_keys)

        c = sorted_keys[0][2] + sorted_keys[-1][2]
        coords.append(c)
        print(f"NEW: {line} => {c}\n")

    print(coords)

    answer = 0
    for a in coords:
        answer += int(a)
    
    print(answer)

    return answer

def find_substring_indexes(haystack, needle):
     indexes = []
     index = haystack.find(needle)
     while index != -1:
         indexes.append(index)
         index = haystack.find(needle, index + 1)
     return indexes