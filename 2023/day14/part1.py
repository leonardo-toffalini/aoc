with open("day14/input.txt", "r") as f:
    grid = f.read().splitlines()

columns = dict()
N = len(grid)

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if c not in columns:
            columns[c] = {-1: 0}
        if char == "#":
            columns[c][r] = 0
        if char == "O":
            columns[c][max(columns[c].keys())] += 1

total = 0
for key in columns.keys():
    print(f"{key}: {columns[key]}")
    for rock in columns[key]:
        total += sum([N - i for i in range(rock + 1, rock + 1 + columns[key][rock])])
print(total)
