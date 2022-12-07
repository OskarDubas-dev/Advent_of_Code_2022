import functions

elf_calories_data = functions.get_data()
elf_calories_data_stripped = [s.strip() for s in elf_calories_data]
elf_calories_data_int = [int(i or 0) for i in elf_calories_data_stripped]
elves = []
calories = 0
most_calories = 0

for item in elf_calories_data_int:

    if item != 0:
        calories += item
    else:
        elves.append(calories)
        if most_calories < calories:
            most_calories = calories
        calories = 0

print(most_calories)