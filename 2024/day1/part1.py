import numpy as np

with open("input.txt", "r") as f:
    d = np.array(list(map(
        lambda x: list(map(
            lambda y: int(y),
            x.strip().split("   "))),
        f.readlines()
    )))

res = sum([abs(x - y) for x, y in zip(sorted(d[:, 0]), sorted(d[:, 1]))])
print(res)
