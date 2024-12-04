def part_one():
    coords = []
    count = 0

    with open('puzzle-input.txt') as f:
        coords_str = f.readlines()
        for c in coords_str:
            coords.append(c.strip("\n"))        

    for n in range(len(coords)-1):
        previous = int(coords[n])
        current = int(coords[n+1])

        difference = current-previous

        if difference > 0:
            count = count + 1

    print("Answer:", count)


def part_two():
    coords = []
    count = 0

    with open('puzzle-input.txt') as f:
        coords_str = f.readlines()
        for c in coords_str:
            coords.append(int(c.strip("\n")))        

    for n in range(len(coords)-3):
        window_pair = [0,0]
        for i in range(2):
            first = coords[n+i]
            second = coords[n+1+i]
            third = coords[n+2+i]
            sum = first + second + third
            window_pair[i] = sum

        difference = window_pair[1] - window_pair[0]
        
        if difference > 0:
            count = count + 1

    print("Answer:", count)


if __name__ == "__main__":
    part_one()
    part_two()