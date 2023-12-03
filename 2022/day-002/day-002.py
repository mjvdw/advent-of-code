def open_input(filename):
    raw_data = ""
    with open(filename) as file:
        raw_data = file.read()

    data = raw_data.split("\n")

    return data


def get_outcome(game):
    result = ""

    if game == "A X" or game == "B Y" or game == "C Z":
        result = "draw"
    elif game == "A Y" or game == "B Z" or game == "C X":
        result = "win"
    else:
        result = "lose"

    return result


def get_move(game):
    result = game[2]
    opponent_move = game[0]
    your_move = ""

    if result == "Z":  # win
        if opponent_move == "A":
            your_move = "B"
        elif opponent_move == "B":
            your_move = "C"
        else:
            your_move = "A"
    elif result == "Y":  # draw
        your_move = opponent_move
    else:  # lose
        if opponent_move == "A":
            your_move = "C"
        elif opponent_move == "B":
            your_move = "A"
        else:
            your_move = "B"

    return your_move


def part_one(data):
    total_score = 0

    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "win": 6,
        "draw": 3,
        "lose": 0
    }

    for game in data:
        outcome = get_outcome(game)
        score = scores[game[2]] + scores[outcome]
        total_score += score

    return total_score


def part_two(data):
    total_score = 0

    scores = {
        "X": 0,
        "Y": 3,
        "Z": 6,
        "A": 1,
        "B": 2,
        "C": 3
    }

    for game in data:
        move = get_move(game)
        score = scores[game[2]] + scores[move]
        print(score)
        total_score += score

    return total_score


if __name__ == "__main__":
    input_file = "input.txt"
    data = open_input(input_file)

    # answer_one = part_one(data)
    # print(answer_one)
    # ANSWER 1: 12679

    answer_two = part_two(data)
    print(answer_two)
    # ANSWER 2: 15387 - too high
