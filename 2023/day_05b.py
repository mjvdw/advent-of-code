sample_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class Mapping(object):
    def __init__(
        self, destination_range_start: int, source_range_start: int, range_length: int
    ):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length


def go(data):
    # data = sample_data

    raw_mapping = [m for m in data.splitlines()[2:]]
    mappings = dict()
    for index, line in enumerate(raw_mapping):
        if line.endswith("map:"):
            start_position = line.split("-")[0]
            mappings[start_position] = dict()

            target_position = line.split("-")[2].split()[0]
            mappings[start_position]["target"] = target_position
            mappings[start_position]["maps"] = []

            current_mapping = True

            while current_mapping and index < len(raw_mapping) - 1:
                index += 1
                if raw_mapping[index] == "":
                    current_mapping = False
                    break
                destination_range_start, source_range_start, range_length = [
                    int(r) for r in raw_mapping[index].split()
                ]
                mapping = Mapping(
                    destination_range_start, source_range_start, range_length
                )

                mappings[start_position]["maps"].append(mapping)

    locations = []
    current_position = "seed"

    seeds = [int(s) for s in data.splitlines()[0].split()[1:]]
    seed_pairs = []

    for i in range(0, len(seeds), 2):
        seed_pairs.append(seeds[i : i + 2])

    for pair in seed_pairs:
        source_range = set(range(pair[0], pair[0] + pair[1]))

        while current_position != "location":
            for m in mappings[current_position]["maps"]:
                mapped_source_range = set(
                    range(
                        m.source_range_start,
                        m.source_range_start + m.range_length,
                    )
                )

                source_overlap = source_range.intersection(mapped_source_range)
                new_source_range = set(
                    [x for x in source_range if x not in source_overlap]
                ).union(source_overlap)

                source_range.union(new_source_range)

                print(source_range)

                # for current_value in list(overlap):
                #     if (current_value >= m.source_range_start) and (
                #         current_value < (m.source_range_start + m.range_length)
                #     ):
                #         current_value = (
                #             current_value
                #             - m.source_range_start
                #             + m.destination_range_start
                #         )
                #         break

            current_position = mappings[current_position]["target"]

        # locations.append(current_value)
        current_position = "seed"

    # answer = min(locations)
    # print(answer)
    # return answer
