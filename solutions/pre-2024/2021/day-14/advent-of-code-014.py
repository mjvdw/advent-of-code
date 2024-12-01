class Polymer():
    def __init__(self, polymer_string, pairs):
        self.polymer_string = polymer_string
        self.pairs = pairs

        self.pair_count = dict.fromkeys(self.pairs.keys(), 0)
        for pair in self.pairs.keys():
            self.pair_count[pair] = self.polymer_string.count(pair)

        all_pairs_str = "".join([pair for pair in self.pairs.keys()])
        unique_elements = list(set(all_pairs_str))
        self.element_count = dict.fromkeys(unique_elements,0)
        for element in unique_elements:
            self.element_count[element] = self.polymer_string.count(element)


    def run_pair_insertion(self):
        new_count_dict = dict.fromkeys(self.pairs.keys(),0)

        for pair in self.pairs.keys():
            count = self.pair_count[pair]
            if count > 0:
                new_pair_1 = pair[:1] + self.pairs[pair]
                new_pair_2 = self.pairs[pair] + pair[1:]

                new_count_dict[new_pair_1] += count
                new_count_dict[new_pair_2] += count

                self.element_count[self.pairs[pair]] += count

        self.pair_count = new_count_dict

        # Option 1
        # insertion_values = []
        # for i in range(len(self.polymer_string)-1):
        #     pair = self.polymer_string[i] + self.polymer_string[i+1]
        #     insertion_value = self.pairs[pair]
        #     insertion_values.append(insertion_value)

        # new_polymer_list = list(zip(self.polymer_string, insertion_values))
        # new_polymer_str = ""

        # for element_pair in new_polymer_list:
        #     for element in element_pair:
        #         new_polymer_str += element
        
        # self.polymer_string = new_polymer_str + self.polymer_string[-1]

        # Option 2
        # search_keys = []
        # for pair in pair_keys:
        #     if pair in self.polymer_string:
        #         search_keys.append(pair)

        # for key in search_keys:
        #     insertion_value = key[0] + self.pairs[key] + key[1]
        #     self.polymer_string = self.polymer_string.replace(key, insertion_value)
        #     # print(key, insertion_value)

        # print(self.polymer_string)

        # self.interate_pair_dict()

    @property
    def most_common_element(self):
        most_common_element = max(self.element_count, key=self.element_count.get)
        return most_common_element

    @property
    def least_common_element(self):
        most_common_element = min(self.element_count, key=self.element_count.get)
        return most_common_element

    def get_element_occurrences(self, element):
        return self.element_count[element]


def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        
        template = content.pop(0).strip("\n")
        
        content.pop(0)  # Removing new line.
        pair_keys = []
        pair_values = []

        for pair in content:
            key_value = pair.strip("\n").split(" -> ")
            pair_keys.append(key_value[0])
            pair_values.append(key_value[1])

        pairs = dict(zip(pair_keys,pair_values))

        return template, pairs


def get_element_count(steps):
    template, pairs = get_content_from_file()
    polymer = Polymer(template, pairs)

    i = 0
    while i < steps:
        polymer.run_pair_insertion()
        i += 1

    most_common_count = polymer.get_element_occurrences(polymer.most_common_element)
    least_common_count = polymer.get_element_occurrences(polymer.least_common_element)

    print("Answer", most_common_count - least_common_count)


if __name__ == "__main__":
    get_element_count(10)
    get_element_count(40)
