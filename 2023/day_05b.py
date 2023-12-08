import copy


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


# class Mapping(object):
#     def __init__(
#         self, destination_range_start: int, source_range_start: int, range_length: int
#     ):
#         self.destination_range_start = destination_range_start
#         self.source_range_start = source_range_start
#         self.range_length = range_length
#         self.summary = f"Source: {(source_range_start, source_range_start + range_length - 1)} --> Destination: {(destination_range_start, destination_range_start + range_length - 1)}"


# class Range(object):
#     def __init__(self, start_value: int, length: int) -> None:
#         self.working_range = set([(start_value, start_value + length - 1)])

#     def transform(self, mapping: Mapping):
#         source_range = (
#             mapping.source_range_start,
#             mapping.source_range_start + mapping.range_length - 1,
#         )

#         destination_range = (
#             mapping.destination_range_start,
#             mapping.destination_range_start + mapping.range_length - 1,
#         )

#         print("Source range:", source_range, "Destination range:", destination_range)

#         iter_range = copy.copy(self.working_range)
#         for segment in iter_range:
#             self._subtract_from_range(segment, source_range)
#             self._add_to_range(segment, destination_range)

#     def _subtract_from_range(self, start_range: tuple, transform_range: tuple) -> None:
#         new_range = copy.copy(self.working_range)
#         # for segment in self.working_range:
#         a = start_range[0]
#         b = start_range[1]
#         c = transform_range[0]
#         d = transform_range[1]

#         print(f"Subtracting {transform_range} from segment", start_range)

#         def remove():
#             try:
#                 new_range.remove(start_range)
#             except KeyError:
#                 pass

#         if a <= c and d <= b:
#             # Split segment into two by removing range from middle.
#             # New segments are (a, c-1) and (d+1, b)
#             print("This is a split scenario")
#             remove()
#             new_range.add(tuple((a, c - 1)))
#             new_range.add(tuple((d + 1, b)))
#         elif c <= a and b <= d:
#             # Completely remove segment from working range.
#             print("Completely remove segment")
#             remove()
#         elif b <= d and a <= c and c <= b:
#             # Upper part of segment overlaps with lower part of transform.
#             # New segment is (a, c-1)
#             print("Upper part of segment overlaps with lower part of transform")
#             remove()
#             new_range.add(tuple((a, c - 1)))
#         elif c <= a and b <= d and a <= d:
#             # Lower part of segment overlaps with upper part of transform.
#             # New segment is (d+1, b)
#             print("Lower part of segment overlaps with upper part of transform")
#             remove()
#             new_range.add(tuple((d + 1, b)))
#         else:
#             print("No change")

#         self.working_range = set([r for r in new_range if r[0] <= r[1]])

#     def _add_to_range(self, start_range: tuple, transform_range: tuple) -> None:
#         new_range = copy.copy(self.working_range)
#         # for segment in self.working_range:
#         a = start_range[0]
#         b = start_range[1]
#         c = transform_range[0]
#         d = transform_range[1]

#         print(f"Adding {transform_range} to segment", start_range)

#         def remove():
#             try:
#                 new_range.remove(start_range)
#             except KeyError:
#                 pass

#         if a <= c and d <= b:
#             print("No change")
#             # No change, transform sits within existing segment.
#             pass
#         elif c <= a and b <= d:
#             # Replace segment with transfer, (c, d)
#             print("Replace segment with transform")
#             remove()
#             new_range.add(tuple((c, d)))
#         elif b <= d and a <= c and c <= b:
#             # Upper part of segment overlaps with lower part of transform.
#             # New segment is (a, d)
#             print("Upper part of segment overlaps with lower part of transform")
#             remove()
#             new_range.add(tuple((a, d)))
#         elif c <= a and b <= d and a <= d:
#             # Lower part of segment overlaps with upper part of transform.
#             # New segment is (c, b)
#             print("Lower part of segment overlaps with upper part of transform")
#             remove()
#             new_range.add(tuple((c, b)))
#         else:
#             # If there is no overlap, just add the new segment.
#             print("No overlap, just add new segment")
#             new_range.add(tuple((c, d)))

#         self.working_range = set([r for r in new_range if r[0] <= r[1]])

#     def _consolidate_segments(self):
#         consolidated_range = copy.copy(self.working_range)
#         return consolidated_range

#     def get_minimum_value(self) -> int:
#         return 0


# def ranges_overlap(first: tuple, second: tuple) -> tuple:
#     """Given two tuples (a, b) and (c, d), there are three possible overlap scenarios.
#     1. No overlap. This occurs if when (b < c AND d < a).
#     2. Partial overlap. This occurs when (b < d AND a < c AND c < b) OR (c < a AND b < d AND a < d).
#     3. Complete overlap. This occurs when (a < c AND d < b) OR (c < a AND b < d).

