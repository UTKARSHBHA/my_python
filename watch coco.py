name = input("enter the name: ")
age = int(input("enter the age: "))
if age >= 10 and (name[0] == "a" or name[0] == "A"):
    print("you can watch the movie")
else:
    print("you cannot watch the movie")