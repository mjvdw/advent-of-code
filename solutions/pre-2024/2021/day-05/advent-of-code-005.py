class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_all_coords(self):
        all_coords = []

        if self.x1 == self.x2:
            # This means line is vertical.
            # Therefore equation is x = x1 = x2
            x = self.x1
            start_y = min(self.y1, self.y2)
            end_y = max(self.y1, self.y2)
            for i in range(start_y, end_y+1):  # Plus 1 to make sure that coordinate is actually included.
                all_coords.append({
                    "x": x,
                    "y": i
                })
        elif self.y1 == self.y2:
            # This means line is horizontal.
            # Therefore equation is y = y1 = y2 = c
            y = self.y1
            start_x = min(self.x1, self.x2)
            end_x = max(self.x1, self.x2)
            for i in range(start_x, end_x+1):  # Plus 1 to make sure that coordinate is actually included.
                all_coords.append({
                    "x": i,
                    "y": y
                })
        else:
            # Line must be at 45 degrees (question parameter)
            # Assume line always goes left to right.

            if self.x1 < self.x2:
                start_x = self.x1
                start_y = self.y1
                trending_up = True if self.y2 > self.y1 else False
            else:
                start_x = self.x2
                start_y = self.y2
                trending_up = True if self.y2 < self.y1 else False

            steps = abs(self.y2 - self.y1)   # This could also be x, since line is always 45 degrees.

            for i in range(steps+1): 
                coord = {
                    "x": start_x + i,
                    "y": start_y + i if trending_up else start_y - i
                }
                # print(coord)
                all_coords.append(coord)

        return all_coords


def get_coords():
    lines = []

    with open("puzzle-input.txt") as f:
        content = f.readlines()
        for line in content:
            start_coords = line.split("->")[0]
            end_coords = line.split("->")[1]
            
            x1 = int(start_coords.split(",")[0])
            y1 = int(start_coords.split(",")[1])
            x2 = int(end_coords.split(",")[0])
            y2 = int(end_coords.split(",")[1])

            lines.append(Line(x1, y1, x2, y2))
    
    return lines


def get_empty_grid(lines):
    max_x = 0
    max_y = 0

    for line in lines:
        if line.x1 > max_x:
            max_x = line.x1
        elif line.y1 > max_y:
            max_y = line.y1
        elif line.x2 > max_x:
            max_x = line.x2
        elif line.y2 > max_y:
            max_y = line.y2

    grid = []
    for i in range(max_y + 1):
        grid_cols = [0] * (max_x + 1)   # Plus 1 because max_x is the largest index, not the length.
        grid.append(grid_cols)

    return grid


def count_overlaps_more_than_two(grid):
    count = 0

    for row in grid:
        for n in row:
            if n >= 2:
                count += 1

    return count


def part_one():
    lines = get_coords()
    grid = get_empty_grid(lines)

    for line in lines:
        if line.x1 == line.x2 or line.y1 == line.y2:
            coords = line.get_all_coords()
            for coord in coords:
                x = coord["x"]
                y = coord["y"]
                grid[y][x] += 1

    answer = count_overlaps_more_than_two(grid)

    print("Answer", answer)


def part_two():
    lines = get_coords()
    grid = get_empty_grid(lines)

    for line in lines:
        coords = line.get_all_coords()
        for coord in coords:
            x = coord["x"]
            y = coord["y"]
            grid[y][x] += 1
    
    answer = count_overlaps_more_than_two(grid)
    print("Answer", answer)


if __name__ == "__main__":
    part_one()
    part_two()