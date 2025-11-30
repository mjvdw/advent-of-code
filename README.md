# Advent of Code

This project uses the [AOCD](https://github.com/wimglenn/advent-of-code-data) and [advent-of-code-sample](https://github.com/wimglenn/advent-of-code-sample/blob/master/README.md) approach.

## Installation

1. Clone into this repo locally.
2. Install [uv](https://docs.astral.sh/uv/) if you haven't already: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. `cd` into the folder and run `uv sync` to install dependencies.
4. Write your code in the relevant year folder in the solution folder.
5. Submit by running `uv run aoc --years 2024 --days 1 2 3`.

## Running Solutions

To run a specific day's solution:

```bash
uv run aoc-run <day> --year <year>
```

To submit your answer automatically:

```bash
uv run aoc-run <day> --year <year> --send
```

Example:

```bash
uv run aoc-run 1 --year 2024
```
