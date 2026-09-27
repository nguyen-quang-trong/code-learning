import os

class danhmuc:
    def __init__(self,madm,ten):
        self.madm=madm
        self.ten=ten
    
    def Nhap(self):
        self.madm=input("Mã danh mục: ")
        self.ten=input("Tên danh mục: ")
    
    def Xuat(self):
        print("Mã: ",self.madm)
        print("Tên: ",self.ten)

class sanpham:
    def __init__(self,masp,ten,dg,madm):
        self.masp=masp
        self.ten=ten
        self.dg=dg
        self.madm=madm

    def Nhap(self,DSdanhmuc):
        self.masp=input("Mã sản phẩm: ")
        self.ten=input("Tên sản phẩm: ")
        self.dg=input("Đơn giá: ")
        while(True):
            self.madm=input("Mã danh mục: ")
            codm=0
            for i in range(len(DSdanhmuc)):
                dm=DSdanhmuc[i]
                if self.madm==dm.madm:
                    codm=1
                    break
            if codm==1:
                break
            else:
                print("Danh mục không tồn tại, vui lòng nhập lại.")
    
    def Xuat(self):
        print("Mã sản phẩm: ",self.masp)
        print("Tên: ",self.ten)
        print("Đơn giá: ",self.dg)
        print("Mã danh mục: ",self.madm)

def LuuFile(path,data): 
    file=open(path,'w',encoding='utf-8') 
    for i in range(len(data)):
        file.writelines(data[i])
        file.writelines("\n") 
    file.close() 

def DocFile(path,tenlop): 
    ds=[]
    file=open(path,'r',encoding='utf-8')
    for line in file: 
        chuanhoa=line.strip() 
        data=chuanhoa.split(';')
        obj=tenlop(*data)
        ds.append(obj) 
    file.close() 
    return  ds

