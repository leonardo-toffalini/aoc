from typing import Dict

with open("day12/input.txt", "r") as f:
    data = [line.split(" ") for line in f.readlines()]

grid, nums = [], []
for row in data:
    grid.append(row[0])
    nums.append(tuple(map(int, row[1].strip().split(","))))


def is_valid(row, places):
    counter = 0
    j = 0
    for ch in row:
        if ch == "#":
            counter += 1
        if ch == "." and counter > 0:
            if j > len(places) - 1:
                return False
            if places[j] != counter:
                return False
            else:
                j += 1
                counter = 0
    if row[-1] == "#":
        j += 1
        if places[-1] != counter:
            return False
    return j == len(places)


cache: Dict[str, tuple] = dict()


def place(row, places):
    if row.count("?") == 0:
        if not is_valid(row, places):
            return 0
        else:
            # print(row)
            return 1
    else:
        if (row, places) in cache:
            return cache[(row, places)]
        i = row.find("?")
        row1 = row[:i] + "." + row[i + 1 :]
        row2 = row[:i] + "#" + row[i + 1 :]
        # print(row1)
        # print(row2)
        result = place(row1, places) + place(row2, places)
        cache[(row, places)] = result
        return result


total = 0
for i in range(len(grid)):
    total += place(grid[i], nums[i])
print(total)
print(len(cache))
