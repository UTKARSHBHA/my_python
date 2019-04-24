print("CALCULATOR")

n1 = int(input("enter first number :"))
n2 = int(input("enter second number :"))
n3 = input("choose operator:")

if n1 == 45 and n2 == 3 and n3 == "*":
    print(555)
elif n1 == 56 and n2 == 9 and n3 == "+":
    print(77)
elif n1 == 56 and n2 == 6 and n3 == "/":
    print(4)
elif n3 == "+":
    print(n1+n2)
elif n3 == "-":
    print(n1-n2)
elif n3 == "*":
    print(n1*n2)
elif n3 == "/":
    print(n1/n2)
elif n3 == "**":
    print(n1**n2)
else:
    print("error! chose appropriate operator")
