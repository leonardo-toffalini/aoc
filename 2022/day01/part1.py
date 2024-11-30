with open("day1/input.txt") as f:
    blocks = f.read().strip().split("\n\n")
    calories = []
    for block in blocks:
        int_block = list(map(int, block.split("\n")))
        calories.append(sum(int_block))
    print(max(calories))
