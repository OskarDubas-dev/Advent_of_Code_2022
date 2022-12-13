import functions

big_list = functions.get_data(strip=True)

pairs = 0

first = []
second = []

first_sections = [[]]
second_sections = [[]]

for idx, i in enumerate(big_list):

    a, b = i.split(",")
    # first.append(a)
    # second.append(b)

    a_section1, a_section2 = a.split("-")
    b_section1, b_section2 = b.split("-")

    # a_list = [int(i) for i in a.split("-")]
    # b_list = [int(i) for i in b.split("-")]

    a_list = [*range(int(a_section1), int(a_section2) + 1)]
    # first_sections.append(a_list)

    b_list = [*range(int(b_section1), int(b_section2) + 1)]
    # second_sections.append(b_list)

    sections_set = list(set(a_list) & set(b_list))

    # sections_set = list(set(first_sections[idx]) & set(second_sections[idx]))
    # print(sections_set, first_sections[idx], second_sections[idx])
    if sections_set == a_list or sections_set == b_list:
        pairs += 1

print(pairs)

# In how many assignment pairs does one range fully contain the other?
#
