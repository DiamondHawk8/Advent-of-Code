def task1():
    total = 0
    with open("file2.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            safe = True

            for i in range(len(levels) - 1):
                diff = levels[i + 1] - levels[i]
                if not (1 <= diff <= 3 or -3 <= diff <= -1):
                    safe = False
                    break

            if safe:
                increasing = all(levels[i + 1] > levels[i] for i in range(len(levels) - 1))
                decreasing = all(levels[i + 1] < levels[i] for i in range(len(levels) - 1))
                if not (increasing or decreasing):
                    safe = False

            if safe:
                total += 1
    print(total)


def task2():
    safe_count = 0
    with open("file2.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))

            def is_safe(report):
                for i in range(len(report) - 1):
                    diff = report[i + 1] - report[i]
                    if not (1 <= diff <= 3 or -3 <= diff <= -1):
                        return False
                increasing = all(report[i + 1] > report[i] for i in range(len(report) - 1))
                decreasing = all(report[i + 1] < report[i] for i in range(len(report) - 1))
                return increasing or decreasing

            if is_safe(levels):
                safe_count += 1

            else:
                # cehck if removing one level makes it safe
                for i in range(len(levels)):
                    modified_levels = levels[:i] + levels[i + 1:]
                    if is_safe(modified_levels):
                        safe_count += 1
                        break

    print(safe_count)


def task1_test():
    total = 0
    # split the inputs
    with open("file2.txt", "r") as file:
        for line in file:
            cleaned = list(map(int, line.split()))
            if check_is_safe(cleaned):
                total += 1
    print(total)


def check_is_safe(line):
    pos = False
    neg = False
    for i in range(len(line)-1):
        diff = line[i+1] - line[i]
        if 1 <= diff <= 3:
            pos = True
        elif -3 <= diff <= -1:
            neg = True
        else:
            return False
    return pos ^ neg

def task2_test():
    total = 0
    # split the inputs
    with open("file2.txt", "r") as file:
        for line in file:
            cleaned = list(map(int, line.split()))
            if check_is_safe(cleaned):
                total += 1
            else:
                for i in range(len(cleaned)):
                    newlist = cleaned[:i] + cleaned[i+1:]
                    if check_is_safe(newlist):
                        total += 1
                        break
    print(total)



def main():
    task1()
    task2()
    task1_test()
    task2_test()


if __name__ == "__main__":
    main()

