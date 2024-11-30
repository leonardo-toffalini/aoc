
with open('day3/input1.txt') as f:
    lines = f.read().splitlines()

# for line in lines:
#     print(line)


cs = set()

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char.isdigit() or char == '.':
            continue
        # print(char, end='')
        for cr in [row - 1, row, row + 1]:
            for cc in [col - 1, col, col + 1]:
                if cr < 0 or cc < 0 or cr >= len(lines) or cc >= len(line) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc - 1].isdigit():
                    cc -= 1
                cs.add((cr, cc))
# print()
# print(cs)

out = []
for row, col in cs:
    s = ""
    while col < len(lines[row]) and lines[row][col].isdigit():
        s += lines[row][col]
        col += 1
    out.append(int(s))
    # print(s)

print(sum(out))