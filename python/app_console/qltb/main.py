from xml.dom.minidom import parse 
import xml.dom.minidom 
import os

class nhom:
    def __init__(self,manhom,ten):
        self.manhom=manhom
        self.ten=ten
    
    def Xuat(self):
        print("Mã: ",self.manhom)
        print("Tên: ",self.ten)

class thietbi:
    def __init__(self,matb,ten,manhom):
        self.matb=matb
        self.ten=ten
        self.manhom=manhom
    
    def Xuat(self):
        print("Mã thiết bị: ",self.matb)
        print("Tên: ",self.ten)
        print("Mã nhóm: ",self.manhom)

def DocFile(path,loai):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement

    if loai == 1:
        ds = collection.getElementsByTagName("nhom")
        ketqua = []

        for pt in ds:
            tag_id = pt.getElementsByTagName('ma')[0]
            id = tag_id.childNodes[0].data

            tag_name = pt.getElementsByTagName('ten')[0]
            name = tag_name.childNodes[0].data

            ntb = nhom(id, name)
            ketqua.append(ntb)

        return ketqua

    else:
        ds = collection.getElementsByTagName("thietbi")
        ketqua = []

        for pt in ds:
            tag_id = pt.getElementsByTagName('ma')[0]
            id = tag_id.childNodes[0].data

            tag_name = pt.getElementsByTagName('ten')[0]
            name = tag_name.childNodes[0].data

            manhom = pt.getAttribute("manhom")

            tb = thietbi(id, name, manhom)
            ketqua.append(tb)

        return ketqua

def main():
    pathntb=os.path.join(os.path.dirname(__file__), "nhomthietbi.xml")
    pathtb=os.path.join(os.path.dirname(__file__), "ThietBi.xml")

    DSnhom = DocFile(pathntb, 1)
    DStb = DocFile(pathtb, 2)

    while(True):
        print("0. Thoát")
        print("1. Xuất danh sách nhóm thiết bị")
        print("2. Xuất danh sách thiết bị")
        print("3. Lọc thiết bị theo nhóm")
        print("4. Xuất nhóm có thiết bị nhiều nhất")
        print("Mục bạn chọn: ",end='')
        muc=int(input())

        if muc==0:
            break
        elif muc==1:
            stt=1
            for ntb in DSnhom:
                print("Nhóm thiết bị thứ ",stt)
                ntb.Xuat()
                stt+=1
        elif muc==2:
            stt=1
            for tb in DStb:
                print("Thiết bị thứ ",stt)
                tb.Xuat()
                stt+=1
        elif muc==3:
            k=input("Nhập nhóm thiết bị: ")
            conhom=0
            for ntb in DSnhom:
                if k==ntb.manhom:
                    conhom=1
                    break
            if conhom==0:
                print("Nhóm không tồn tại")
            else:
                dem=0
                for tb in DStb:
                    if tb.manhom==k:
                        dem+=1
                        print("Thiết bị thứ ",dem)
                        tb.Xuat()
                if dem==0:
                    print("Nhóm này chưa có thiết bị")
        elif muc==4:
            nhommax=[]
            slmax=0
            for nhom in DSnhom:
                sltb=0
                for tb in DStb:
                    if tb.manhom==nhom.manhom:
                        sltb+=1
                if slmax < sltb:
                    slmax=sltb
                    nhommax=[]
                    nhommax.append(nhom)
                elif slmax==sltb:
                    nhommax.append(nhom)
            print("Nhóm có số lượng thiết bị nhiều nhất:")

            if len(nhommax) <= 1:
                nhommax[0].Xuat()
            else:
                stt=1
                for nhom in nhommax:
                    print("Nhóm thứ ",stt)
                    nhom.Xuat()
                    stt+=1

if __name__=="__main__":
    main()