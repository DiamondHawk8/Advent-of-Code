import re


def task1():
    total = 0
    pattern = r"mul\((\d+),(\d+)\)"
    with open("inputs/file3.txt", "r") as file:
        for line in file:
            matches = re.findall(pattern, line)
            numbers = [(int(x), int(y)) for x, y in matches]
            for tup in numbers:
                total = total + mult(tup)
    return total

def mult(tup):
    return tup[0] * tup[1]



def task2():
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)"
    total = 0
    is_enabled = True
    with open('inputs/file3.txt', 'r') as f:
        data = f.read()

    matches = re.finditer(pattern, data)
    for match in matches:
        s = match.group(0)
        if s == 'do()':
            is_enabled = True
        elif s == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                m = re.match(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", s)
                if m:
                    x, y = int(m.group(1)), int(m.group(2))
                    total += x * y
    return total

def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
