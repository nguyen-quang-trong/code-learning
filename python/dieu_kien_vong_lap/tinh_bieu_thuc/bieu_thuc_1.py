x=int(input("x="))
n=int(input("n="))
if n<= 0: print("n khong hop le")
else:
    tong=0
    for i in range(1,n+1):
        gt=1
        for j in range (1,i+1): gt=gt*j
        tong=tong+((x**i)/gt)
    print("Ket qua:",tong)
