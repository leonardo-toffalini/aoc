with open("input.txt", "r") as f:
    d = list(map(
            lambda y: [int(y[0]), list(map(int, y[1].split()))],
            list(map(
                lambda x: x.strip().split(":"),
                f.readlines()
            ))
        ))

def try_sol(target, numbers):
    if len(numbers) == 1: return target == numbers[0]
    if target % numbers[-1] == 0 and try_sol(target // numbers[-1], numbers[:-1]): return True
    if target > numbers[-1] and try_sol(target - numbers[-1], numbers[:-1]): return True
    return False

total = 0
for r in d:
    target = r[0]
    numbers = r[1]
    if try_sol(target, numbers): total += target

print(total)
