"""
Viết chương trình nhập vào một dãy n số thực M [0], M [1],..., M [n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp
"""

n=int(input("Nhap n= "))
m=[]
for i in range(n):
    print("m[",i,"]= ",end='')
    m.append(float(input()))
for i in range(n-1):
    for j in range(i+1,n):
        if m[i]<m[j]: m[i],m[j]=m[j],m[i]
print("Mang sap xep giam dan la:")
print(m)