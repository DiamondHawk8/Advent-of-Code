def evaluate_sequence(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops, start=1):
        if op == '+':
            result = result + numbers[i]
        elif op == '*':
            result = result * numbers[i]
        # modified for part 2
        else:
            result = int(str(result) + str(numbers[i]))
    return result


def all_operator_combinations(n):
    from itertools import product
    # modified for part 2
    return product(['+', '*', "||"], repeat=n - 1)


def task1():
    with open("inputs/file7.txt", "r") as f:
        lines = f.readlines()

    total_sum = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Parse the line
        target_str, nums_str = line.split(':')
        target = int(target_str.strip())
        numbers = list(map(int, nums_str.strip().split()))

        found_solution = False
        for ops in all_operator_combinations(len(numbers)):
            val = evaluate_sequence(numbers, ops)
            if val == target:
                found_solution = True
                break

        if found_solution:
            total_sum += target

    print(total_sum)


def main():
    task1()


if __name__ == '__main__':
    main()
