import os
import json

class lophoc:
    def __init__(self,malop,ten):
        self.malop=malop
        self.ten=ten
    
    def Nhap(self):
        self.malop=input("Mã lớp: ")
        self.ten=input("Tên lớp: ")
    
    def Xuat(self):
        print("Mã: ",self.malop)
        print("Tên: ",self.ten)

class sinhvien:
    def __init__(self,masv,ten,ns,malop):
        self.masv=masv
        self.ten=ten
        self.ns=ns
        self.malop=malop

    def Nhap(self,DSlophoc):
        self.masv=input("Mã sinh viên: ")
        self.ten=input("Tên sinh viên: ")
        self.ns=input("Năm sinh: ")
        while(True):
            self.malop=input("Mã lớp: ")
            colop=0
            for i in range(len(DSlophoc)):
                lh=DSlophoc[i]
                if self.malop==lh.malop:
                    colop=1
                    break
            if colop==1:
                break
            else:
                print("Lớp học không tồn tại, vui lòng nhập lại.")
    
    def Xuat(self):
        print("Mã sinh viên: ",self.masv)
        print("Tên: ",self.ten)
        print("Năm sinh: ",self.ns)
        print("Mã lớp: ",self.malop)

# def LuuFile(path,data): 
#     file=open(path,'w',encoding='utf-8') 
#     for i in range(len(data)):
#         file.writelines(data[i])
#         file.writelines("\n") 
#     file.close() 

# def DocFile(path,tenlop): 
#     ds=[]
#     file=open(path,'r',encoding='utf-8')
#     for line in file: 
#         chuanhoa=line.strip() 
#         data=chuanhoa.split(';')
#         obj=tenlop(*data)
#         ds.append(obj) 
#     file.close() 
#     return  ds

def LuuFile(path, data):
    dulieu = []

    for obj in data:
        dulieu.append(obj.__dict__)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(dulieu, file, ensure_ascii=False, indent=4)

def DocFile(path, tenlop):
    ds = []

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        obj = tenlop(**item)
        ds.append(obj)

    return ds

