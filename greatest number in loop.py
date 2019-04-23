list = [5, 10, 21, 12, 32, 65, 65, 48, 65, 87, 66, 77, 54, 55, 10]

max = list[0]
for i in range(0, 15):
    if list[i] > max:
        max = list[i]
        print(max, "is greatest")
    i += i

