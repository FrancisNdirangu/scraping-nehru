array = []
stuff = []
for i in range(100):
    if len(stuff)==5:
        array.append(stuff)
        stuff = []

    for j in range(100):
        if j%3 == 0:
            stuff.append(j)
print(array)
print('stuff:',stuff)
