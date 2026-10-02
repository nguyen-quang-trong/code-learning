# Viết chương trình cho phép: 
# - Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên.
# - Xuất dòng bất kỳ nhập từ bàn phím.
# - Xuất cột bất kỳ từ bàn phím.
# - Xuất số MAX trong ma trận.

from random import randrange
def KhoiTaoMaTranNgauNhien(m,n):
    l=[]
    for i in range(m):
        dong=[]
        for j in range(n):
            dong.append(randrange(100))
        l.append(dong)
    return l
def XuatMaTran(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=' ')
        print()
def XuatDongBatKy(l,m,n):
    tmp=[]
    d=int(input("Nhap dong can xuat: "))
    d=d-1
    if d>=m:
        print("Khong co du lieu")
        return
    for i in range(m):
        if d!=i: continue
        for j in range(n):
            tmp.append(l[i][j])
        print("Dong ",d+1," co du lieu la:")
        print(tmp)
        return
def XuatCotBatKy(l,m,n):
    tmp=[]
    c=int(input("Nhap cot can xuat:"))
    c=c-1
    if c>=n:
        print("Khong co du lieu")
        return
    for i in range(m):
        for j in range(n):
            if c==j:
                tmp.append(l[i][j])
    print("Cot ",c+1," co du lieu la:")
    print(tmp)
def TimMax(l,m,n):
    max=l[0][0]
    for i in range(m):
        for j in range(n):
            if l[i][j]>max:max=l[i][j]
    return max

m=int(input("Nhap so dong: "))
n=int(input("Nhap so cot: "))
l=KhoiTaoMaTranNgauNhien(m,n)
XuatMaTran(l,m,n)
XuatDongBatKy(l,m,n)
XuatCotBatKy(l,m,n)
print("Max trong ma tran la: ",TimMax(l,m,n))