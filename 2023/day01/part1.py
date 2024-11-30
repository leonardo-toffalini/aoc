
# getting the input
with open('day1/input.txt') as f:
    lines = f.readlines()

out = 0

for line in lines:
  first, last = '0', '0'
  first_found = False
  for char in line:
    if char.isnumeric() and not first_found:
      first = char
      first_found = True
    if char.isnumeric():
        last = char
 
  out += int(first + last)
  last = '0'
  first_found = False

print(out)
