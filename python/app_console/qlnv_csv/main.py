import csv
import os

class nhanvien:
    def __init__(self,manv,ten,tuoi):
        self.manv=manv
        self.ten=ten
        self.tuoi=tuoi
    def Xuat(self):
        print("Mã: ",self.manv)
        print("Tên: ",self.ten)
        print("Tuổi: ",self.tuoi)

def LuuFile(duongdan, DSnhanvien):
    with open(duongdan, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(["STT", "MÃ", "TÊN", "TUỔI"])

        stt = 1

        for nv in DSnhanvien:
            writer.writerow([
                stt,
                nv.manv,
                nv.ten,
                nv.tuoi
            ])
            stt += 1

def DocFile(duongdan):
    DSnhanvien = []

    with open(duongdan, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')

        next(reader)  # bỏ dòng tiêu đề

        for row in reader:
            stt, manv, ten, tuoi = row

            nv = nhanvien(manv, ten, tuoi)
            DSnhanvien.append(nv)

    return DSnhanvien

def main():
    duongdan=os.path.join(os.path.dirname(__file__), "nhanvien.csv")

    if os.path.exists(duongdan):
        DSnhanvien = DocFile(duongdan)
    else:
        DSnhanvien = []

    while(True):
        print("0. Thoát")
        print("1. Thêm")
        print("2. Xuất danh sách")
        print("3. Sắp xếp")
        print("4. Lưu")
        print("Mục bạn chọn: ",end='')
        muc=int(input())

        if muc==0:
            break
        elif muc==1:
            manv=input("Mã nhân viên: ")
            ten=input("Tên: ")
            tuoi=input("Tuổi: ")
            nv=nhanvien(manv,ten,tuoi)
            DSnhanvien.append(nv)
        elif muc==2:
            stt=1
            for nv in DSnhanvien:
                print("Nhân viên thứ ",stt)
                nv.Xuat()
                stt+=1
        elif muc==3:
            for i in range(len(DSnhanvien)-1):
                for j in range(i+1,len(DSnhanvien)):
                    if float(DSnhanvien[i].tuoi) > float(DSnhanvien[j].tuoi):
                        DSnhanvien[i], DSnhanvien[j]=DSnhanvien[j], DSnhanvien[i]
        elif muc==4:
            LuuFile(duongdan, DSnhanvien)
            print("Đã lưu file!")

if __name__=="__main__":
    main()