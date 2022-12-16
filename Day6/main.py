import functions

data = str(functions.get_data())

print(data)

counter = 0

print(type(data))

for idx, i in enumerate(data):
    try:
        if(data[idx]) == 'p':
            print("hi")
    except:
        print("error")