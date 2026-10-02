# Dùng vòng lặp while vĩnh cửu, cho phép Nhập vào một Chuỗi ➔ Xuất Chuỗi này có phải đối xứng hay không? Hỏi người sử dụng có tiếp tục phần mềm. Nếu tiếp tục thì nhập Chuỗi mới, còn không thì thoát và thông báo cảm ơn.

def ktDoiXung(chuoi):
    for i in range(len(chuoi)):
        if chuoi[i]!=chuoi[len(chuoi)-i-1]:
            return False
    return True

while True:
    chuoi=input("Nhap chuoi: ")
    if ktDoiXung(chuoi): print("Chuoi doi xung")
    else: print("Chuoi khong doi xung")
    tt=int(input("Tiep tuc khong? <0:khong/1:co> "))
    if tt==0:break
print("Cam on")