class Instruction:
    def __init__(self, direction, fold_line):
        self.direction = direction
        self.fold_line = fold_line


class Grid:
    def __init__(self, coords):
        self.coords = coords
        self.grid = self.generate_grid_from_coords()

    def generate_grid_from_coords(self):
        grid = []
        row = ["."] * (self.max_width + 1)
        for i in range(self.max_height + 1):
            grid.append(row.copy())

        for coord in self.coords:
            grid[coord[0]][coord[1]] = "#"

        return grid
    
    def print_grid(self):
        grid = self.generate_grid_from_coords()
        grid = list(zip(*grid[::-1]))

        printable_grid = []
        for y in range(self.min_height, self.max_height + 1):
            row_str = ""
            for x in range(self.min_width, self.max_width + 1):
                row_str += grid[x][y]
            printable_grid.append(row_str)
        
        for row in printable_grid:
            print(row)


    def count_dots(self):
        coords_as_tuples = [(i[0],i[1]) for i in self.coords]
        unique = list(dict.fromkeys(coords_as_tuples))
        count = len(list(unique))
        return count


    def fold(self, instruction):
        coord_index = 0 if instruction.direction == "x" else 1

        for i in range(len(self.coords)):
            value = self.coords[i][coord_index]
            if value > instruction.fold_line:
                new_value = value - (2 * (value - instruction.fold_line))
                self.coords[i][coord_index] = new_value
    
    @property
    def max_height(self):
        height = []
        for coord in self.coords:
            height.append(coord[0])
        
        return max(height)

    @property
    def max_width(self):
        width = []
        for coord in self.coords:
            width.append(coord[1])
        
        return max(width)

    @property
    def min_height(self):
        height = []
        for coord in self.coords:
            height.append(coord[0])
        
        return min(height)

    @property
    def min_width(self):
        width = []
        for coord in self.coords:
            width.append(coord[1])
        
        return min(width)


def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        content = [x.strip("\n") for x in content]

        split_index = content.index("")

        coords_raw = content[:split_index]
        coords = [[int(x.split(",")[0]),int(x.split(",")[1])] for x in coords_raw]
        grid = Grid(coords)

        instructions_raw = content[split_index:]
        instructions_raw.pop(0)
        instructions = []
        for i in instructions_raw:
            i = i.strip("fold along ")
            direction = i[0]
            coord = int(i.split("=")[1])
            instructions.append(Instruction(direction, coord))

        return grid, instructions


def part_one():
    grid, instructions = get_content_from_file()

    for instruction in instructions:
        grid.fold(instruction)
        visible_dots = grid.count_dots()
        print("Answer", visible_dots)
        break    # Break after first iteration just for part one


def part_two():
    grid, instructions = get_content_from_file()

    for instruction in instructions:
        grid.fold(instruction)
        
    grid.print_grid()
    # print(grid.coords)
    
    # Tried EFLFJQRF


if __name__ == "__main__":
    # part_one()
    part_two()