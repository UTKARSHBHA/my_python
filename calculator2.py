def add(a, b):
    return(a + b)
def sub(a, b):
    return(a - b)
def mult(a, b):
    return(a * b)
def div(a, b):
    return(a / b)

dict = {"+":add,"-":sub, "*":mult, "/":div}
e = "y"
while e == "y":

    c = input("enter operator:")
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))


    def cal(c, a, b):
        print(dict[c](a, b))
    cal(c,a,b)
    d = input("do you want to continue:")