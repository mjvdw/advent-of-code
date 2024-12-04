class School:
    def __init__(self, fish):
        self.fish = self.convert_to_dict(fish)


    def convert_to_dict(self, fish_list):
        fish_dict = dict.fromkeys([0,1,2,3,4,5,6,7,8], 0)

        for f in fish_list:                
            fish_dict[f] += 1

        return fish_dict


    def grow(self):
        current_state = self.fish.copy()

        # All other fish (between 1 and 8) get bumped down one.
        for i in range(1,9):
            self.fish[i-1] = current_state[i]

        # Fish at 0 have another fish at 8.
        self.fish[8] = current_state[0]

        # Fish at 0 get added to fish at 6.
        self.fish[6] += current_state[0]


    @property
    def size(self):
        count = 0
        
        for f in self.fish.values():
            count += f

        return count


def get_fish_data_from_file():
    with open('puzzle-input.txt') as f:
        content = f.readlines()[0].split(",")
        content = list(map(lambda x: int(x), content))
        return content


def simulate_fish_growth(days):
    school = School(get_fish_data_from_file())

    for i in range(days):
        school.grow()

    print("Answer:", school.size)


if __name__ == "__main__":
    # Part 1
    simulate_fish_growth(80)

    # Part 2
    simulate_fish_growth(256)