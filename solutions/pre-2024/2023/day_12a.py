import copy
import itertools

sample_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


class Row(object):
    def __init__(self, springs: str, groups: list[int]) -> None:
        self.springs = springs
        self.groups = groups

    @property
    def arrangements(self) -> list[str]:
        possible_arrangements = []

        num_unknowns = self.springs.count("?")
        products = itertools.product("#.", repeat=num_unknowns)
        for p in products:
            a = copy.copy(self.springs)
            for char in p:
                a = a.replace("?", char, 1)

            possible_arrangements.append(a)

        arrangements = [
            a for a in possible_arrangements if self._is_valid_arrangement(a)
        ]
        return arrangements

    def _is_valid_arrangement(self, arrangement: str) -> bool:
        groups = [a for a in arrangement.split(".") if a != ""]
        is_valid = [len(b) for b in groups] == self.groups
        return is_valid


def go(data):
    # data = sample_data
    data = data.splitlines()

    rows = []
    for line in data:
        rows.append(
            Row(
                springs=line.split()[0],
                groups=[int(l) for l in line.split()[1].split(",")],
            )
        )

    answer = 0
    for row in rows:
        answer += len(row.arrangements)

    print("Answer:", answer)
    return answer
