from tkinter import *

def chuyen():
    nam = int(txtNamDuong.get())

    can = [
        "Giáp", "Ất", "Bính", "Đinh", "Mậu",
        "Kỷ", "Canh", "Tân", "Nhâm", "Quý"
    ]

    chi = [
        "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
        "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
    ]

    tenCan = can[(nam - 4) % 10]
    tenChi = chi[(nam - 4) % 12]

    lblNamAm.config(text=tenCan + " " + tenChi)


root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")


lblNamDuong = Label(root, text="Nhập năm dương:")
lblNamDuong.grid(row=0, column=0)

txtNamDuong = Entry(root)
txtNamDuong.grid(row=0, column=1)

btnChuyen = Button(root, text="Chuyển", command=chuyen)
btnChuyen.grid(row=1, column=1)

lblKetQua = Label(root, text="Năm âm:")
lblKetQua.grid(row=2, column=0)

lblNamAm = Label(root, text="")
lblNamAm.grid(row=2, column=1)


root.mainloop()