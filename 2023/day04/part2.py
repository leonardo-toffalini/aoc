
with open('day4/input2.txt') as f:
    lines = f.read().splitlines()


m = {}

for i, line in enumerate(lines):
    if i not in m:
        m[i] = 1

    line = line.split(":")[1].strip()
    winners, nums = [list(map(int, part.split())) for part in line.split(" | ")] # converts two lists of strings into two lists of ints
    j = 0
    for winner in winners:
        if winner in nums:
            j += 1
    
    for n in range(i + 1, i + j + 1):
        m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))