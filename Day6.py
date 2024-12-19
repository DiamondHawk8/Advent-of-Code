def task1():
    with open("inputs/file6.txt", "r") as file1:
        # Read the file into a 2d array
        area = [list(line.strip()) for line in file1]

        # up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # Starts facing up
        current_direction = 0

        # Find starting index
        for row_index, row in enumerate(area):
            for col_index, char in enumerate(row):
                if char == "^":
                    loc = (row_index, col_index)

        locations = {tuple(loc)}

        # Determine the next location of the guard
        next_loc = [x + y for x, y in zip(loc, directions[current_direction])]

        # While the guard is still in bounds
        while (next_loc[0] >= 0 and next_loc[1] >= 0) and (next_loc[0] < len(area) and next_loc[1] < len(area[0])):

            # If the next area is an obstacle
            if area[next_loc[0]][next_loc[1]] == "#":
                # Change directions 90 degrees
                current_direction = (current_direction + 1) % 4

            # Otherwise, add our current location to the set, and move forward
            else:
                locations.add(tuple(next_loc))
                loc = next_loc
            next_loc = [x + y for x, y in zip(loc, directions[current_direction])]

        return locations


def task2():
    with open("inputs/file6.txt", "r") as file1:
        # Read the file into a 2d array
        area = [list(line.strip()) for line in file1]

        # up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        positions = []

        total_iterations = len(area) * len(area[0])
        iterations = 0

        # loop through every location in the area, and place a #
        for row_index in range(len(area)):
            for space_index in range(len(area[row_index])):
                iterations += 1
                # Skip if obstacle exists or is starting location
                if area[row_index][space_index] in ("#", "^"):
                    continue

                # Create a copy of the area
                area_copy = [row[:] for row in area]

                area_copy[row_index][space_index] = "#"

                # Starts facing up
                current_direction = 0

                # Find starting index
                for r_index, row in enumerate(area_copy):
                    for col_index, char in enumerate(row):
                        if char == "^":
                            loc = (r_index, col_index)

                locations = set()

                # Determine the next location of the guard
                next_loc = [x + y for x, y in zip(loc, directions[current_direction])]

                while ((next_loc[0] >= 0 and next_loc[1] >= 0) and
                       (next_loc[0] < len(area_copy) and next_loc[1] < len(area_copy[0]))):

                    # If the next area is an obstacle
                    if area_copy[next_loc[0]][next_loc[1]] == "#":
                        # Change directions 90 degrees
                        current_direction = (current_direction + 1) % 4

                    # If the current location and the direction has already occurred, we are in a loop
                    else:
                        state = (tuple(next_loc), current_direction)
                        if state not in locations:
                            locations.add(state)
                        else:
                            positions.append((row_index, space_index))
                            break
                        loc = next_loc
                    next_loc = [x + y for x, y in zip(loc, directions[current_direction])]
                    print(f"Progress: {iterations}/{total_iterations}, {len(positions)} total loops found")
    return len(positions)


def main():
    reachable_positions = task1()

    # Todo, refactor code to use only reachable positions
    print(task2())


if __name__ == "__main__":
    main()
