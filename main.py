import importlib
import click
from aocd import get_data, submit
from rich.console import Console




@click.command
@click.argument("puzzle_code")
@click.option('--send', default=False, help="Whether to submit the answer to AOCD")
def run(puzzle_code: str, send):
    year = 2023
    day = int(puzzle_code[0:-1])
    part = puzzle_code[-1]

    c = Console()
    data = get_data(year=year, day=day)
    c.rule(f"Advent of Code {year}-{day}{part}")
    ####################################################################################
    
    working = importlib.import_module(f"working.day_{day:03d}{part}")
    answer = working.go(data)

    ####################################################################################
    c.rule("Finished")

    if send:
        submit(year=year, day=day, part=part, answer=answer)


if __name__ == "__main__":
    run()