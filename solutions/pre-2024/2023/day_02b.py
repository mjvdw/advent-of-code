sample_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


class Game(object):
    def __init__(self, id: int, red: [int], blue: [int], green: [int]):
        self.id = id
        self.red = red
        self.blue = blue
        self.green = green


def go(data):
    # data = sample_data

    data = data.splitlines()
    parsed = []

    # Parse data.
    for line in data:
        id = 0
        num_red = [0]
        num_blue = [0]
        num_green = [0]

        id = int(line.split(":")[0].split(" ")[1])

        draws = [d.strip().split(",") for d in line.split(":")[1].split(";")]

        for draw in draws:
            for colour in draw:
                colour = colour.strip()
                num = int(colour.split(" ")[0])
                name = colour.split(" ")[1]

                if name == "red":
                    num_red.append(num)
                elif name == "blue":
                    num_blue.append(num)
                elif name == "green":
                    num_green.append(num)
                else:
                    print("There's a fourth colour that doesn't seem to match.")

        parsed.append(Game(id=id, red=num_red, blue=num_blue, green=num_green))

    answer = 0

    # Filter valid games.
    for game in parsed:
        power = max(game.red) * max(game.blue) * max(game.green)
        answer += power

    print(answer)
    return answer
