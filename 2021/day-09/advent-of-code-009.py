class Basin:
    def __init__(self, coords):
        self.coords = coords

class Floor:
    def __init__(self, map):
        self.map = map
        self.max_height = len(self.map) - 1
        self.max_width = len(self.map[0]) - 1


    def is_lowest(self, x, y):
        adjacent = self.get_adjacent(x, y)
        value = self.value(x, y)
        return value < min([self.value(a[0],a[1]) for a in adjacent])


    def get_adjacent(self, x, y):
        adjacent = []

        # Get values above and below.
        # Check whether value is in top or bottom row, otherwise take values above and below.
        if y == 0:
            adjacent.append((x, y+1))
        elif y == self.max_height:
            adjacent.append((x, y-1))
        else:
            adjacent.append((x, y+1))
            adjacent.append((x, y-1))

        # Get values left and right.
        # Check whether value is far left or far right, otherwise take both left and right.
        if x == 0:
            adjacent.append((x+1, y))
        elif x == self.max_width:
            adjacent.append((x-1, y))
        else:
            adjacent.append((x+1, y))
            adjacent.append((x-1, y))

        return adjacent

    
    def value(self, x, y):
        value = int(self.map[y][x])
        return value


    @property
    def lowest_points(self):
        points = []

        for y in range(self.max_height + 1):
            for x in range(self.max_width + 1):
                if self.is_lowest(x, y):
                    points.append((x, y))

        return points

    
    @property
    def basins(self):
        basins = []
        # lowest_points = self.lowest_points.copy()
        lowest_points = [self.lowest_points[0], self.lowest_points[1], self.lowest_points[2]].copy()

        for point in lowest_points:
            coords_to_search = [point]
            basin_coords = []
            searched = []
            while len(coords_to_search) > 0:
                next_coords_to_search = []

                for coord in coords_to_search:
                    if self.value(coord[0],coord[1]) < 9 and coord not in searched:
                        searched.append(coord)
                        basin_coords.append(coord)
                        next_coords_to_search = self.get_adjacent(coord[0],coord[1])
                    else:
                        searched.append(coord)

                coords_to_search = next_coords_to_search

                basins.append(basin_coords)

        print(basins)

        return basins
        


def get_floor_map_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        content = [line.strip("\n") for line in content]
        return content


def part_one():
    floor = Floor(get_floor_map_from_file())

    height = len(floor.map)
    width = len(floor.map[0])

    total_risk_level = 0

    for y in range(height):
        for x in range(width):
            if floor.is_lowest(x, y):
                total_risk_level = total_risk_level + 1 + floor.value(x, y)
    
    print("Answer", total_risk_level)


def part_two():
    floor = Floor(get_floor_map_from_file())

    basins = floor.basins
    
    

if __name__ == "__main__":
    # part_one()
    part_two()