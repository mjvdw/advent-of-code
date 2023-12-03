import os
import importlib
import click
from aocd import get_data, submit
from rich.console import Console


@click.command
@click.argument("year")
@click.argument("puzzle_code")
@click.option("--send", default=False, help="Whether to submit the answer to AOCD")
def run(year: int, puzzle_code: str, send: bool):
    year = 2023
    day = int(puzzle_code[0:-1])
    part = puzzle_code[-1]

    data = get_data(
        session=os.getenv("AOC_SESSION"),
        year=year,
        day=day,
    )

    c = Console()
    c.rule(f"Advent of Code {year}-{day}{part}")
    ####################################################################################

    working = importlib.import_module(f"{year}.day_{day:02d}{part}")
    answer = working.go(data)

    ####################################################################################
    c.rule("Finished")

    if send:
        submit(year=year, day=day, part=part, answer=answer)


if __name__ == "__main__":
    run()
