def find_anti_nodes(area, char, x_cord, y_cord):
    antinodes = set()

    # Search every point in the area for matching characters
    for y, line in enumerate(area):
        for x, val in enumerate(line):
            # if a matching char is found
            if val == char and x != x_cord and y != y_cord:
                # print(f"matching char found at {x} {y}")
                # calculate the step between points
                dx = x - x_cord
                dy = y - y_cord

                node = (x + dx, y + dy)
                # print(f"potential node found at {node}")
                # if the antinode is within the bounds of area
                if 0 <= node[0] < len(area) and 0 <= node[1] < len(area[0]):
                    # if the distance of the anti node is twice as far from the further antenna
                    if node[0] - (dx * 2) == x_cord and node[1] - (dy * 2) == y_cord:
                        antinodes.add(node)
                    else:
                        pass
                        # print("2:1 ratio check failed")
                else:
                    pass
                    # print("Node exceeds bounds")
    # print(f"{len(antinodes)} antinodes found\n")
    return antinodes


def task1():
    with open("inputs/file8.txt", 'r') as file:
        area = [list(line.strip()) for line in file]

    antinodes = set()
    # Search each line in the file for any non . character
    for y_cord, line in enumerate(area):
        for x_cord, char in enumerate(line):
            # if char != ".":
            if char != '.':
                # print(f"finding o antinode at {x_cord}, {y_cord}")
                nodes = find_anti_nodes(area, char, x_cord, y_cord)
                for node in nodes:
                    antinodes.add(node)
    """
    for x, y in antinodes:
        area[y][x] = "#"
    for line in area:
        print("".join(line))
    """
    return len(antinodes)


def find_anti_nodes2(area, char, x_cord, y_cord):
    antinodes = set()

    # Search every point in the area for matching characters
    for y, line in enumerate(area):
        for x, val in enumerate(line):
            # if a matching char is found and the antenna is not refering to itself
            if val == char and x != x_cord and y != y_cord:
                print(f"matching char found at {x} {y}")
                # calculate the step between points

                x_step = (x - x_cord)
                y_step = (y - y_cord)

                print(f"{x_step} {y_step}")

                x = x + x_step
                y = y + y_step
                while 0 <= x < len(area[0]) and 0 <= y < len(area):
                    print(f"new node attempting to be added at {x} {y}")
                    node = (x, y)
                    antinodes.add(node)
                    x = x + x_step
                    y = y + y_step
                    print(f"{x} {y}, current bounds are {len(area)}, {len(area[0])}")
                print("bounds")
    print(f"{len(antinodes)} antinodes found\n")
    return antinodes

def task2():
    with open("inputs/file8.txt", 'r') as file:
        area = [list(line.strip()) for line in file]

    antinodes = set()
    # Search each line in the file for any non . character
    for y_cord, line in enumerate(area):
        for x_cord, char in enumerate(line):
            if char != '.':
                print(f"finding antinodes for {x_cord} {y_cord}")
                nodes = find_anti_nodes2(area, char, x_cord, y_cord)
                for node in nodes:
                    antinodes.add(node)

    for x, y in antinodes:
        area[y][x] = "#"
    for line in area:
        print("".join(line))

    return len(antinodes)



def main():
    print(task1())
    print(task2())


if __name__ == '__main__':
    main()
