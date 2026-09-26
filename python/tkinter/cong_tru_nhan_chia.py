from tkinter import *

root=Tk()

lblTitle=Label(root,text="Cộng trừ nhân chia")
lblTitle.grid(row=0,column=0)

def Cong():
    a = float(entrySoA.get())
    b = float(entrySoB.get())

    if entryKQ.get() != "":
        entryKQ.delete(0, "end")

    entryKQ.insert(0, str(a + b))

def Tru():
    a = float(entrySoA.get())
    b = float(entrySoB.get())

    if entryKQ.get() != "":
        entryKQ.delete(0, "end")

    entryKQ.insert(0, str(a - b))

def Nhan():
    a = float(entrySoA.get())
    b = float(entrySoB.get())

    if entryKQ.get() != "":
        entryKQ.delete(0, "end")

    entryKQ.insert(0, str(a * b))

def Chia():
    a = float(entrySoA.get())
    b = float(entrySoB.get())

    if entryKQ.get() != "":
        entryKQ.delete(0, "end")

    if b == 0:
        entryKQ.insert(0, "Không thể chia cho 0")
    else:
        entryKQ.insert(0, str(a / b))

def Thoat():
    root.destroy()

btnCong=Button(root,text="Cộng",command=Cong)
btnCong.grid(row=1,column=0)
btnTru=Button(root,text="Trừ",command=Tru)
btnTru.grid(row=2,column=0)
btnNhan=Button(root,text="Nhân",command=Nhan)
btnNhan.grid(row=3,column=0)
btnChia=Button(root,text="Chia",command=Chia)
btnChia.grid(row=4,column=0)
btnThoat=Button(root,text="thoát",command=Thoat)
btnThoat.grid(row=4,column=2)

lblSoA=Label(root,text="số a:")
lblSoA.grid(row=1,column=1)
lblSoB=Label(root,text="số b:")
lblSoB.grid(row=2,column=1)
lblKQ=Label(root,text="kết quả:")
lblKQ.grid(row=3,column=1)

entrySoA=Entry(root)
entrySoA.grid(row=1,column=2)
entrySoB=Entry(root)
entrySoB.grid(row=2,column=2)
entryKQ=Entry(root)
entryKQ.grid(row=3,column=2)

root.mainloop()