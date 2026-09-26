import math
def TinhDTTG(a,b,c):
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

if (a<=0 or b<=0 or c<=0) or (a+b)<=c or (b+c)<=a or (a+c)<=b:
    print("Day khong la tam giac")
else:
    print("Dien tich tam giac: ",TinhDTTG(a,b,c))