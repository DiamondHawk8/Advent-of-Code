class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(f"{self.value}")


def read_data():
    topmap = []
    with open("inputs/file10.txt", 'r') as file:
        for line in file:
            layer = [Node(int(val)) for val in line.strip()]
            topmap.append(layer)
    return topmap


def task1():
    # Directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total_score = 0
    topmap = read_data()
    visited = set()

    # Search for trailheads and start BFS from them
    for x, row in enumerate(topmap):
        for y, node in enumerate(row):

            # If a new trailhead is found
            if node.value == 0:
                visited.add((x, y))
                queue = [(x, y)]
                score = 0
                # while there are unchecked moves
                while len(queue) > 0:

                    cx, cy = queue.pop(0)
                    current_node = topmap[cx][cy]
                    # check if the current node is the goal
                    if current_node.value == 9:
                        # if it is, move onto the next queue elements, and refresh which nodes have been visited
                        score += 1
                        visited = set()
                        continue
                    # check all neighbors
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        # ensure coords are valid
                        if 0 <= nx < len(topmap) and 0 <= ny < len(topmap[0]):
                            neighbor = topmap[nx][ny]

                            if not (nx, ny) in visited and neighbor.value == current_node.value+1:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
                total_score += score
    return total_score


# Same logic, only change being that visited nodes arent tracked
def task2():
    # Directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total_score = 0
    topmap = read_data()
    visited = set()

    # Search for trailheads and start BFS from them
    for x, row in enumerate(topmap):
        for y, node in enumerate(row):

            # If a new trailhead is found
            if node.value == 0:
                queue = [(x, y)]
                score = 0
                # while there are unchecked moves
                while len(queue) > 0:

                    cx, cy = queue.pop(0)
                    current_node = topmap[cx][cy]
                    # check if the current node is the goal
                    if current_node.value == 9:
                        # if it is, move onto the next queue elements, and refresh which nodes have been visited
                        score += 1
                        continue
                    # check all neighbors
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        # ensure coords are valid
                        if 0 <= nx < len(topmap) and 0 <= ny < len(topmap[0]):
                            neighbor = topmap[nx][ny]

                            if neighbor.value == current_node.value+1:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
                total_score += score
    return total_score





def main():
    print(task1())
    print(task2())


if __name__ == '__main__':
    main()
