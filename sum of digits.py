i = input("enter a number of more than one digit number: ")

t = 0
u = 0
q = len(i)
q = int(q)
while (u < q):

    p = i[u]
    p = int(p)
    t += p
    u += 1

print(t)