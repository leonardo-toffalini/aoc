from icecream import ic

with open("test.txt", "r") as f:
    d = list(map(
        lambda x: list(x.strip()),
        f.readlines()
    ))

si, sj = -1, -1
for ii, r in enumerate(d):
    for jj, c in enumerate(r):
        if c == "^":
            si, sj = (ii, jj)

total = 0
for ii, r in enumerate(d):
    for jj, c in enumerate(r):
        if c != ".":
            continue
        d[ii][jj] = "O"

        di, dj = -1, 0
        i, j = si, sj

        cache = set()
        while (i, j, di, dj) not in cache:
            cache.add((i, j, di, dj))

            ni, nj = i + di, j + dj
            if ni < 0 or ni >= len(d) or nj < 0 or nj >= len(d[0]):
                break

            if d[ni][nj] in ("#", "O"):
                di, dj = dj, -di

            i, j = i + di, j + dj
        else:
            total += 1

        d[ii][jj] = "."

print(total)

