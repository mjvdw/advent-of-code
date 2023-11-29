# Advent of Code 2023

This project uses the code in `main.py` to abstract away from the admin of getting and parsing the input for each puzzle, as well as then submitting the code.

To use this approach:

1. create python files corresponding to the day and part you are working on (this assumes you're working on 2023, but if you change the `year` variable in `main.py` you can use this for any year),
   - This should be in the format `day_NNNa.py` and in the `working` folder.
   - For example, day 3 part b would be `day_003b.py` and day 15 part a would be `day_015a.py`.
2. you can run this working file through the automation using Click. Run `python3 main.py 1a` to run your `day_001a.py` file (for example).
3. when you're ready to submit your answer, you can add the `--send` option to your command.
