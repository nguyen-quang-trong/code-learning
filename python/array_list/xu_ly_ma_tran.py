"""
Nhập 2 matrix A , B. 
Cộng 2 matrix 
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A , B 
"""

def Nhap(a,d,c):
    for i in range(d):
        cot=[]
        for j in range(c):
            print("Phan tu [",i,"][",j,"]: ",end='')
            cot.append(int(input()))
        a.append(cot)
    return a

def CongHaiMaTran(a,b,d,c):
    mtt=[]
    for i in range(d):
        dongA=a[i]
        dongB=b[i]
        tmp=[]
        for j in range(c):
            tmp.append(dongA[j]+dongB[j])
        mtt.append(tmp)
    print(mtt)

def HoanVi(a, d, c):
    mtt = []

    for j in range(c):
        dong = []

        for i in range(d):
            dong.append(a[i][j])

        mtt.append(dong)

    print(mtt)

a=[]
b=[]
da=int(input("Dong cua ma tran A: "))
ca=int(input("Cot cua ma tran A: "))
print("Nhap ma tran A:")
a=Nhap(a,da,ca)
print("Nhap ma tran B:")
b=Nhap(b,da,ca)
print("Ma tran A:")
print(a)
print("Ma tran B:")
print(b)
print("Ma tran A+B:")
CongHaiMaTran(a,b,da,ca)
print("Ma tran A hoan vi:")
HoanVi(a,da,ca)
print("Ma tran B hoan vi:")
HoanVi(b,da,ca)