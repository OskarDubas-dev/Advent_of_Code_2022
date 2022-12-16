import functions

with open('input.txt') as file:
    data = file.read()

print(data)

counter = 0

for i in range(4, len(data)):
    s = set(data[(i-4):i])
    #print(s, i)
    if len(s) == 4:
        print(i)
