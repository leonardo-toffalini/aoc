with open("input.txt", "r") as f:
    d = list(map(
        lambda x: list(x.strip()),
        f.readlines()
    ))

# rotations: (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
dir = (-1, 0)
i, j = -1, -1

for ii, r in enumerate(d):
    for jj, c in enumerate(r):
        if c == "^":
            i, j = (ii, jj)

cache = set()

while (i, j, dir) not in cache:
    cache.add((i, j, dir))

    ni, nj = i + dir[0], j + dir[1]
    if ni < 0 or ni >= len(d) or nj < 0 or nj >= len(d[0]):
        break

    if d[ni][nj] == "#":
        dir = (dir[1], -dir[0])

    i, j = i + dir[0], j + dir[1]

visited = list(set([key[:2] for key in cache]))

for p in visited:
    d[p[0]][p[1]] = "X"

for r in d:
    print("".join(r))

print(len(visited))

