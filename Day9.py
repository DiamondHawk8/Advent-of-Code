from time import sleep


def get_uncompressed():
    with open("inputs/file9.txt", "r") as f:
        data = list(f.read().strip())

    free_space = False
    id = 0
    uncompressed = []
    for val in data:

        if free_space:
            free_space = False
            uncompressed += ['.'] * int(val)
        else:
            free_space = True
            uncompressed += [id] * int(val)
            id += 1
    # returns uncompressed data and number of file ids
    return uncompressed, id


def checksum(disk):
    total = 0
    prevval = 0
    previndex = -1
    for index, val in enumerate(disk):
        if val != '.':
            print(f"multiplying {val} by {index}")
            if val == prevval and previndex != index-1:
                print("CRITICAL ERROR")
                break
            total += int(val) * index
        prevval = val
        previndex = index
    return total


def task1():
    uncompressed = get_uncompressed()[0]
    for index, val in enumerate(uncompressed):
        # print(f"checking val {val} at index {index}")
        if val == '.':
            # Ensure no free memory is being moved
            mov = uncompressed.pop()
            while mov == '.':
                mov = uncompressed.pop()
                continue
            uncompressed[index] = mov

    return checksum(uncompressed)


def task2():
    data, ids = get_uncompressed()

    # For every file id in descending order
    for num in reversed(range(ids)):
        print(f"On num {num} of {ids}")
        # get all indexes of said file
        if num not in data:  # or: if any(x == num for x in data):
            continue  # skip this file entirely, it has zero blocks or it doesn't exist
        indexes = [i for i, value in enumerate(data) if value == num]

        # Search for empty space in the area preceding the file section
        size = 0
        for index, val in enumerate(data[:data.index(num)]):
            # determine if there is a space large enough to house to file
            if val == '.':
                size += 1
            else:
                # if a large enough space is found, shift the values over to the empty slots
                if size >= len(indexes):
                    # Decrement index so that it refers to the preceding empty space
                    index = index - 1
                    # Offset to the beginning depending on if there is extra space
                    offset = size - len(indexes)

                    for i in indexes:
                        data[i] = '.'
                        data[index - offset] = num
                        index -= 1
                    break
                size = 0
    return checksum(data)


def main():
    pass
    # print(task1())
    # print(task2())


if __name__ == '__main__':
    main()
