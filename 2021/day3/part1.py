import numpy as np

with open("input.txt", "r") as f:
    d = np.array(list(
        map(lambda x:
            list(map(lambda y: int(y), list(x.strip()))),
        f.readlines())
    ))

gamma = ""
epsilon = ""

for i in range(len(d[0])):
    ones = np.count_nonzero(d[:, i] == 1)
    zeros = np.count_nonzero(d[:, i] == 0)

    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    elif ones < zeros:
        gamma += "0"
        epsilon += "1"


g = int(gamma, 2)
e = int(epsilon, 2)
print(g * e)

