# Viết chương trình cho phép: 
# - Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list.
# - Gọi k là một số nhập từ bàn phím , hãy xóa tất cả các phần tử có giá trị k tồn tại trong list.
# - Kiểm tra list có đối xứng hay không.

from random import randrange
def KhoiTaoDSNgauNhien(n):
    l=[]
    for i in range(n):
        l.append(randrange(0,100))
    return l
def XoaPhanTuCoGiaTriK(l):
    k=int(input("k= "))
    while l.count(k)>0: l.remove(k)
    return l
def ktDSDoiXung(l,n):
    for i in range(n):
        if l[i]!=l[len(l)-i-1]:return False
    return True

n=int(input("n= "))
l=KhoiTaoDSNgauNhien(n)
print("Danh sach sau khi tao ngau nhien:")
print(l)
l=XoaPhanTuCoGiaTriK(l)
print("Danh sach sau khi xoa phan tu k:")
print(l)
if ktDSDoiXung(l,n): print("Chuoi doi xung")
else: print("Chuoi khong doi xung")