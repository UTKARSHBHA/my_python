#Commented by GAurav Dixit

print("PYTHONS NOTES")
#so what you saw was the prit function you can print anything using this functiom
#you can create comments by putting hash sign before any statement so that it do not effect the program
"""
if you want to create multiline comments
you can use triple qoutes
"""
print("every print function will start with new line")
print("so if you do not want to end the statement")
print("you can use the end", end = "")
print(", new line charater ")
print()
print("also you can put anyting", end = " between ")
print("the quotes")
#imp do not forget to put comma before starting the end
print("you can also join","two statements by comma which woks as space")
#strings and integers can be added as a string by using comma statement but can nit be used by adding them
print("strings can also be added "+"by using plus sign")
print("ESCAPE SEQUENCE CHARACTER")
print("backword slash n breakes\nthe line ")

print("VARIABLES")
string = "always comes in double quotes"
integer = 5
floating_point_number = 66.25
#integers and floating point numbers do not needed to be put in quotes
print(string)
print(integer)
print(floating_point_number)

print("TYPE FUNCTION")
print("type function tells us which type of variable is it")
print(type(string))
print(type(integer))
print(type(floating_point_number))

print("variables and floating point number can be added")
print(integer + floating_point_number)
#two strings can also be added but string and integer can not
string2 = "and can be changed to integers"
print(string + string2)
#variables can be changed to string by putting it in quotes
integer2 = "10"
integer3 = "550.36"
print(integer2 + integer3)
print("you can change integer to string by using str function also vice versa by using int function and float function to")
v1 = "65"
v2 = "55"
print(v1 + v2)
print(int(v1) + int(v2))
s1 = "hello"
s2 = "world"
"""
to print any variable multiple time 
you can enter the number and star before it
"""
print(100 * "hello darkness my old friend")
print(1000 * "if you want to start the sentence with new line you can put backward slash n at the end\n")
#if you did the same with a integer it simply multiply its value
print(55 * 55)
"""
print("INPUT FUNCTION")
inp = input()
print("you entered", inp)

print("CALCULATOR")
print("enter first number")
inp1 = input()
print("enter second number")
inp2 = input()
print("product of the above numbers is", int(inp1) * int(inp2))
"""
#no matter what you type in the input function it is always going to ba a string and to change the input to integer you have to use the int function
print("STRING")
s = "string is combination of characters"
print(s)
#characters start with 0
print(s[0])
print(s[1])
#to print from some character to some character use colun
print(s[0:6])
print("LENGTH FUNCTION")
print(len(s))
print(s[0:35])
#first number is including and last number is excluding
print("to skip characters another colun is used")
print(s[0:35:2])
#using 2 every alternative character is skiped
print(s[0:])
#if you left the space after column it takes it as the length of the string and print the whole
print(s[:5])
#if you left the space before the column it will take it as zero
print(s[:])
#if you just put the column it will print the whole thing
print(s[::])
#if you left the space empty after the second column it will take it as 1 therefore print the whole
print(s[::3])
#if you type 3 after the second column it will skip 2 characters after every one character
print(s[-5:-2])
#you can also count the characters in negative but it starts from right hand side to left hand side
#and the last character can be stated as negative one
print(s[::-1])
#if you put negative one after the second column it will reverse the string

#boolean string test
print(s.isalnum())
#this functuon checks that if the string has space or not
print(s.isalpha())
#this checks alpha numbers
print(s.endswith("characters"))
print(s.endswith("character"))
#it chackes that if the string ends with given characters or not
print(s.count("a"))
#it counts how many times given character is present in the string
print(s.capitalize())
#it capitalise the first letter
print(s.find("characters"))
#it finds the character in the string
print(s.lower())
print(s.upper())
#it changes the whole string to given upper or lower case
print(s.replace("characters", "char"))
print("Tile Has First Letter Capital".istitle())
""""
o = input("What is your first name:").lower()
print(o)

p = input("what is your sir name:").upper()
print(p)
"""
print("LIST")
books = ["rd", "rs", "hc", "vs", 999]
print(books)
print(books[0])
print(books[3])
print(books[4])
numbers = [000, 555, 888]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#functions like sort and reverse change the list but slicing does not
print(numbers[1:3])
print(numbers)
print(numbers[::-1])
#do not use values less than negative one after the second column because if you put any values rather than leaving it empty in the space between column or before column it will show empty list
print(numbers[0:3:-2])
print(numbers[::-2])
print("APPEND FUNCTION")
numbers.append(55)
print(numbers)
#append function add the given number at the end if the function

