# Functions to extract data from text files into lists.
def get_numbers():
    with open('puzzle-input.txt') as f:
        content = f.readlines()
        numbers = content[0].split(",")
        numbers = list(map(lambda x : int(x), numbers))
        return numbers

def get_boards():
    with open('./puzzle-input.txt') as f:
        content = f.readlines()
        content.pop(0)   # numbers
        
        boards = []
        board = []
        for row in content:
            if row != "\n":
                row_list = []
                for i in [0,3,6,9,12]:
                    value = row[i] + row[i+1]
                    
                    # Number is represented by two values. The numbers itself, and a boolean
                    # indicating whether it's been called.
                    value = [int(value), False]
                    
                    row_list.append(value)

                board.append(row_list)
            else:
                boards.append(board)
                board = []

        boards.pop(0)   # Remove empty list at start

        return boards


# Play bingo!
def play_bingo(boards, number):
    for board in boards:
        for row in board:
            for value in row:
                if value[0] == number:
                    value[1] = True
                    
    return boards


# Function to check whether any of the current boards have won.
# Should return index of boards list of the winning board.
def check_for_winners(boards):
    winners = []

    success_criteria = [True, True, True, True, True]

    for board in boards:
        row_matches = False
        col_matches = False

        # Check rows
        for row in board:
            matches = [value[1] for value in row]
            if matches == success_criteria:
                row_matches = True        
                break

        # Check columns
        for i in range(5):
            matches = [row[i][1] for row in board]
            if matches == success_criteria:
                col_matches = True
                break
    
        if row_matches or col_matches:
            winners.append(board)

    return winners


# Function to calculate the score of a winning board.
def calculate_score(board, number):
    sum_of_unmatched = 0

    for row in board:
        for value in row:
            if value[1] == False:
                sum_of_unmatched += value[0]
    
    score = sum_of_unmatched * number

    return score


# PART ONE
def part_one():
    # Lists of random numbers and boards, using function above.    
    boards = get_boards()
    numbers = get_numbers()
    winning_board = []
    score = 0

    for number in numbers:
        print("Number", number)
        boards = play_bingo(boards, number)
        winners = check_for_winners(boards)   # Returns None if no winner.

        if winners:
            winning_board = winners[0]
            print(winning_board)
            score = calculate_score(winning_board, number)
            break
    
    print("Answer:", score)


# PART TWO
def part_two():
    # Lists of random numbers and boards, using function above.    
    boards = get_boards()
    numbers = get_numbers()
    score = 0
    winning_boards = []

    for number in numbers:
        boards = play_bingo(boards, number)
        winners = check_for_winners(boards)

        print(len(winning_boards), len(boards))
        if winners:
            for winner in winners:
                winning_boards.append([winner, number])
                boards.pop(boards.index(winner))

    print(winning_boards[-1])
    score = calculate_score(winning_boards[-1][0], winning_boards[-1][1])

    print("Answer:", score) 


if __name__ == "__main__":
    # part_one()
    part_two()