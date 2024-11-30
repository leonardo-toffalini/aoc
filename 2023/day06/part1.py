
with open('day6/input.txt') as f:
  times, distances = f.readlines()

times = list(map(int, times.split(': ')[1].split()))
distances = list(map(int, distances.split(': ')[1].split()))
# print(times)
# print(distances)

total = 1

for time, distance in zip(times, distances):
  counter = 0
  for t in range(time):
    d = t * (time - t)
    if d > distance:
      counter += 1

  if counter != 0:
    total = total * counter

print(total)