def main():
    DSdanhmuc=[]
    DSsanpham=[]

    pathdm = os.path.join(os.path.dirname(__file__), "danhmuc.txt")
    pathsp = os.path.join(os.path.dirname(__file__), "sanpham.txt")

    DSdanhmuc=DocFile(pathdm,danhmuc)
    DSsanpham=DocFile(pathsp,sanpham)

    while(True):
        print("0. Thoát")
        print("1. Thêm mới")
        print("2. Sửa")
        print("3. Xóa")
        print("4. Tìm kiếm")
        print("5. Sắp xếp")
        print("6. Lưu")
        print("7. Xuất danh mục và sản phẩm")
        print("Mục bạn chọn:",end='')
        muc=int(input())
        if muc==0:
            break
        elif muc==1:
            while(True):
                print("0. Trở lại")
                print("1. Thêm danh mục mới")
                print("2. Thêm sản phẩm mới")
                print("Mục bạn chọn:",end='')
                muc1=int(input())

                if muc1==0:
                    break
                elif muc1==1:
                    madm=input("Mã danh mục: ")
                    ten=input("Tên danh mục: ")
                    dm=danhmuc(madm,ten)
                    DSdanhmuc.append(dm)
                elif muc1==2:
                    masp=input("Mã sản phẩm: ")
                    ten=input("Tên sản phẩm: ")
                    dg=input("Đơn giá: ")
                    madm=""
                    while(True):
                        madm=input("Mã danh mục: ")
                        codm=0
                        for i in range(len(DSdanhmuc)):
                            dm=DSdanhmuc[i]
                            if madm==dm.madm:
                                codm=1
                                break
                        if codm==1:
                            break
                        else:
                            print("Danh mục không tồn tại, vui lòng nhập lại.")
                    sp=sanpham(masp,ten,dg,madm)
                    DSsanpham.append(sp)
        elif muc==2:
            while(True):
                print("0. Trở lại")
                print("1. Sửa danh mục")
                print("2. Sửa sản phẩm")
                print("Mục bạn chọn:",end='')
                muc2=int(input())
                
                if muc2==0:
                    break
                elif muc2==1:
                    k=input("Mã danh mục cần sửa: ")
                    timduoc=0
                    for i in range(len(DSdanhmuc)):
                        if k==DSdanhmuc[i].madm:
                            print("Sửa danh mục:")
                            DSdanhmuc[i].Nhap()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy danh mục cần sửa")
                elif muc2==2:
                    k=input("Mã sản phẩm cần sửa: ")
                    timduoc=0
                    for i in range(len(DSsanpham)):
                        if k==DSsanpham[i].masp:
                            print("Sửa sản phẩm:")
                            DSsanpham[i].Nhap(DSdanhmuc)
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sản phẩm cần sửa")

        elif muc==3:
            while(True):
                print("0. Trở lại")
                print("1. Xóa danh mục")
                print("2. Xóa sản phẩm")
                print("Mục bạn chọn:",end='')
                muc2=int(input())
                
                if muc2==0:
                    break
                elif muc2==1:
                    k=input("Mã danh mục cần xóa: ")
                    timduoc=0
                    dmcosp=0
                    for i in range(len(DSdanhmuc)):
                        if k==DSdanhmuc[i].madm:
                            timduoc=1
                            for j in range(len(DSsanpham)):
                                if DSsanpham[j].madm==k:
                                    dmcosp=1
                            if dmcosp==1:
                                print("Danh mục có tồn tại sản phẩm, không thể xóa")
                                break
                            DSdanhmuc.remove(DSdanhmuc[i])
                            break
                    if timduoc==0:
                        print("Không tìm thấy danh mục cần xóa")
                elif muc2==2:
                    k=input("Mã sản phẩm cần xóa: ")
                    timduoc=0
                    for i in range(len(DSsanpham)):
                        if k==DSsanpham[i].masp:
                            DSsanpham.remove(DSsanpham[i])
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sản phẩm cần xóa")
            
        elif muc==4:
            while(True):
                print("0. Trở lại")
                print("1. Tìm danh mục")
                print("2. Tìm sản phẩm")
                print("Mục bạn chọn:",end='')
                muc4=int(input())
                
                if muc4==0:
                    break
                elif muc4==1:
                    k=input("Mã danh mục cần tìm: ")
                    timduoc=0
                    for i in range(len(DSdanhmuc)):
                        if k==DSdanhmuc[i].madm:
                            print("Thông tin danh mục cần tìm:")
                            DSdanhmuc[i].Xuat()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy danh mục cần tìm")
                elif muc4==2:
                    k=input("Mã sản phẩm cần tìm: ")
                    timduoc=0
                    for i in range(len(DSsanpham)):
                        if k==DSsanpham[i].masp:
                            print("Thông tin sản phẩm cần tìm:")
                            DSsanpham[i].Xuat()
                            timduoc=1
                            break
                    if timduoc==0:
                        print("Không tìm thấy sản phẩm cần tìm")

        elif muc==5:
            for i in range(len(DSdanhmuc)-1):
                for j in range(i+1,len(DSdanhmuc)):
                    if DSdanhmuc[i].madm > DSdanhmuc[j].madm:
                        DSdanhmuc[i],DSdanhmuc[j]=DSdanhmuc[j],DSdanhmuc[i]

            for i in range(len(DSsanpham)-1):
                for j in range(i+1,len(DSsanpham)):
                    if DSsanpham[i].madm > DSsanpham[j].madm:
                        DSsanpham[i],DSsanpham[j]=DSsanpham[j],DSsanpham[i]

        elif muc==6:
            linedm=""
            datadm=[]
            for i in range(len(DSdanhmuc)):
                dm=DSdanhmuc[i]
                linedm=dm.madm+";"+dm.ten
                datadm.append(linedm)

            linesp=""
            datasp=[]
            for i in range(len(DSsanpham)):
                sp=DSsanpham[i]
                linesp=sp.masp+";"+sp.ten+";"+str(sp.dg)+";"+sp.madm
                datasp.append(linesp)
            
            LuuFile(pathdm,datadm)
            LuuFile(pathsp,datasp)
            print("Luu thanh cong")
            print()
        elif muc==7:
            print("Danh sách danh mục:")
            for i in range(len(DSdanhmuc)):
                dm=DSdanhmuc[i]
                print("Danh mục thứ ",i+1)
                dm.Xuat()
            print()
            print("Danh sách sản phẩm:")
            for i in range(len(DSsanpham)):
                sp=DSsanpham[i]
                print("Sản phẩm thứ ",i+1)
                sp.Xuat()

if __name__=="__main__":
    main()