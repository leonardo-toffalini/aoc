with open("day11/input.txt", "r") as f:
    grid = f.read().splitlines()


all_rows = set([i for i in range(len(grid))])
all_cols = set([i for i in range(len(grid[0]))])

cols = set()
rows = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            rows.add(i)
            cols.add(j)

exp_rows = all_rows - rows
exp_cols = all_cols - cols

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxies.append((i, j))


total = 0

for i, (r1, c1) in enumerate(galaxies):
    for r2, c2 in galaxies[i:]:
        for r in range(min(r1, r2), max(r1, r2)):
            if r in exp_rows:
                total += 1000000
            else:
                total += 1
        for c in range(min(c1, c2), max(c1, c2)):
            if c in exp_cols:
                total += 1000000
            else:
                total += 1

print(total)
