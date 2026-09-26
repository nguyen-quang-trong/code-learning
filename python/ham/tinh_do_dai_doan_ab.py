import math
def TinhDoDai(xa,ya,xb,yb):
    return math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya))

xa=float(input("xa= "))
ya=float(input("ya= "))
xb=float(input("xb= "))
yb=float(input("yb= "))

print("Do dai doan AB: ",TinhDoDai(xa,ya,xb,yb))