"""
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:  
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.  
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.  
- Dòng 3 : gồm các số nguyên tố.  
- Dòng 4 : gồm các số không phải là số nguyên tố.  
M [] ={3,6,7,8,11,17,2,90,2,5,4,5,8} 
➔ 3, 7, 11,17, 5(2) ➔ 6 số lẻ 
"""

def NhapMang(a,n):
    for i in range(n):
        print("a[",i,"]= ",end='')
        a[i]=int(input())
def XuatMang(a):
    print(a)
def XuatSoLe(a,n):
    dem=0
    tmp=[]
    for i in range(n):
        if a[i]%2!=0:
            tmp.append(a[i])
            dem=dem+1
    if dem!=0:
        print("- Dong 1: ",end='')
        print(tmp,end='')
        print(", tong cong co ",dem,"so le.")
    else: print("Khong co so le nao.")
def XuatSoChan(a,n):
    dem=0
    tmp=[]
    for i in range(n):
        if a[i]%2==0:
            tmp.append(a[i])
            dem=dem+1
    if dem!=0:
        print("- Dong 2: ",end='')
        print(tmp,end='')
        print(", tong cong co ",dem,"so chan.")
    else: print("Khong co so chan nao.")
def ktSoNguyenTo(n):
    for i in range(2,n):
        if n%i==0:return False
    return True
def XuatSoNguyenTo(a,n):
    tmp=[]
    for i in range(n):
        if ktSoNguyenTo(a[i]):
            tmp.append(a[i])
    print("- Dong 3: ",end='')
    print(tmp)
def XuatSoKhongLaNguyenTo(a,n):
    tmp=[]
    for i in range(n):
        if ktSoNguyenTo(a[i])==False:
            tmp.append(a[i])
    print("- Dong 4: ",end='')
    print(tmp)
        
n=int(input("n= "))
a=[0]*n
NhapMang(a,n)
XuatMang(a,n)
XuatSoLe(a,n)
XuatSoChan(a,n)
XuatSoNguyenTo(a,n)
XuatSoKhongLaNguyenTo(a,n)