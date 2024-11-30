with open("input.txt", "r") as f:
    d = f.readlines()

prev = sum(map(lambda x: int(x), d[:3]))
counter = 0
for i in range(4, len(d)+1):
    cur = sum(map(lambda x: int(x), d[i-3:i]))
    if cur > prev:
        counter += 1
    prev = cur

print(counter)
