from typing import Tuple, Set
from collections import deque

with open("day16/input.txt", "r") as f:
    grid = f.read().splitlines()


def counter(r: int, c: int, dr: int, dc: int) -> int:
    visited: Set[Tuple] = set()

    q = deque([(r, c, dr, dc)])
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

    return len(coords)


max_val = 0

for r in range(len(grid)):
    max_val = max(max_val, counter(r, -1, 0, 1))
    max_val = max(max_val, counter(r, len(grid[0]), 0, -1))

for c in range(len(grid[0])):
    max_val = max(max_val, counter(-1, c, 1, 0))
    max_val = max(max_val, counter(len(grid), c, -1, 0))

print(max_val)
