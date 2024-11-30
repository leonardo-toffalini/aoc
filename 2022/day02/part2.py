strategy = {
    ("A", "X"): (0 + 3),
    ("A", "Y"): (3 + 1),
    ("A", "Z"): (6 + 2),
    ("B", "X"): (0 + 1),
    ("B", "Y"): (3 + 2),
    ("B", "Z"): (6 + 3),
    ("C", "X"): (0 + 2),
    ("C", "Y"): (3 + 3),
    ("C", "Z"): (6 + 1),
}

with open("day02/input.txt", "r") as f:
    games = [line.split(" ") for line in f.read().strip().splitlines()]

total = 0
for game in games:
    total += strategy[tuple(game)]


print(total)
