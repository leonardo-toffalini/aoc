with open("input.txt", "r") as f:
    d = list(map(
        lambda x: list(x.strip()),
        f.readlines()
    ))

antennas = dict()
for i, r in enumerate(d):
    for j, c in enumerate(r):
        if c == ".": continue
        if c in antennas: antennas[c].append((i, j))
        else: antennas[c] = [(i, j)]

def is_inbounds(i, j):
    return 0 <= i and i < len(d) and 0 <= j and j < len(d[0])

antinodes = set()
for k, points in antennas.items():
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x, y = points[i], points[j]
            diff = (x[0] - y[0], x[1] - y[1])
            a1 = (x[0] - diff[0], x[1] - diff[1])
            a2 = (x[0] + diff[0], x[1] + diff[1])
            a3 = (y[0] - diff[0], y[1] - diff[1])
            a4 = (y[0] + diff[0], y[1] + diff[1])
            a = set([z for z in [a1, a2, a3, a4] if is_inbounds(z[0], z[1])]) - set([x, y])
            antinodes = antinodes.union(a)

for antinode in antinodes:
    d[antinode[0]][antinode[1]] = "#"

for r in d:
    print("".join(r))

print(f"answer: {len(antinodes)}")
