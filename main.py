import os
import importlib.util
import sys
import click
from aocd import get_data, submit
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()


@click.command()
@click.argument("day", type=int)
@click.option("--year", default=2025, help="Which year's puzzles you are referencing")
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

    # Load module from file path since year directories start with numbers
    module_path = os.path.join(
        os.path.dirname(__file__), str(year), f"day_{day:02d}.py"
    )
    spec = importlib.util.spec_from_file_location(f"day_{day:02d}", module_path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError(f"Could not find solution file: {module_path}")
    working = importlib.util.module_from_spec(spec)
    sys.modules[f"day_{day:02d}"] = working
    spec.loader.exec_module(working)

    answer = working.go(data)

    ####################################################################################
    c.print(f"\n[bold green]Answer:[/bold green] {answer}\n")
    c.rule("Finished")

    if send:
        submit(year=year, day=day, answer=answer)


if __name__ == "__main__":
    run()