#     Args:
#         first (tuple): A tuple specifying a range starting at "a" and ending at "b".
#         second (tuple): A tuple specifying a range starting at "c" and ending at "d".

#     Returns:
#         tuple: The overlaping range (x, y) starting at "x" and ending at "y".
#     """

#     overlap = ()

#     # I find it easier to think about it this way, with the docstring above!
#     a = first[0]
#     b = first[1]
#     c = second[0]
#     d = second[1]

#     if a < c and d < b:
#         overlap = (c, d)
#     elif c < a and b < d:
#         overlap = (a, b)
#     elif b < d and a < c and c < b:
#         overlap = (c, b)
#     elif c < a and b < d and a < d:
#         overlap = (a, d)

#     return overlap


# def go(data):
#     data = sample_data

#     raw_mapping = [m for m in data.splitlines()[2:]]
#     mappings = dict()
#     for index, line in enumerate(raw_mapping):
#         if line.endswith("map:"):
#             start_position = line.split("-")[0]
#             mappings[start_position] = dict()

#             target_position = line.split("-")[2].split()[0]
#             mappings[start_position]["target"] = target_position
#             mappings[start_position]["maps"] = []

#             current_mapping = True

#             while current_mapping and index < len(raw_mapping) - 1:
#                 index += 1
#                 if raw_mapping[index] == "":
#                     current_mapping = False
#                     break
#                 destination_range_start, source_range_start, range_length = [
#                     int(r) for r in raw_mapping[index].split()
#                 ]
#                 mapping = Mapping(
#                     destination_range_start, source_range_start, range_length
#                 )

#                 mappings[start_position]["maps"].append(mapping)

#     seeds = [int(s) for s in data.splitlines()[0].split()[1:]]
#     seed_pairs = []

#     for i in range(0, len(seeds), 2):
#         seed_pairs.append(seeds[i : i + 2])

#     locations = []

#     for pair in seed_pairs:
#         print("\n===========================")
#         print("Working on pair:", pair)
#         print("===========================")

#         r = Range(start_value=pair[0], length=pair[1])

#         current_position = "seed"
#         while current_position != "location":
#             for m in mappings[current_position]["maps"]:
#                 print("BEFORE:", r.working_range)
#                 r.transform(mapping=m)
#                 print("AFTER:", r.working_range)
#                 print("===========================")
#             current_position = mappings[current_position]["target"]

#         print(r.working_range)
#         locations.append(r.get_minimum_value())

#     answer = min(locations)
#     print("\nANSWER:", answer)
#     return answer
#     # test_range = Range(start_value=3, length=8)
#     # test_transform = Mapping(12, 3, 2)
#     # # Expected result: (3,10) -> (5,10),(12,13)
#     # print("Test range start:", test_range.working_range)

#     # test_range.transform(test_transform)

#     # print("Test range finish:", test_range.working_range)


def go(data):
    """This is Richard Clark's answer. I wasn't able to solve it using the above,
    though I think I was on the right track, sort of.
    """
    import re
    from intervaltree import IntervalTree, Interval

    lines = data.split("\n")
    seed_numbers = [int(x) for x in lines[0].split(":")[1].split()]

    # Get the seeds as start,end pairs
    seeds = IntervalTree(
        [
            Interval(start, start + length)
            for start, length in zip(seed_numbers[::2], seed_numbers[1::2])
        ]
    )

    # Collect the mappings as interval trees with the offset as the data value of each interval
    maps = []

    for line in lines[2:]:
        if line == "":
            continue
        m = re.match(r"(\w+)-to-(\w+) map:", line)
        if m:
            current_map = IntervalTree()
            maps.append(current_map)
        else:
            destination_start, source_start, length = [int(x) for x in line.split()]
            current_map[source_start : source_start + length] = (
                destination_start - source_start
            )

    # For each map, take the current seeds and add their intervals to the map intervals, then use split_overlaps to
    # make a set of intervals where the map and seed intervals are split up to match. Then it's a trivial matter of
    # iterating through the intervals and determining whether there's a pair of seed and map intervals (then map them)
    # or a solo seed interval (copy across untransformed)
    for m in maps:
        interim = m.union(seeds)
        interim.split_overlaps()
        seeds = IntervalTree()

        for iv in interim:
            n_matches = len(interim[iv.begin : iv.end])
            if iv.data is not None:
                if n_matches > 1:
                    seeds.add(Interval(iv.begin + iv.data, iv.end + iv.data))
            else:
                if n_matches == 1:
                    seeds.add(iv)

    # Find the lowest starting value of the transformed intervals
    answer = min(s.begin for s in seeds)
    print(answer)
    return answer
