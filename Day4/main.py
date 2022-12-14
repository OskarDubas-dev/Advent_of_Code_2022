import functions

big_list = functions.get_data(strip=True)

pairs_part2 = 0
pairs = 0
pairs1 = 0

for idx, i in enumerate(big_list):

    a, b = i.split(",")

    a_section1, a_section2 = a.split("-")
    b_section1, b_section2 = b.split("-")

    a_list = [*range(int(a_section1), int(a_section2) + 1)]
    b_list = [*range(int(b_section1), int(b_section2) + 1)]

    sections_set = list(set(a_list) & set(b_list))

    if sections_set:
        pairs_part2 += 1

    if sections_set == a_list or sections_set == b_list:
        pairs += 1


    # different way

    first = [int(i) for i in a.split("-")]
    second = [int(i) for i in b.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs1 += 1
        pair_found_again = True
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs1 += 1

    if first[0] > second[0] and first[1] >= second[1]:
        pairs1 += 1
        pair_found_again = True
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs1 += 1



# wrong answer
# I kept it so to remember that set() is unordered and messed up the solution
print(pairs)
# answer to Part 1
print(pairs1)

# answer to part 2
print(pairs_part2)
# In how many assignment pairs does one range fully contain the other?
#
