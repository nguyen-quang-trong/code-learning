import os

class danhmuc:
    def __init__(self,madm,ten):
        self.madm=madm
        self.ten=ten
    
    # def Nhap(self):
    #     self.madm=input("Mã danh mục: ")
    #     self.ten=input("Tên danh mục: ")
    
    def Xuat(self):
        print("Mã: ",self.madm)
        print("Tên: ",self.ten)

class sanpham:
    def __init__(self,masp,ten,dg,madm):
        self.masp=masp
        self.ten=ten
        self.dg=dg
        self.madm=madm

    # def Nhap(self,DSdanhmuc):
    #     self.masp=input("Mã sản phẩm: ")
    #     self.ten=input("Tên sản phẩm: ")
    #     self.dg=input("Đơn giá: ")
    #     while(True):
    #         self.madm=input("Mã danh mục: ")
    #         codm=1
    #         for i in range(len(DSdanhmuc)):
    #             dm=DSdanhmuc[i]
    #             if self.madm==dm.madm:
    #                 codm=1
    #                 break
    #             codm=0
    #         if codm==1:
    #             break
    #         else:
    #             print("Danh mục không tồn tại, vui lòng nhập lại.")
    
    def Xuat(self):
        print("Mã sản phẩm: ",self.masp)
        print("Tên: ",self.ten)
        print("Đơn giá: ",self.dg)
        print("Mã danh mục: ",self.madm)

def LuuFile(path,data): 
    file=open(path,'a',encoding='utf-8') 
    file.writelines(data) 
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
                        codm=1
                        for i in range(len(DSdanhmuc)):
                            dm=DSdanhmuc[i]
                            if madm==dm.madm:
                                codm=1
                                break
                            codm=0
                        if codm==1:
                            break
                        else:
                            print("Danh mục không tồn tại, vui lòng nhập lại.")
                    sp=sanpham(masp,ten,dg,madm)
                    DSsanpham.append(sp)
        elif muc==2:
            break
        elif muc==3:
            break
        elif muc==4:
            break
        elif muc==5:
            break
        elif muc==6:
            linedm=""
            for i in range(len(DSdanhmuc)):
                dm=DSdanhmuc[i]
                linedm=dm.madm+";"+dm.ten

            linesp=""
            for i in range(len(DSsanpham)):
                sp=DSsanpham[i]
                linesp=sp.masp+";"+sp.ten+";"+str(sp.dg)+";"+sp.madm
            
            LuuFile(pathdm,linedm)
            LuuFile(pathsp,linesp)
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