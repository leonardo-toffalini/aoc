
with open('day6/input.txt') as f:
  t, d = f.readlines()


time = "".join(t.strip().split(': ')[1].strip().split())
distance = "".join(d.strip().split(': ')[1].strip().split())

time = int(time)
distance = int(distance)
# print(time)
# print(distance)

minimum = 0
for i in range(time):
  td = i * (time - i)
  if td > distance:
    minimum = i
    break


print(f'minimum: {minimum}')
print(f'time: {time}')
print(time - 2*minimum + 1)