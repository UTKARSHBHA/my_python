
l2 = "y"
while l2 == "y":
    l1 = int(input("enter number of which you want to print table:"))
    u = 0
    for u in range(0, 11):
        print(l1, "*", u, "=", l1 * u)
    l2 = input("do you want to continue:")


