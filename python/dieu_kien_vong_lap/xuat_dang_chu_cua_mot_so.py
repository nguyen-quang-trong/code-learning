# Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
# Vd: n=35 => Ba mươi lăm; n=5 => năm.

n=int(input("n= "))
if n>99: print("Số không hợp lệ")
else:
    print(" => ")
    if n==0:print("Không")
    elif n<10:
        if n==1:print("Một")
        elif n==2: print("Hai")
        elif n==3: print("Ba")
        elif n==4: print("Bốn")
        elif n==5: print("Năm")
        elif n==6: print("Sáu")
        elif n==7: print("Bảy")
        elif n==8: print("Tám")
        else: print("Chín")
    else:
        dv=n%10
        chuc=n//10
        if chuc==1:kq="Mười"
        elif chuc==2:kq="Hai mươi"
        elif chuc==3:kq="Ba mươi"
        elif chuc==4:kq="Bốn mươi"
        elif chuc==5:kq="Năm mươi"
        elif chuc==6:kq="Sáu mươi"
        elif chuc==7:kq="Bảy mươi"
        elif chuc==8:kq="Tám mươi"
        else:kq="Chín mươi"

        if dv==0:pass
        elif dv==1:
            if chuc==1: kq=kq+" một"
            else: kq=kq+" mốt"
        elif dv==2: kq=kq+" hai"
        elif dv==3: kq=kq+" ba"
        elif dv==4: kq=kq+" bốn"
        elif dv==5: kq=kq+" năm"
        elif dv==6: kq=kq+" sáu"
        elif dv==7: kq=kq+" bảy"
        elif dv==8: kq=kq+" tám"
        else: kq=kq+" chín"
        print(kq)
