with open("input.txt", "r") as f:
    d = f.readlines()

prev = 0
counter = -1 # the first increase doesnt count
for l in d:
    cur = int(l)
    if cur > prev:
        counter += 1
    prev = cur

print(counter)
