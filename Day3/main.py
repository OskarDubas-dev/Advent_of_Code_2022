import functions

rucksacks = functions.get_data(strip=True)
left_compartment = []
right_compartment = []
# Priority values
# a to z is 1 to 26 -> subtract 96 from ord()
# A to Z is 27 to 52 -> subtract 38 from ord()
result_part1 = 0
result_part2 = 0

for idx, i in enumerate(rucksacks):
    # part 1
    x = int(len(i) / 2)
    left_compartment.append(i[:x])
    right_compartment.append(i[-x:])

    rucksack_set = set(left_compartment[idx]) & set(right_compartment[idx])
    same_item = rucksack_set.pop()
    if same_item.isupper() is True:
        result_part1 += ord(same_item) - 38
    else:
        result_part1 += ord(same_item) - 96

    # part2
    if (idx + 1) % 3 == 0:
        rucksack_set_3 = set(rucksacks[idx]) & \
                         set(rucksacks[idx-1]) & \
                         set(rucksacks[idx-2])
        same_item = rucksack_set_3.pop()
        if same_item.isupper() is True:
            result_part2 += ord(same_item) - 38
        else:
            result_part2 += ord(same_item) - 96


# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?
# Part 1 answer
print(result_part1)

# Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?
# Part 2 answer
print(result_part2)
