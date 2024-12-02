import numpy as np
from icecream import ic

with open("test.txt", "r") as f:
    d = np.array(list(
        map(lambda x:
            list(map(lambda y: int(y), list(x.strip()))),
        f.readlines())
    ))

o2 = d
co2 = d
final_o2 = []
final_co2 = []


for i in range(len(d[0])):
    count1 = np.count_nonzero(d[:, i] == 1)
    count0 = np.count_nonzero(d[:, i] == 0)

    if count1 > count0:
        i1 = np.nonzero(o2[:, i] == 1)
        i0 = np.nonzero(co2[:, i] == 0)
        o2 = o2[i1]
        co2 = co2[i0]
    elif count1 < count0:
        i1 = np.nonzero(co2[:, i] == 1)
        i0 = np.nonzero(o2[:, i] == 0)
        o2 = o2[i0]
        co2 = co2[i1]
    elif count1 == count0:
        i1 = np.nonzero(o2[:, i] == 1)
        i0 = np.nonzero(co2[:, i] == 0)
        

    if len(o2) == 1:
        final_o2 = o2
    if len(co2) == 1:
        final_co2 = co2

print(final_o2)
print(final_co2)

x = int(
    "".join(
        list(map(lambda x: str(x), final_o2[0]))
    ),
    2
)
y = int(
    "".join(
        list(map(lambda x: str(x), final_co2[0]))
    ),
    2
)
print(x, y)
print(x*y)


