
with open('day9/input.txt', 'r') as f:
  starters = f.readlines()

def all_zeros(arr):
  for num in arr:
    if num != 0:
      return False
  return True


total = 0
for starter in starters:
  mtx = [list(map(int, starter.strip().split()))]
  while not all_zeros(mtx[-1]):
    temp = []
    for i in range(len(mtx[-1])-1):
      temp.append(mtx[-1][i+1] - mtx[-1][i])
    mtx.append(temp)
  
  curr = 0
  for i in range(len(mtx) - 1, -1, -1):
    curr = mtx[i][0] - curr
  total += curr

print(total)