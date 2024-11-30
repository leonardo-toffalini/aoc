with open("input.txt", "r") as f:
    d = f.readlines()

depth = 0
hor = 0

for l in d:
    dir, x = l.split()
    x = int(x)
    if dir == "forward":
        hor += x
    if dir == "down":
        depth += x
    if dir == "up":
        depth -= x

print(depth, hor)
print(depth * hor)
