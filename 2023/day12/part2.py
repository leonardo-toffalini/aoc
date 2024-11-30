from typing import Dict

cache: Dict[str, tuple] = dict()


def count(row, nums):
    if row == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in row else 1

    key = (row, nums)

    if key in cache:
        return cache[key]

    result = 0

    if row[0] in ".?":
        result += count(row[1:], nums)

    if row[0] in "#?":
        if (
            nums[0] <= len(row)
            and "." not in row[: nums[0]]
            and (nums[0] == len(row) or row[nums[0]] != "#")
        ):
            result += count(row[nums[0] + 1 :], nums[1:])

    cache[key] = result
    return result


total = 0

with open("day12/input.txt", "r") as f:
    for line in f.readlines():
        row, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        row = "?".join([row] * 5)
        nums = nums * 5

        total += count(row, nums)

print(total)
