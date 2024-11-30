with open("day02/input.txt", "r") as f:
    games = [line.split(" ") for line in f.read().strip().splitlines()]

abc = {"A": 0, "B": 1, "C": 2}
xqz = {"X": 0, "Y": 1, "Z": 2}
scores = [[1 + 3, 2 + 6, 3 + 0], [1 + 0, 2 + 3, 3 + 6], [1 + 6, 2 + 0, 3 + 3]]

total = 0

for game in games:
    opp, me = game

    total += scores[abc[opp]][xqz[me]]

print(total)
