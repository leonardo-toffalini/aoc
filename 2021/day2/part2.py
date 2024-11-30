with open("input.txt", "r") as f:
    d = f.readlines()

depth = 0
hor = 0
aim = 0

for l in d:
    dir, x = l.split()
    x = int(x)
    match dir:
        case "forward":
            hor += x
            depth += aim * x
        case "down":
            aim += x
        case "up":
            aim -= x

print(f"{depth = }, {hor = }")
print(depth * hor)
