from math import gcd

with open('day8/input2.txt', 'r') as f:
  steps, nodes = f.read().split('\n\n')

mp = {}

nodes = nodes.splitlines()

for node in nodes:
  val, dirs = node.split(' = ')
  left, right = dirs[1:-1].split(', ')
  mp[val] = {'L': left, 'R': right}

currs = [key for key in mp.keys() if key.endswith('A')]
cycles = []

print(currs)

for current in currs:
  cycle = []

  curr_steps = steps
  counter = 0
  first_z = None

  while True:
    while counter == 0 or not current.endswith('Z'):
      counter += 1
      current = mp[current][curr_steps[0]]
      curr_steps = curr_steps[1:] + curr_steps[0]

    cycle.append(counter)

    if first_z is None:
      first_z = current
      counter = 0
    elif current == first_z:
      break

  cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
  lcm = lcm * num // gcd(lcm, num)

print(lcm)
