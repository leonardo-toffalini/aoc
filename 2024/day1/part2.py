import numpy as np

with open("input.txt", "r") as f:
    d = np.array(list(map(
        lambda x: list(map(
            lambda y: int(y),
            x.strip().split("   "))),
        f.readlines()
    )))

col1 = d[:, 0]
col2 = d[:, 1]

res = 0
for i, n in enumerate(col1):
    res += n * np.count_nonzero(col2 == n)

print(res)
