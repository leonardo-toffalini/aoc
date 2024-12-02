with open("input.txt", "r") as f:
    d = list(map(
        lambda x: list(map(
            lambda y: int(y),
            x.strip().split())),
        f.readlines()
    ))

def safe(report):
    return inc(report) or dec(report)

def inc(report):
    prev = report[0]
    for x in report[1:]:
        if prev >= x or prev < x - 3:
            return False
        prev = x
    return True

def dec(report):
    prev = report[0]
    for x in report[1:]:
        if prev <= x or prev > x + 3:
            return False
        prev = x
    return True

res = 0
for report in d:
    if any([safe(report[:i] + report[i+1:]) for i in range(len(report))]):
        res += 1

print(res)
