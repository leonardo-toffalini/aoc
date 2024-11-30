import re

# getting the input
with open('day1/input2.txt') as f:
    lines = f.readlines()

n = "one two three four five six seven eight nine".split()

p = "(?=(" + "|".join(n) + "|\\d))"

def f(x):
    if x in n:
        return str(n.index(x) + 1)
    return x


out = 0
for line in lines:
    digits = [*map(f, re.findall(p, line))]
    print(digits)
    out += int(digits[0] + digits[-1])

print(out)
