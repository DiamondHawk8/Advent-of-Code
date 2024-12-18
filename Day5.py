def task1():
    with open("file5a.txt", "r") as file1:
        rules = [line.strip().split("|") for line in file1]

    with open("file5b.txt", "r") as file2:
        instructions = [line.strip().split(",") for line in file2]

    def is_update_valid(update, rules):

        update_dict = {page: index for index, page in enumerate(update)}
        for x, y in rules:
            if x in update_dict and y in update_dict:
                if update_dict[x] > update_dict[y]:
                    return False
        return True

    # Identify valid updates
    valid_updates = []
    for update in instructions:
        if is_update_valid(update, rules):
            valid_updates.append(update)


    middle_pages = []
    for update in valid_updates:
        middle_page = update[len(update) // 2]
        middle_pages.append(int(middle_page))

    # Sum of middle pages
    result = sum(middle_pages)
    return result


def task2():
    with open("file5a.txt", "r") as file1:
        rules = [line.strip().split("|") for line in file1]

    with open("file5b.txt", "r") as file2:
        instructions = [line.strip().split(",") for line in file2]

    def reorder_update(update, rules):
        update_list = list(update)  # Make a mutable copy of the update
        changed = True
        changes = 0
        while changed:
            changed = False
            for x, y in rules:
                if x in update_list and y in update_list:
                    index_x = update_list.index(x)
                    index_y = update_list.index(y)
                    if index_x > index_y:
                        update_list.remove(x)
                        update_list.insert(index_y, x)
                        changed = True
                        changes += 1
        if changes == 0:
            return None
        return update_list

    reordered_updates = []
    for update in instructions:
        reordered_update = reorder_update(update, rules)
        if reordered_update is not None:
            reordered_updates.append(reordered_update)


    middle_pages = []
    for update in reordered_updates:
        middle_page = update[len(update) // 2]
        middle_pages.append(int(middle_page))

    # Sum of middle pages
    result = sum(middle_pages)
    return result



def main():
    print(task1())
    print(task2())

if __name__ == "__main__":
    main()