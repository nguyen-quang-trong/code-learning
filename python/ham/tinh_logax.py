import math
def TinhLogax(a,x):
    return math.log(x)/math.log(a)

a=float(input("Nhập cơ số a= "))
x=float(input("Nhập đối số x= "))
print("Loga(x)= ",TinhLogax(a,x))