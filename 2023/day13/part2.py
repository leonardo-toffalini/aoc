def find_symmetry(part):
    for r, _ in enumerate(part, 1):
        top = (part[:r])[::-1]
        bot = part[r:]

        if (
            sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(top, bot))
            == 1
        ):
            return r

    return 0


total = 0
with open("day13/input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")
    for block in blocks:
        part = block.split("\n")

        row = find_symmetry(part)
        transpose = list(zip(*part))
        col = find_symmetry(transpose)
        total += 100 * row + col


print(total)
