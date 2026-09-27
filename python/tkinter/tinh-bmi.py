from tkinter import *


def tinhBMI():
    chieuCao = float(txtChieuCao.get())
    canNang = float(txtCanNang.get())

    bmi = canNang / (chieuCao * chieuCao)

    txtBMI.delete(0, END)
    txtBMI.insert(0, round(bmi, 2))

    if bmi < 18.5:
        tinhTrang = "Gầy"
        nguyCo = "Thấp"

    elif bmi < 25:
        tinhTrang = "Bình thường"
        nguyCo = "Bình thường"

    elif bmi < 30:
        tinhTrang = "Mập"
        nguyCo = "Hơi cao"

    else:
        tinhTrang = "Béo phì"
        nguyCo = "Cao"

    txtTinhTrang.delete(0, END)
    txtTinhTrang.insert(0, tinhTrang)

    txtNguyCo.delete(0, END)
    txtNguyCo.insert(0, nguyCo)


def thoat():
    root.destroy()


root = Tk()
root.title("Tính BMI")


lblChieuCao = Label(root, text="Nhập chiều cao:")
lblChieuCao.grid(row=0, column=0)

txtChieuCao = Entry(root)
txtChieuCao.grid(row=0, column=1)


lblCanNang = Label(root, text="Nhập cân nặng:")
lblCanNang.grid(row=1, column=0)

txtCanNang = Entry(root)
txtCanNang.grid(row=1, column=1)


btnTinhBMI = Button(root, text="Tính BMI", command=tinhBMI)
btnTinhBMI.grid(row=2, column=1)


lblBMI = Label(root, text="BMI của bạn:")
lblBMI.grid(row=3, column=0)

txtBMI = Entry(root)
txtBMI.grid(row=3, column=1)


lblTinhTrang = Label(root, text="Tình trạng của bạn:")
lblTinhTrang.grid(row=4, column=0)

txtTinhTrang = Entry(root)
txtTinhTrang.grid(row=4, column=1)


lblNguyCo = Label(root, text="Nguy cơ phát triển bệnh:")
lblNguyCo.grid(row=5, column=0)

txtNguyCo = Entry(root)
txtNguyCo.grid(row=5, column=1)


btnThoat = Button(root, text="Thoát", command=thoat)
btnThoat.grid(row=6, column=1)


root.mainloop()