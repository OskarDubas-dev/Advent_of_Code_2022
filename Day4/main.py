import functions

big_list = functions.get_data(strip=True)

print(big_list)

for idx, i in enumerate(big_list):
    a = int(i[0])
    b = int(i[2])
    list_1 = [x for x in range(a) if x <= b]
    print(list_1)
    list_2 = []

# In how many assignment pairs does one range fully contain the other?
#
