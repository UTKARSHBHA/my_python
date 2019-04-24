a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
"""
if a > b > c:
    print(a)
elif a > c > b:
    print(a)
elif b > a > c:
    print(b)
elif b > c > a:
    print(b)
elif c > a > b:
    print(c)
elif c > b > a:
    print(c)
else:
    print("error")
"""

if a > b and a > c:
    print(a, "is greater")
elif b > a and b > c:
    print(b, "is greater")
elif c > b and c > a:
    print(c, "is greater")