print("INSERT FUNCTIOM")
numbers.insert(2, 100)
print(numbers)
#insert function add the number to the given position in the list which is given before the comma and the is given after the comma

print("POP FUNCTION")
numbers.pop()
print(numbers)
#pop function removes the last number of the list

#Mutble - which can be changed ie list
#Immutable - ehich can not be changed ie tuple

numbers[1] = 98
print(numbers)

tp = (52, 62, 92, 32, 72)
print(tp)
#tuple comes in paranthesis and list comes in square brackets
#if you want to create a one value tuple you have to put comma after the first digit otherwise it will take it as variable
tp2 = (65,)
print(tp2)

print("To swap two variables")
a = 5
b = 10
print(a, b)
temp = a
a = b
b = temp
print(a, b)

#or you can simply do it like this
a, b = b, a
print(a, b)

print("DICTIONARY")
#dictionary is noting but key value function
d1 = {"utkarsh":"bhardwaj", "akshay":"kumar", "salman":{"a":"khan", "b":"ali"}}
print(d1)
print(d1["utkarsh"])
print(d1["salman"])
print(d1["salman"]["a"])
#you can create dictionary in dictionary as value
#to add value in the dictionary
d1["hritik"] = "roshan"
print(d1)
#to delete any value from the function
del d1["salman"]
print(d1)
d2 = d1
del d2["akshay"]
print(d2)
print(d1)
#if you put a dictionary to another dictionary without using copy function it will not create a new dictionary but refer to the another dictionary and if you delete or change any thing from the dictionary it will change the another dictionary
d3 = d1.copy()
del d3["utkarsh"]
print(d3)
print(d1)
print(d1.get("utkarsh"))
#get function will give the value of the key
d1.update({"rajkumar":"rao"})
print(d1)
#update function udate the dictionary
print(d1.keys())
#keys function print all the keys in the given dictionary
print(d1.items())
#items function print all the items

print("SET")
s = set([5, 10, 55, 52])
print(s)
s1 = s.intersection({10, 5, 88})
print(s, s1)
s2 = s.union({12,21})
print(s, s2)
#intersection prints common numbers
#union prints all numbers
s.add(1)
print(s)
s.remove(10)
print(s)

print("IF ELSE ELSEIF")
var1 = 12
var2 = 12
#var3 = int(input())

if var2>var1:
    print("greater")
elif var2==var1:
    print("equal")
else:
    print("lesser")
#to use equal you have to put two equal signs
list1 = [2, 222, 32, 54]
print(5 in list1)
if 5 in list1:
    print("yes it is in list")
else:
    print("no it is not in list")

print(2 not in list1)
if 2 in list1:
    print("yes it is")
else:
    print("not")
"""
u = input("enter:")
if u.isalpha():
    print("entered input is alpha")
elif u.isalnum():
    print("entered input is alnum")
elif u.istitle():
    print("input is title")
elif u.isupper():
    print("input is in upper case")
else:
    pass
"""

#nested statement
"""
b = input("what do you want:")
a = input("what cheese do you want:")
if b.lower() == "burger".lower():

    print(a)
    if a.lower() == "mozzarella".lower():
        print("your burger is ready")
    elif a.lower() == "processed".lower():
        print("your burger is ready")
    else:
        pass
elif b.lower() == "sandwich".lower():
    print(a)

    if a.lower() == "mozzarella".lower():
        print("your sandwich is ready")
    elif a.lower() == "processed".lower():
        print("your sandwich is ready")
    else:
        pass
else:
    pass
"""

#in and not in keywords when used in print statement print true or false

#if you only wants to execute only one statement use pass

a = 10
b = 12
if a > b:
    print("a is greater than b")
else:
    pass
print("FOR LOOP")
list4 = ["ram", "lakshman", "shatrughan", "bharat"]
for item in list4:
    print(item)
#using for you can print every item in the list at the same time

list1 = [["arjun", 5], ["bheem", 5], ["yudhinter", 9], ["nakul", 5], ["sahdev", 6]]
for name, letters in list1:
    print(name,"has alphabets equals to", letters)

#to typecast list to dictionary use dict

dict1 = dict(list1)
for name, letters in dict1.items():
    print(name, letters)
u = list(range(0, 9))
print(u)
#range function will create a range of numbers including first input and excluding second

#for calculating total you have to create a variable equal to zero

t = 0
for n in range(1,7):
    t = t + n
print(t)
#you can also use t += n insted  of t = t + n

