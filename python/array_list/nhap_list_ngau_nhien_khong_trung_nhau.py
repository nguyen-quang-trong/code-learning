from random import randrange

n=int(input("Nhap n= "))
l=[]
if n<=50: l.append(randrange(100))
else: l.append(randrange(n*2))
i=0
while i<n:
    if n<=50: x=randrange(100)
    else: x=randrange(n*2)
    for j in range(len(l)):
        if x==l[j]:break
        if j==i:
            l.append(x)
            i+=1
print(l)