import math
a=float(input("Nhập a= "))
b=float(input("Nhập b= "))
c=float(input("Nhập c= "))
d=(b*b)-4*a*c
if(d<0): print("Pt vô nghiệm")
elif(d==0): print("Pt có 1 nghiệm kép: ",-b/(2*a))
else:
    n1=(-b+math.sqrt(d))/(2*a)
    n2=(-b-math.sqrt(d))/(2*a)
    print("Pt có 2 nghiệm: x1= ",n1,", x2= ",n2)
