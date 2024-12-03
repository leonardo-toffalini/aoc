import re

with open("input.txt", "r") as f:
    d = "".join(f.readlines())

p1 = r"(mul\([0-9]+,[0-9]+\))"
p2 = r"(do\(\))"
p3 = r"(don't\(\))"
pattern = fr"{p1}|{p2}|{p3}"
print(f"regex pattern: {pattern}")

matches = re.findall(pattern=pattern, string=d)
total = 0

flag = True
for m in matches:
    if m[2] != "":
        flag = False
    if m[1] != "":
        flag = True
    if m[0] != "":
        x, y = list(map(int, m[0][len("mul("):-len(")")].split(",")))
        if flag:
            total += x*y

print(total)
