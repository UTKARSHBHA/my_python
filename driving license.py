print("WHAT IS YOUR AGE?")

age = int(input())

if age<7:
    print("invalid input")
elif age>100:
    print("invalid output")
elif age<18:
    print("you can not get a driving license")
elif age==18:
    print("we will think about it")

else:
    print("you can have your driving license")