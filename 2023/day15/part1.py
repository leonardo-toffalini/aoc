with open("day15/input.txt", "r") as f:
    blocks = f.read().split(",")


def hash(part):
    curr = 0
    for ch in part:
        curr += ord(ch)
        curr = (curr * 17) % 256
    return curr


total = 0
for part in blocks:
    total += hash(part.strip())
print(total)
