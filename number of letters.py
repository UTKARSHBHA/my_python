name = input("enter your name: ")

i = len(name)
u = 0
temp = ""
while u < i:
    p = name[u]
    q = name.count(p)

    if p not in temp:
        print(f"{p} is {q} times in {name}" )
    temp += p
    u += 1