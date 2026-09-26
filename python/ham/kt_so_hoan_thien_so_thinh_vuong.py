def TinhTongUoc(n):
    t=0
    for i in range(1,n):
        if n%i==0:t=t+i
    return t
def ktSoHoanThien(n):
    if n==TinhTongUoc(n):return True
    return False
def ktSoThinhVuong(n):
    if n<TinhTongUoc(n):return True
    return False
n=int(input("n= "))
if ktSoHoanThien==True: print("Day la so hoan thien")
else: print("Day khong la so hoan thien")
if ktSoThinhVuong==True: print("Day la so thinh vuong")
else: print("Day khong la so thinh vuong")