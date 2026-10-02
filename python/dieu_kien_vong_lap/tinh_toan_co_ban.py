# Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.

a=int(input("a= "))
b=int(input("b= "))
pt=str(input("Phep toan: "))
if pt=="/":
    if b==0: print("Khong the chia cho 0")
    else: print("Ket qua:",a/b)
else:
    if pt=="+": kq=a+b
    elif pt=="-":kq=a-b
    elif pt=="*":kq=a*b
    print("Ket qua:",kq)
