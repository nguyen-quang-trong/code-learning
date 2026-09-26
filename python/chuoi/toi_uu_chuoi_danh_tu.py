"""
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa 
"""

def ToiUuChuoiDanhTu(s):
    tmp=""
    for i in range(len(s)):
        if s[i]==" " and (tmp=="" or s[i-1]==" "): continue
        else: tmp=tmp+s[i]
    s=tmp
    if tmp[len(tmp)-1]==" ":
        s=""
        for i in range(len(tmp)-1): s=s+tmp[i]
    return s.title()

s=input("Nhap chuoi: ")
print("Toi uu chuoi danh tu:",ToiUuChuoiDanhTu(s)," - ",len(ToiUuChuoiDanhTu(s)))