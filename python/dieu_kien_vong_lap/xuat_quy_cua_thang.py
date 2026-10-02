# Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

thang=int(input("Thang="))
if thang in (1,2,3):print("Thang thuoc quy 1")
elif thang in (4,5,6): print("Thang thuoc quy 2")
elif thang in (7,8.9): print("Thang thuoc quy 3")
elif thang in (10,11,12): print("Thang thuoc quy 4")
else: print("Thang khong hop le")
