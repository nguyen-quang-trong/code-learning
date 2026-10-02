# Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).

ngay=int(input("ngay= "))
thang=int(input("thang= "))
nam=int(input("nam= "))

if ngay==31 and thang==12:
    ngay=1
    thang=1
    nam=nam+1
elif ngay==31 and thang in (1,3,5,7,8,10):
    ngay=1
    thang=thang+1
elif ngay==30 and thang in (4,6,9,11):
    ngay=1
    thang=thang+1
elif (ngay==28 or ngay==29) and thang==2:
    ngay=1
    thang=3
elif ngay>=1 and ngay<31 and thang in (1,3,5,7,8,10):
    ngay=ngay+1
elif ngay>=1 and ngay<30 and thang in (4,6,9,11):
    ngay=ngay+1
elif ngay>=1 and (ngay<28 or ngay<29) and thang==2:
    ngay=ngay+1
print(ngay,"/",thang,"/",nam)
