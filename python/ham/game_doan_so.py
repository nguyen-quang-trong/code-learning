# Máy ra 1 số trong đoạn [1...100].
# Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn số của máy và hiển thị số lần đoán.
# Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
# Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?

from random import randrange
def DoanSo():
    somay=randrange(1,101)
    solandoan=0
    while solandoan<7:
        songuoi=int(input("Ban doan so may tu 1 den 100: "))
        if songuoi==somay:
            print("Chuc mung ban")
            break
        elif songuoi>somay: print("Ban da sai, so nguoi > so may")
        else: print("Ban da sai, so nguoi < so may")
        solandoan+=1
    if solandoan >=7: print("Game over!")

while True:
    DoanSo()
    hoi=int(input("Tiep khong? <0:khong/1:tiep> "))
    if hoi==0: break
print("Cam on ban da choi")