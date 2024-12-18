def task1():
    with open("inputs/file4.txt", "r") as file:
        total = 0
        arr = []
        for line in file:
            data = list(line.strip())
            arr.append(data)

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        pattern = ["X", "M", "A", "S"]

        for row_idx in range(len(arr)):
            for col_idx in range(len(arr[row_idx])):

                if not arr[row_idx][col_idx] == pattern[0]:
                    continue

                valid_directions = []
                for vertical_direction, horizontal_direction in directions:
                    new_row = row_idx + vertical_direction
                    new_col = col_idx + horizontal_direction

                    # Add direction if the next step is within bounds
                    if 0 <= new_row < len(arr) and 0 <= new_col < len(arr[0]):
                        valid_directions.append((vertical_direction, horizontal_direction))

                # Iterate the number of times equal to valid direcitons, once for each direction, 3 times in each
                # direction, breaking if pattern isnt matching

                for vertical_direction, horizontal_direction in valid_directions:
                    current_pattern = []
                    for x in range(4):
                        new_row = row_idx + vertical_direction * x
                        new_col = col_idx + horizontal_direction * x

                        # Second check
                        if not (0 <= new_row < len(arr) and 0 <= new_col < len(arr[0])):
                            break

                        current_pattern.append(arr[new_row][new_col])
                    if current_pattern == pattern:
                        total += 1

        return total


def task2():
    with open("inputs/file4.txt", "r") as file:
        arr = [list(line.strip()) for line in file]

    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0

    # check if a diagonal matches 
    def check_diagonal(a, b, c):
        return (a == 'M' and b == 'A' and c == 'S') or (a == 'S' and b == 'A' and c == 'M')

    total = 0

    # need at least a 3x3 area around the center cell
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if arr[r][c] != 'A':
                continue
            tl = arr[r - 1][c - 1]
            tr = arr[r - 1][c + 1]
            bl = arr[r + 1][c - 1]
            br = arr[r + 1][c + 1]

            # check  diagonals
            diagonal1_valid = check_diagonal(tl, 'A', br)
            diagonal2_valid = check_diagonal(bl, 'A', tr)

            if diagonal1_valid and diagonal2_valid:
                total += 1

    return total


def main():
    print(task2())


if __name__ == '__main__':
    main()
