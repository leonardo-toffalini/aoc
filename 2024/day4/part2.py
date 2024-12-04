import numpy as np

with open("input.txt", "r") as f:
    d = np.array(list(map(
        lambda x: list(x.strip()),
        f.readlines()
    )))

def diag_xmas(a, i, j):
    ul = a[i-1, j-1]
    lr = a[i+1, j+1]
    return (ul == "M" and lr == "S") or (ul == "S" and lr == "M")

def secondary_diag_xmas(a, i, j):
    ur = a[i-1, j+1]
    ll = a[i+1, j-1]
    return (ur == "M" and ll == "S") or (ur == "S" and ll == "M")


def check_xmas(a, i, j):
    return diag_xmas(a, i, j) and secondary_diag_xmas(a, i, j)

total = 0
for i, r in enumerate(d):
    for j, c in enumerate(r):
        if i in (0, len(d)-1) or j in (0, len(r)-1):
            continue
        if c == "A":
            total += int(check_xmas(d, i, j))

print(total)
