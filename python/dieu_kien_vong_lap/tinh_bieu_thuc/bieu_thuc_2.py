x=int(input("x="))
n=int(input("n="))
kq=0
for i in range (0,n+1):
    gt=1
    for j in range (1,2*i+2):
        gt=gt*j
    kq=kq+((x**(2*i+1))/gt)
print("kq=",kq)
