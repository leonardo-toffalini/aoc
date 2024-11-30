# 12 red cubes, 13 green cubes, and 14 blue cubes

with open('day2/input.txt') as f:
    lines = f.readlines()

out = 0
for i, x in enumerate(lines):
    groups = x.strip().split(': ')[1].split('; ')
    for group in groups:
        m = {'red': 0, 'green': 0, 'blue': 0}
        for element in group.split(', '):
            num, color = element.split(' ')
            m[color] = int(num)
        if m['red'] > 12 or m['green'] > 13 or m['blue'] > 14:
            break
    else:
        out += i + 1
print(out)
