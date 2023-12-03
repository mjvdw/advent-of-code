# Advent of Code

This project uses the code in `main.py` to abstract away from the admin of getting and parsing the input for each puzzle, as well as then submitting the code.

To use this approach:

1. create python files corresponding to the day and part you are working on in an appropriate year folder.
   - This should be in the format `day_NNa.py` and in the relevant year folder.
   - For example, day 3 part b would be `day_03b.py` and day 15 part a would be `day_15a.py`.
2. you can run this working file through the automation using Click. Run `python3 main.py 2023 1a` to run your `day_01a.py` file for 2023 (for example).
3. when you're ready to submit your answer, you can add the `--send=True` option to your command.
