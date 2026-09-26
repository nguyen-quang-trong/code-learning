"""
Viết chương trình cho phép: 
- Khởi tạo list 
- Thêm phần tử vào list 
- Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list 
- Tính tổng các số nguyên tố trong list 
- Sắp xếp 
- Xóa list
"""

def NhapDS(l,n):
    for i in range(n):
        print("Phan tu thu ",i,": ",end='')
        l[i]=int(input())
    return l
def XuatDS(l,n):
    for i in range(n):
        print(l[i],end=' ')
def demSoK(l,n):
    k=int(input("Nhap k= "))
    dem=0
    for i in range(n):
        if k==l[i]:dem=dem+1
    print("So ",k," xuat hien ",dem," lan trong danh sach")
def ktSoNguyenTo(n):
    if n<=0: return False
    for i in range(2,n):
        if n%i==0: return False
    return True
def TinhTongCacSoNguyenTo(l,n):
    t=0
    for i in range(n):
        if ktSoNguyenTo(l[i]):t=t+l[i]
    return t
def SapXepTang(l,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i]>l[j]:
                l[i], l[j]=l[j], l[i]
    return l

n=int(input("Nhap n= "))
list=[0]*n
list=NhapDS(list,n)
print("Danh sach vua nhap: ",end='')
XuatDS(list,n)
print()
demSoK(list,n)
print("Tong cac so nguyen to trong danh sach: ",TinhTongCacSoNguyenTo(list,n))
list=SapXepTang(list,n)
print("Danh sach sau khi sap xep tang: ",end='')
XuatDS(list,n)
print()
del list
print("Danh sach sau khi xoa:",end='')
XuatDS(list,n)
print()