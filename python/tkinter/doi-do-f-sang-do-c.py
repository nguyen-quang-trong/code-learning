from tkinter import *


def chuyen():
    doF = float(txtDoF.get())

    doC = (doF - 32) * 5 / 9

    lblKetQua.config(text=doC)


root = Tk()
root.title("Chuyển độ F thành độ C")


lblNhapDoF = Label(root, text="Nhập độ F")
lblNhapDoF.grid(row=0, column=0)

txtDoF = Entry(root)
txtDoF.grid(row=0, column=1)

btnChuyen = Button(root, text="Chuyển", command=chuyen)
btnChuyen.grid(row=1, column=1)

lblDoC = Label(root, text="Độ C")
lblDoC.grid(row=2, column=0)

lblKetQua = Label(root, text="Độ C ở đây")
lblKetQua.grid(row=2, column=1)


root.mainloop()