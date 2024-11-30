
with open('day8/input1.txt', 'r') as f:
  steps, nodes = f.read().split('\n\n')
mp = {}

nodes = nodes.splitlines()

for node in nodes:
  val, dirs = node.split(' = ')
  left, right = dirs[1:-1].split(', ')
  mp[val] = {'L': left, 'R': right}

curr = 'AAA'

counter = 0
while curr != 'ZZZ':
  for direction in steps:
    curr = mp[curr][direction]
    counter += 1
    if curr == 'ZZZ':
      break

print(counter)