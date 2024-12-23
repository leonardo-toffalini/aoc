
with open('day5/input1.txt') as f:
  inputs, *blocks = f.read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []

    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            overlap_start = max(s, b)
            overlap_end = min(e, b + c)
            if overlap_start < overlap_end:
                new.append((overlap_start - b + a, overlap_end - b + a))
                if overlap_start > s:
                    seeds.append((s, overlap_start))
                if e > overlap_end:
                    seeds.append((overlap_end, e))
                break
        else:
            new.append((s, e))
    seeds = new

# print(sorted(seeds))
print(min(seeds)[0])