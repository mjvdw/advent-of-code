class Vertex:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    @property
    def above(self):
        pass


def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        grid_raw = [x.strip("\n") for x in content]
        
        grid = []
        for y in range(len(grid_raw)):
            row = []
            for x in range(len(grid_raw[0])):
                row.append(Vertex(x=x, y=y, value=grid_raw[y][x]))
            grid.append(row)

        return grid


def part_one():
    grid = get_content_from_file()

    for row in grid:
        print(row)


if __name__ == "__main__":
    part_one()