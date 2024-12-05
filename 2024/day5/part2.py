import numpy as np
from functools import cmp_to_key

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

def custom_comparison(x, y):
    if x in ruleset.get(y, set()):
        return -1
    return 1

total = 0
for page in pages:
    sorted_page = sorted(page, key=cmp_to_key(custom_comparison))
    if page != sorted_page:
        total += sorted_page[len(sorted_page) // 2]

print(total)
