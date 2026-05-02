array = []
stuff = []
for i in range(100):
    if i %5 == 0:
        array.append(stuff)
        stuff = []
    else:
        stuff = stuff

    for j in range(100):
        if j%3 == 0:
            stuff.append(j)
print(array)