def main():
    DSlophoc=[]
    DSsinhvien=[]

    pathlh = os.path.join(os.path.dirname(__file__), "lophoc.json")
    pathsv = os.path.join(os.path.dirname(__file__), "sinhvien.json")

    DSlophoc=DocFile(pathlh,lophoc)
    DSsinhvien=DocFile(pathsv,sinhvien)

    while(True):
        print("0. Thoát")
        print("1. Thêm mới")
        print("2. Sửa")
        print("3. Xóa")
        print("4. Tìm kiếm")
        print("5. Sắp xếp")
        print("6. Lưu")
        print("7. Xuất lớp học và sinh viên")
        print("Mục bạn chọn:",end='')
        muc=int(input())
        if muc==0:
            break
        elif muc==1:
            while(True):
                print("0. Trở lại")
                print("1. Thêm lớp học mới")
                print("2. Thêm sinh viên mới")
                print("Mục bạn chọn:",end='')
                muc1=int(input())

                if muc1==0:
                    break
                elif muc1==1:
                    malop=input("Mã lớp: ")
                    ten=input("Tên lớp: ")
                    lh=lophoc(malop,ten)
                    DSlophoc.append(lh)
                elif muc1==2:
                    masv=input("Mã sinh viên: ")
                    ten=input("Tên sinh viên: ")
                    ns=input("Năm sinh: ")
                    malop=""
                    while(True):
                        malop=input("Mã lớp: ")
                        colop=0
                        for i in range(len(DSlophoc)):
                            lh=DSlophoc[i]
                            if malop==lh.malop:
                                colop=1
                                break
                        if colop==1:
                            break
                        else:
                            print("lớp học không tồn tại, vui lòng nhập lại.")
                    sv=sinhvien(masv,ten,ns,malop)
                    DSsinhvien.append(sv)
        elif muc==2:
            while(True):
                print("0. Trở lại")
                print("1. Sửa lớp học")
                print("2. Sửa sinh viên")
                print("Mục bạn chọn:",end='')
                muc2=int(input())
                
                if muc2==0:
                    break
                elif muc2==1:
                    k=input("Mã lớp cần sửa: ")
                    timduoc=0
                    for i in range(len(DSlophoc)):
                        if k==DSlophoc[i].malop:
                            print("Sửa lớp học:")
                            DSlophoc[i].Nhap()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy lớp học cần sửa")
                elif muc2==2:
                    k=input("Mã sinh viên cần sửa: ")
                    timduoc=0
                    for i in range(len(DSsinhvien)):
                        if k==DSsinhvien[i].masv:
                            print("Sửa sinh viên:")
                            DSsinhvien[i].Nhap(DSlophoc)
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sinh viên cần sửa")

        elif muc==3:
            while(True):
                print("0. Trở lại")
                print("1. Xóa lớp học")
                print("2. Xóa sinh viên")
                print("Mục bạn chọn:",end='')
                muc2=int(input())
                
                if muc2==0:
                    break
                elif muc2==1:
                    k=input("Mã lớp cần xóa: ")
                    timduoc=0
                    lhcosv=0
                    for i in range(len(DSlophoc)):
                        if k==DSlophoc[i].malop:
                            timduoc=1
                            for j in range(len(DSsinhvien)):
                                if DSsinhvien[j].malop==k:
                                    lhcosv=1
                            if lhcosv==1:
                                print("lớp học có tồn tại sinh viên, không thể xóa")
                                break
                            DSlophoc.remove(DSlophoc[i])
                            break
                    if timduoc==0:
                        print("Không tìm thấy lớp học cần xóa")
                elif muc2==2:
                    k=input("Mã sinh viên cần xóa: ")
                    timduoc=0
                    for i in range(len(DSsinhvien)):
                        if k==DSsinhvien[i].masv:
                            DSsinhvien.remove(DSsinhvien[i])
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sinh viên cần xóa")
            
        elif muc==4:
            while(True):
                print("0. Trở lại")
                print("1. Tìm lớp học")
                print("2. Tìm sinh viên")
                print("Mục bạn chọn:",end='')
                muc4=int(input())
                
                if muc4==0:
                    break
                elif muc4==1:
                    k=input("Mã lớp cần tìm: ")
                    timduoc=0
                    for i in range(len(DSlophoc)):
                        if k==DSlophoc[i].malop:
                            print("Thông tin lớp học cần tìm:")
                            DSlophoc[i].Xuat()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy lớp học cần tìm")
                elif muc4==2:
                    k=input("Mã sinh viên cần tìm: ")
                    timduoc=0
                    for i in range(len(DSsinhvien)):
                        if k==DSsinhvien[i].masv:
                            print("Thông tin sinh viên cần tìm:")
                            DSsinhvien[i].Xuat()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sinh viên cần tìm")

        elif muc==5:
            for i in range(len(DSlophoc)-1):
                for j in range(i+1,len(DSlophoc)):
                    if DSlophoc[i].malop > DSlophoc[j].malop:
                        DSlophoc[i],DSlophoc[j]=DSlophoc[j],DSlophoc[i]

            for i in range(len(DSsinhvien)-1):
                for j in range(i+1,len(DSsinhvien)):
                    if DSsinhvien[i].malop > DSsinhvien[j].malop:
                        DSsinhvien[i],DSsinhvien[j]=DSsinhvien[j],DSsinhvien[i]

        elif muc==6:
            # linelh=""
            # datalh=[]
            # for i in range(len(DSlophoc)):
            #     lh=DSlophoc[i]
            #     linelh=lh.malop+";"+lh.ten
            #     datalh.append(linelh)

            # linesv=""
            # datasv=[]
            # for i in range(len(DSsinhvien)):
            #     sv=DSsinhvien[i]
            #     linesv=sv.masv+";"+sv.ten+";"+str(sv.ns)+";"+sv.malop
            #     datasv.append(linesv)
            
            # LuuFile(pathlh,datalh)
            # LuuFile(pathsv,datasv)
            LuuFile(pathlh, DSlophoc)
            LuuFile(pathsv, DSsinhvien)

            print("Lưu thành công")
            print()
        elif muc==7:
            print("Danh sách lớp học:")
            for i in range(len(DSlophoc)):
                lh=DSlophoc[i]
                print("lớp học thứ ",i+1)
                lh.Xuat()
            print()
            print("Danh sách sinh viên:")
            for i in range(len(DSsinhvien)):
                sv=DSsinhvien[i]
                print("sinh viên thứ ",i+1)
                sv.Xuat()

if __name__=="__main__":
    main()