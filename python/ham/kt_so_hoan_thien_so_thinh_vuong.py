# Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
# a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không? 
# - Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
# - Vd: 6 có các ước số là 1,2,3 và 6=1+2+3 ➔ 6 là số hoàn thiện.
# b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (A bundant number)hay không? 
# - Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó.
# - Vd: 12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 ➔ 12 là số thịnh vượng.

def TinhTongUoc(n):
    t=0
    for i in range(1,n):
        if n%i==0:t=t+i
    return t
def ktSoHoanThien(n):
    if n==TinhTongUoc(n):return True
    return False
def ktSoThinhVuong(n):
    if n<TinhTongUoc(n):return True
    return False
n=int(input("n= "))
if ktSoHoanThien==True: print("Day la so hoan thien")
else: print("Day khong la so hoan thien")
if ktSoThinhVuong==True: print("Day la so thinh vuong")
else: print("Day khong la so thinh vuong")