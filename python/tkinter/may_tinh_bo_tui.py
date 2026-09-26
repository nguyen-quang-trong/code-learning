from tkinter import *

root=Tk()

bieuthuc=[]

def Them(kytunhap):
    tmp=""
    bieuthuc.append(kytunhap)
    for i in bieuthuc:
        if i=="--":
            i="-"
        tmp=tmp+i
    
    txtHienThi.delete("1.0",END)
    txtHienThi.insert("1.0",tmp)

def tinhtoanhaiso(a,b,pt):
    if pt=="+":
        return a+b
    elif pt=="-":
        return a-b
    elif pt=="*":
        return a*b
    elif pt=="/":
        return a/b

def tinh():
    chuanhoabt=[]
    so=""
    kqt=0
    for i in bieuthuc:
        if i in "0123456789" or i=="." or i=="--":
            if i=="--":
                i="-"
            so=so+i
        else:
            chuanhoabt.append(so)
            chuanhoabt.append(i)
            so=""
    if so!="":
        chuanhoabt.append(so)
    print(chuanhoabt)
    i=0
    while len(chuanhoabt)>1:
        conhanchia=0
        for j in range(len(chuanhoabt)):
            if chuanhoabt[j]=="*" or chuanhoabt[j]=="/":
                conhanchia=1
        
        if chuanhoabt[i]=="+" or chuanhoabt[i]=="-" or chuanhoabt[i]=="*" or chuanhoabt[i]=="/":
            if conhanchia==1:
                if chuanhoabt[i]=="+" or chuanhoabt[i]=="-":
                    i+=1
                    continue
            so1=float(chuanhoabt[i-1])
            so2=float(chuanhoabt[i+1])
            kqt=tinhtoanhaiso(so1,so2,chuanhoabt[i])
            chuanhoabt[i-1:i+2]=[kqt]
            i=0
        else:
            i+=1

    txtHienThi.delete("2.0",END)
    txtHienThi.insert("2.0","\n"+str(chuanhoabt[0]))

def xoa():
    tmp=""
    bieuthuc.pop()
    for i in bieuthuc:
        if i=="--":
            i="-"
        tmp=tmp+i
    
    txtHienThi.delete("1.0",END)
    txtHienThi.insert("1.0",tmp)


WIDTH_SO=7
WIDTH_PT=2

kq=0

txtHienThi=Text(root,width=WIDTH_PT*3+(WIDTH_PT+2)*2+16,height=2)
txtHienThi.grid(row=0,column=0)

khungSo = Frame(root)
khungSo.grid(row=1, column=0)
khungPhepTinh=Frame(root)
khungPhepTinh.grid(row=2,column=0)

btn1 = Button(khungSo, text="1",command=lambda: Them("1"),width=WIDTH_SO)
btn1.grid(row=1, column=0)

btn2 = Button(khungSo, text="2",command=lambda: Them("2"),width=WIDTH_SO)
btn2.grid(row=1, column=1)

btn3 = Button(khungSo, text="3",command=lambda: Them("3"),width=WIDTH_SO)
btn3.grid(row=1, column=2)

btn4 = Button(khungSo, text="4",command=lambda: Them("4"),width=WIDTH_SO)
btn4.grid(row=2, column=0)

btn5 = Button(khungSo, text="5",command=lambda: Them("5"),width=WIDTH_SO)
btn5.grid(row=2, column=1)

btn6 = Button(khungSo, text="6",command=lambda: Them("6"),width=WIDTH_SO)
btn6.grid(row=2, column=2)

btn7 = Button(khungSo, text="7",command=lambda: Them("7"),width=WIDTH_SO)
btn7.grid(row=3, column=0)

btn8 = Button(khungSo, text="8",command=lambda: Them("8"),width=WIDTH_SO)
btn8.grid(row=3, column=1)

btn9 = Button(khungSo, text="9",command=lambda: Them("9"),width=WIDTH_SO)
btn9.grid(row=3, column=2)

btnDauAm = Button(khungSo, text="-",command=lambda: Them("--"),width=WIDTH_SO)
btnDauAm.grid(row=4, column=0)

btn0 = Button(khungSo, text="0",command=lambda: Them("0"),width=WIDTH_SO)
btn0.grid(row=4, column=1)

btnCham = Button(khungSo, text=".",command=lambda: Them("."),width=WIDTH_SO)
btnCham.grid(row=4, column=2)

btnCong = Button(khungPhepTinh, text="+",command=lambda: Them("+"),width=WIDTH_PT)
btnCong.grid(row=1, column=0)

btnTru = Button(khungPhepTinh, text="-",command=lambda: Them("-"),width=WIDTH_PT)
btnTru.grid(row=1, column=1)

btnNhan = Button(khungPhepTinh, text="*",command=lambda: Them("*"),width=WIDTH_PT)
btnNhan.grid(row=1, column=2)

btnChia = Button(khungPhepTinh, text="/",command=lambda: Them("/"),width=WIDTH_PT)
btnChia.grid(row=1, column=3)

btnBang = Button(khungPhepTinh, text="=", command=tinh,width=WIDTH_PT+4)
btnBang.grid(row=1, column=4)

btnClr = Button(khungPhepTinh, text="Clr",command=xoa,width=WIDTH_PT*3+(WIDTH_PT+2)*2+14)
btnClr.grid(row=2, column=0,columnspan=5)

root.mainloop()