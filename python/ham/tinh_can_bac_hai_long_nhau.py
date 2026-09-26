import math
def TinhCanLongNhau(n):
    t=0
    for i in range(n):
        t=math.sqrt(2+t)
    return t
n=int(input("n= "))
print("Kq= ",TinhCanLongNhau(n))