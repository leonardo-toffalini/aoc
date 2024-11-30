
with open('day4/input1.txt') as f:
    lines = f.read().splitlines()


t = 0

for line in lines:
    line = line.split(":")[1].strip()
    winners, nums = [list(map(int, part.split())) for part in line.split(" | ")] # converts two lists of strings into two lists of ints
    j = 0
    for winner in winners:
        if winner in nums:
            j += 1
    # j = sum(q in a for q in b)
    if j > 0:
        t += 2 ** (j - 1)

print(t)