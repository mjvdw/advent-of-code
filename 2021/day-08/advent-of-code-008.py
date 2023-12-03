TT = "TT"   # Top
TL = "TL"   # Top left
TR = "TR"   # Top right
MD = "MD"   # Middle
BL = "BL"   # Bottom left
BR = "BR"   # Bottom right
BB = "BB"   # Bottom


class Inputs:
    def __init__(self, signal_patterns, outputs):
        self.signal_patterns = self.alphabetise(signal_patterns)
        self.outputs = self.alphabetise(outputs)

        self.translations = self.translate_signal_patterns(self.signal_patterns)


    def translate_signal_patterns(self, signal_patterns):
        mapped_signal = dict.fromkeys(signal_patterns)

        # Dictionary for identifying the letter used each segment.
        segments = dict.fromkeys([TT, TL, TR, MD, BL, BR, BB])
        segment_expected_values = {
            48: TT,
            24: TL,
            32: TR, 
            35: MD,
            12: BL,
            45: BR,
            42: BB
        }

        # Dictionary to count number of times a letter appears.
        segment_count = {
            "a": dict.fromkeys(["Total","Remaining","Product"], 0),
            "b": dict.fromkeys(["Total","Remaining","Product"], 0),
            "c": dict.fromkeys(["Total","Remaining","Product"], 0),
            "d": dict.fromkeys(["Total","Remaining","Product"], 0),
            "e": dict.fromkeys(["Total","Remaining","Product"], 0),
            "f": dict.fromkeys(["Total","Remaining","Product"], 0),
            "g": dict.fromkeys(["Total","Remaining","Product"], 0)
        }

        # Mapping for digits based solely on number of segments.
        length_based_digits = {
            2:1,
            4:4,
            3:7,
            7:8
        }

        for pattern in signal_patterns:
            
            # Identify digits based on length, as applicable.
            if len(pattern) in length_based_digits.keys():
                mapped_signal[pattern] = length_based_digits[len(pattern)]
            
            # Get total and remaining count for each letter
            for letter in segment_count.keys():
                if letter in pattern:
                    segment_count[letter]["Total"] += 1

                if (letter in pattern) and (mapped_signal[pattern] == None):
                    segment_count[letter]["Remaining"] += 1
            
        for letter in segment_count.keys():
            segment_count[letter]["Product"] = segment_count[letter]["Total"] * segment_count[letter]["Remaining"]
            segment_key = segment_expected_values[segment_count[letter]["Product"]]
            segments[segment_key] = letter
        
        # Dictionary mapping segments back to remaining digits.
        digits = [
            ([TT,TL,TR,BL,BR,BB],0),
            ([TT,TR,MD,BL,BB],2),
            ([TT,TR,MD,BR,BB],3),
            ([TT,TL,MD,BR,BB],5),
            ([TT,TL,MD,BL,BR,BB],6),
            ([TT,TL,TR,MD,BR,BB],9),
        ]

        for digit in digits:
            digit_str = ""
            for segment in digit[0]:
                digit_str += segments[segment]
            
            alphabetised_string = "".join(sorted(digit_str))
            mapped_signal[alphabetised_string] = digit[1]

        return mapped_signal

    
    def alphabetise(self, value):  
        alphabetised_strings = []
    
        for v in value:
            alphabetised_string = "".join(sorted(v))
            alphabetised_strings.append(alphabetised_string)

        return alphabetised_strings


class Display:
    def __init__(self, inputs):
        self.inputs = inputs


    @property
    def digits(self):
        translations = self.inputs.translations
        output_as_digits = [translations[x] for x in self.inputs.outputs]

        return output_as_digits
    
    @property
    def value(self):
        value_str = ""

        for digit in self.digits:
            value_str += str(digit)

        value = int(value_str)
        return value


def get_input_from_file():
    displays = []

    with open("puzzle-input.txt") as f:
        content = f.readlines()
        content = list(map(lambda x: x.strip("\n"),content))
        
        patterns = []
        outputs = []

        for line in content:
            patterns_str = line.split(" | ")[0]
            patterns.append([s for s in patterns_str.split(" ")])

            output_str = line.split(" | ")[1]
            outputs.append([o for o in output_str.split(" ")])
        
        for i in range(len(patterns)):
            displays.append(Display(Inputs(patterns[i],outputs[i])))
    
    return displays


def part_one():
    displays = get_input_from_file()

    count = 0
    search_values = [1,4,7,8]

    for display in displays:
        for digit in display.digits:
            if digit in search_values:
                count += 1
    
    print("Answer", count)


def part_two():
    displays = get_input_from_file()

    total_sum = 0

    for display in displays:
        total_sum += display.value

    print("Answer", total_sum)


if __name__ == "__main__":
    # part_one()
    part_two()