d = "y"
while d == "y":
    a = input("enter operator:")
    b = int(input("enter first number:"))
    c = int(input("enter second number"))

    if a == "+":
        print(b + c)
    elif a == "-":
        print(b - c)
    elif a == "*":
        print(b * c)
    elif a == "/":
        print(b / c)
    else:
        print("choose correct operator:")
    d = input("do you want to continue!")
