import os
import importlib
import click
from aocd import get_data, submit
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()


@click.command
@click.argument("day", type=int)
@click.option("--year", default=2024, help="Which year's puzzles you are referencing")
@click.option("--send", default=False, help="Whether to submit the answer to AOCD")
def run(day: int, year: int, send: bool):
    data = get_data(
        session=os.getenv("AOC_SESSION"),
        year=year,
        day=day,
    )

    c = Console()
    c.rule(f"Advent of Code {year}-{day}")
    ####################################################################################

    working = importlib.import_module(f"{year}.day_{day:02d}")
    answer = working.go(data)

    ####################################################################################
    c.rule("Finished")

    if send:
        submit(year=year, day=day, answer=answer)


if __name__ == "__main__":
    run()
