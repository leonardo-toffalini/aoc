from collections import deque

with open('day10/input.txt', 'r') as f:
  grid = f.read().strip().splitlines()

for r, row in enumerate(grid):
  for c, col in enumerate(row):
    if col == 'S':
      sr = r
      sc = c
      break
  else:
    continue
  break
    
# BFS floodfill
seen = {(sr, sc)}
q = deque([(sr, sc)])

maybe_s = {'|', '-', 'J', 'L', 'F', '7'}

while q:
  r, c = q.popleft()
  ch = grid[r][c]

  if r > 0 and ch in 'S|JL' and grid[r-1][c] in '|7F' and (r - 1, c) not in seen: # going up
    seen.add((r - 1, c))
    q.append((r - 1, c))
    if ch == 'S':
      maybe_s &= {'|', 'J', 'L'}

  if r < len(grid) - 1 and ch in 'S|7F' and grid[r + 1][c] in '|JL' and (r + 1, c) not in seen: # going down
    seen.add((r + 1, c))
    q.append((r + 1, c))
    if ch == 'S':
      maybe_s &= {'|', '7', 'F'}

  if c > 0 and ch in 'S-J7' and grid[r][c - 1] in '-LFG' and (r, c - 1) not in seen: # going left
    seen.add((r, c - 1))
    q.append((r, c - 1))
    if ch == 'S':
      maybe_s &= {'-', 'J', '7'}

  if c < len(grid[r]) and ch in 'S-LF' and grid[r][c + 1] in '-J7' and (r, c + 1) not in seen: # going right
    seen.add((r, c + 1))
    q.append((r, c + 1))
    if ch == 'S':
      maybe_s &= {'-', 'L', 'F'}

assert len(maybe_s) == 1
(S,) = maybe_s

grid = [row.replace('S', S) for row in grid]
grid = [[ch if (r, c) in seen else '.' for c, ch in enumerate(row)] for r, row in enumerate(grid)]

outside = set()

for r, row in enumerate(grid):
  within = False
  up = None
  for c, ch in enumerate(row):
    if ch == '|':
      assert up is None
      within = not within
    elif ch == '-':
      assert up is not None
    elif ch in 'LF':
      assert up is None
      up = ch == 'L'
    elif ch in '7J':
      assert up is not None
      if ch != ('J' if up else '7'):
        within = not within
      up = None
    elif ch == '.':
      pass
    else:
      raise RuntimeError(f'unexpected character (horizontal): {ch}')
    if not within:
      outside.add((r, c))
  
print(len(grid) * len(grid[0]) - len(outside | seen))