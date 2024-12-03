import re

with open("input.txt", "r") as f:
    d = "".join(f.readlines())

pattern = r"mul\([0-9]+,[0-9]+\)"
print(f"regex pattern: {pattern}")

matches = re.findall(pattern=pattern, string=d)
total = 0

for m in matches:
    x, y = list(map(int, m[len("mul("):-len(")")].split(",")))
    total += x*y

print(total)

