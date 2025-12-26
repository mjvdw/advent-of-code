from aocd import get_data
from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True)
class Circuit:
    junctions: List["Junction"]


@dataclass
class Neighbour:
    junction: "Junction"
    distance: float


@dataclass(frozen=True)
class Junction:
    x: int
    y: int
    z: int

    def nearest_neighbour(self, neighbours: List["Junction"]) -> Neighbour:
        distance, n = min(
            (get_distance(self, n), n) for n in neighbours if n is not self
        )
        return Neighbour(n, distance)


def get_distance(a: Junction, b: Junction):
    """Pythagoras in 3D"""
    return (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + (a.z - b.z) ** 2) ** (1 / 2)


def parse_input(data: str):
    return [
        Junction(int(x), int(y), int(z))
        for x, y, z in [line.split(",") for line in data.splitlines()]
    ]


def part_a(data):
    input = parse_input(data)

    sorted_junctions = sorted(input, key=lambda j: j.nearest_neighbour(input).distance)
    circuits: List["Circuit"] = [Circuit(junctions=[j]) for j in sorted_junctions]

    count = 0
    return count


def part_b(data):
    input = parse_input(data)
    count = 0
    return count


# Import Data and Test Data
data = get_data(year=2025, day=8)

test_data = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def go(data):
    assert part_a(test_data) == 40
    # assert part_b(test_data) == 40
    # return part_a(data)
    # return part_b(data)
