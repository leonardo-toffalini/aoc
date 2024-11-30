with open("day15/input.txt", "r") as f:
    blocks = f.read().split(",")


def hash(part):
    curr = 0
    for ch in part:
        curr += ord(ch)
        curr = (curr * 17) % 256
    return curr


boxes = [[] for _ in range(256)]
focal_lengths = {}

for part in blocks:
    if "-" in part:
        label = part[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    if "=" in part:
        label, focal_length = part.split("=")
        focal_length = int(focal_length)
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = focal_length


total = 0

for i, box in enumerate(boxes, 1):
    for slot, label in enumerate(box, 1):
        total += i * slot * focal_lengths[label]
print(total)
