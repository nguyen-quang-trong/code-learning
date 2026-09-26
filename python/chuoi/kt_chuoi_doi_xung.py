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