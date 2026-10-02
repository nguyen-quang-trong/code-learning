# Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong.

l=[]
l.append(int(input("Nhap mot so: ")))
i=0
while True:
    a=int(input("Nhap mot so lon hon: "))
    if a>l[i]:
        l.append(a)
        i+=1
    else:continue
    ask=int(input("Ban co muon tiep tuc nhap khong? <0:khong/1:co> "))
    if ask==0:break
print(l)