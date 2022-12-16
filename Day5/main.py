import re

with open("input.txt", 'r') as file_local:
    local_data = file_local.readlines()[10:]
    local_data_stripped = [s.strip() for s in local_data]

# commands for the crane (only numbers)
rearrange_nums = []
re_rearrange_nums = []
for idx, i in enumerate(local_data_stripped):
    rearrange_nums.append([int(s) for s in local_data_stripped[idx] if s.isdigit()])
    re_rearrange_nums.append([int(s) for s in re.findall(r'\d+', i)])
crates = [
    [],
    ['Z', 'J', 'N', 'W', 'P', 'S'],
    ['G', 'S', 'T'],
    ['V', 'Q', 'R', 'L', 'H'],
    ['V', 'S', 'T', 'D'],
    ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
    ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
    ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
    ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'],
    ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
]

for i in re_rearrange_nums:
    print(i)

for idx, i in enumerate(re_rearrange_nums):
    repeat = i[0]
    pickup = i[1]
    dropoff = i[2]

    while repeat != 0:
        try:
            crates[dropoff].append(crates[pickup].pop())
            repeat -= 1
        except:
            print(f"empty list at crate number:{idx}")
            repeat -= 1

for i in crates:
    print(i)
