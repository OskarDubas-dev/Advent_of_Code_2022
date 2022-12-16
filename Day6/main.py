import functions

with open('input.txt') as file:
    data = file.read()

print(data)

counter = 0

for i in range(4, len(data)):
    s = set(data[(i - 4):i])

    # part 1 solution
    if len(s) == 4:
        print(i)
        break

for i in range(14, len(data)):
    s = set(data[(i - 14):i])

    # part 2 solution
    if len(s) == 14:
        print(i)
        break
