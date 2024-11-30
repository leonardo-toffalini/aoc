
with open('day3/input2.txt') as f:
    lines = f.read().splitlines()

# for line in lines:
#     print(line)

total = 0

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char != '*':
            continue

        cs = set()

        for cr in [row - 1, row, row + 1]:
            for cc in [col - 1, col, col + 1]:
                if cr < 0 or cc < 0 or cr >= len(lines) or cc >= len(line) or not lines[cr][cc].isdigit():
                    continue
                
                while cc > 0 and lines[cr][cc - 1].isdigit():
                    cc -= 1
                cs.add((cr, cc))
        if len(cs) != 2:
            continue
        # print(cs)

        out = []
        for cr, cc in cs:
            s = ""
            while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                s += lines[cr][cc]
                cc += 1
            out.append(int(s))
        total += out[0] * out[1]

print(total)