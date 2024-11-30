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

while q:
  r, c = q.popleft()
  ch = grid[r][c]

  if r > 0 and ch in 'S|JL' and grid[r-1][c] in '|7F' and (r - 1, c) not in seen: # going up
    seen.add((r - 1, c))
    q.append((r - 1, c))

  if r < len(grid) - 1 and ch in 'S|7F' and grid[r + 1][c] in '|JL' and (r + 1, c) not in seen: # going down
    seen.add((r + 1, c))
    q.append((r + 1, c))

  if c > 0 and ch in 'S-J7' and grid[r][c - 1] in '-LFG' and (r, c - 1) not in seen: # going left
    seen.add((r, c - 1))
    q.append((r, c - 1))

  if c < len(grid[r]) and ch in 'S-LF' and grid[r][c + 1] in '-J7' and (r, c + 1) not in seen: # going right
    seen.add((r, c + 1))
    q.append((r, c + 1))

print(len(seen) // 2)