with open("day03/input.txt", "r") as f:
    boxes = [line.strip() for line in f.read().splitlines()]


total = 0
for box in boxes:
    n = len(box)
    half = n // 2
    first = box[half:]
    second = box[:half]

    for ch in first:
        if ch in second:
            x = ch
            break

    if x.islower():
        total += ord(x) - 96
    else:
        total += ord(x) - 38

print(total)