print("WHILE LOOP")
i = 0
while(i<50):
    print(i)
    i = i + 2

ll = [12, 15, 5, -9, -8]
tt = 0
ii = 0
while ll[ii] > 0:
    tt += ll[ii]
    ii += 1
print(tt)
#it only works till the negative numbers are at the end of the list and the list contains al least one negative number


#range function create a range including first input but excluding second
#it can be typecasted to create a list

print("WHILE AND BREAK LOOP")

i = 0
while(True):
    if i<10:
        i = i + 1
        continue

    print(i)
    if(i==54):
        break
    i = i + 1

print("OPERATORS:")
o = ["arithmetic", "assignment", "comparision", "logical", "identity", "membership", "bitwise"]
for items in o:
    print(items)
#arithjmetic iperaors
print("10+20", 10 + 20)
print("10-20", 10 - 20)
print("10*20", 10 * 20)
print("10/20", 10 / 20)
print("10//20", 10 // 20)
print("10**20", 10 ** 20)
print("10%20", 10 % 20)

"""
// gives integer value
** gives raise to the power
% gives remainder
"""
#assignment operators
x =10
print(x)
x += 5
print(x)
x -=5
print(x)
x /= 5
print(x)
x *= 5
print(x)
x %= 5
print(x)

#comparision operator
y = 20
print(y > 20)
print(y < 20)
print(y != 20)
print(y >= 20)
print(y >= 20)
print(y == 20)
# != means not equal to

#logical operators
a = True
b = False
print(a and b)
print(a and a)
print(b and b)
print(b and a)
print(a or b)
print(b or b)
print(a or a)
print(b or a)
print(not a)
print(not b)

#identity operators
print(5 is 4)
print(5 is 5)
print(5 is not 4)
print(5 is not 5)

#membership operators
l1 = [54, 21, 3, 87, 65, 11]
print(1 in l1)
print(54 in l1)
print(4 not in  l1)
print(21 not in l1)

#bitwise operators
"""
0 = 00
1 = 01 
2 = 10 
3 = 11

and is &
or is |
"""
print(0 & 1)
print(2 & 3)
print(2 | 1)
print(3 | 1)

print("FUNCTION")
def fun1():
    print("you are in fun1")
fun1()

def fun2(a, b):
    print("sum", a + b)
fun2(5, 10)

def fun3(a, b):
    """this is doc string used to define a function as it is a function use to calculate the average"""
    avg = (a + b)/2
    print(avg)
    return  avg
v = fun3(55, 15)
print(v)
#return is used to store the value in a variable
print(fun3.__doc__)
#doc string is writtten the next line to the function

def fun4(b = "good night"):
    print(b.upper() + "!")
fun4("good morning")
fun4()
#if you put any value in the function it will use other wise it will use the default set by us using equals to sign
print("TRY EXCEPT")
"""
num1 = input("enter num1:")
num2 = input("enter num2:")
try:
    print("the sum of the above numbers is",
      int(num1) + int(num2))
except Exception as e:
    print(e)

print("using this try except function the programme will continue to work after giving the error")
"""

# File Io Basics
"""
"r" - Open file for reading - default
"w" - Open a file for writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""

f = open("file.txt", "rt")
content = f.read()
print(content)
print(f.readline())

f.close()

f = open("file2.txt", "w")
f.write("using write function\n")
f.close()

f = open("file2.txt", "a")
f.write("now using append function\n")
f.close()

#to find number of characters in the file
f = open("file2.txt", "a")
a = f.write("now finding number if characters in the file")
print(a)
f.close()
#using write mode will clear the file and only write what is entered next but using append it adds the entered text

#to read and write
f = open("file3.txt", "r+")
print(f.read())
f.write("now editing")
f.close()

f = open("file3.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.close()
#read line finction will print next line every time you use it
#tell function will tell the position of the file pointer


f = open("file3.txt")
print(f.readline())
f.seek(0)
print(f.readline())
f.seek(10)
print(f.readline())
f.close()
#seek function will replace the point to the input value

f = open("file3.txt")
print(f.readlines())
f.close()
#using readlines all the lines are printed at once

with open("file3.txt") as f:
    print(f.read())
#using with function you do not have to close the file

print("GLOBAL AND LOCAL VARIABLES")
l = 10 #global variable
def fun(n):
    b = 12 #local variable
    global l #to change a global variable global function is used
    l = l + 65
    print(b)
    print(l)
    print(n)
fun("l is global variable")
print(l)
