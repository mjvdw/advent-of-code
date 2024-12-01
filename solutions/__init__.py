import importlib


def solve(year, day, data):
    mod_name = f"solutions.aoc{year}.day{day}"
    mod = importlib.import_module(mod_name)
    a = mod.part_a(data)
    b = mod.part_b(data)
    return a, b
