import numpy as np
import re

with open("input.txt", "r") as f:
    d = np.array(list(map(
        lambda x: list(x.strip()),
        f.readlines()
    )))

pattern1 = r"XMAS"
pattern2 = r"SAMX"

def find_xmas(text) -> int:
    return len(re.findall(pattern1, text)) + len(re.findall(pattern2, text))

total = 0

# rows
for i, row in enumerate(d):
    r = "".join(row)
    total += find_xmas(r)

# cols
for i in range(len(d[0])):
    col = "".join(d[:, i])
    total += find_xmas(col)

def tally_diags(mtx):
    counter = 0
    main_diag = "".join(mtx.diagonal())
    counter += find_xmas(main_diag)

    for i in range(1, len(mtx)):
        udiag = "".join(mtx.diagonal(i))
        counter += find_xmas(udiag)

        ldiag = "".join(mtx.diagonal(-i))
        counter += find_xmas(ldiag)
    return counter

total += tally_diags(d)  # main diags
total += tally_diags(np.fliplr(d))  # secondary diags diags

print(total)

