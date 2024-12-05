import numpy as np

with open("input.txt", "r") as f:
    rules, pages = f.read().split("\n\n")

rules = np.array(list(map(
    lambda x: list(map(
        int,
        x.strip().split("|")
    )),
    rules.splitlines()
)))

pages = list(map(
    lambda x: list(map(
        int,
        x.strip().split(",")
    )),
    pages.splitlines()
))

# 53 -> {47, 61, 97, ...}
# 13 -> {97, 61, 29, ...}
# ... 
ruleset = dict()
for rule in rules:
    if rule[1] not in ruleset:
        ruleset[rule[1]] = {rule[0]}
    else:
        ruleset[rule[1]].add(rule[0])

remaining = []
for page in pages:
    seen = set()
    for x in page:
        if seen - ruleset.get(x, set()):
            break
        seen.add(x)
    else:
        remaining.append(page)

total = 0
for page in remaining:
    total += page[len(page) // 2]

print(total)

