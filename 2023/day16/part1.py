from typing import Tuple, Set
from collections import deque

with open("day16/input.txt", "r") as f:
    grid = f.read().splitlines()

visited: Set[Tuple] = set()

q = deque([(0, -1, 0, 1)])
while q:
    r, c, dr, dc = q.popleft()
    r += dr
    c += dc

    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        continue

    next = grid[r][c]

    if next == "." or (next == "-" and dc != 0) or (next == "|" and dr != 0):
        if (r, c, dr, dc) not in visited:
            visited.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    elif next == "/":
        dr, dc = -dc, -dr
        if (r, c, dr, dc) not in visited:
            visited.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    elif next == "\\":
        dr, dc = dc, dr
        if (r, c, dr, dc) not in visited:
            visited.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    elif next == "|":
        for dr, dc in [(1, 0), (-1, 0)]:
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
    elif next == "-":
        for dr, dc in [(0, 1), (0, -1)]:
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
    else:
        raise AssertionError(f"unrecognized character: {next}")

coords = {(r, c) for (r, c, _, _) in visited}

print(len(coords))
