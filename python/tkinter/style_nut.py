from tkinter import *

root = Tk()
root.title("frame 2")

# ===== Dòng borderwidth = 0 =====

lblBW0 = Label(root, text="borderwidth = 0")
lblBW0.grid(row=0, column=0, sticky="w")

btnRaised0 = Button(root, text="raised", borderwidth=0, relief="raised")
btnRaised0.grid(row=0, column=1)

btnSunken0 = Button(root, text="sunken", borderwidth=0, relief="sunken")
btnSunken0.grid(row=0, column=2)

btnFlat0 = Button(root, text="flat", borderwidth=0, relief="flat")
btnFlat0.grid(row=0, column=3)

btnRidge0 = Button(root, text="ridge", borderwidth=0, relief="ridge")
btnRidge0.grid(row=0, column=4)

btnGroove0 = Button(root, text="groove", borderwidth=0, relief="groove")
btnGroove0.grid(row=0, column=5)

btnSolid0 = Button(root, text="solid", borderwidth=0, relief="solid")
btnSolid0.grid(row=0, column=6)

# ===== Dòng borderwidth = 1 =====

lblBW1 = Label(root, text="borderwidth = 1")
lblBW1.grid(row=1, column=0, sticky="w")

btnRaised1 = Button(root, text="raised", borderwidth=1, relief="raised")
btnRaised1.grid(row=1, column=1)

btnSunken1 = Button(root, text="sunken", borderwidth=1, relief="sunken")
btnSunken1.grid(row=1, column=2)

btnFlat1 = Button(root, text="flat", borderwidth=1, relief="flat")
btnFlat1.grid(row=1, column=3)

btnRidge1 = Button(root, text="ridge", borderwidth=1, relief="ridge")
btnRidge1.grid(row=1, column=4)

btnGroove1 = Button(root, text="groove", borderwidth=1, relief="groove")
btnGroove1.grid(row=1, column=5)

btnSolid1 = Button(root, text="solid", borderwidth=1, relief="solid")
btnSolid1.grid(row=1, column=6)

# ===== Dòng borderwidth = 2 =====

lblBW2 = Label(root, text="borderwidth = 2")
lblBW2.grid(row=2, column=0, sticky="w")

btnRaised2 = Button(root, text="raised", borderwidth=2, relief="raised")
btnRaised2.grid(row=2, column=1)

btnSunken2 = Button(root, text="sunken", borderwidth=2, relief="sunken")
btnSunken2.grid(row=2, column=2)

btnFlat2 = Button(root, text="flat", borderwidth=2, relief="flat")
btnFlat2.grid(row=2, column=3)

btnRidge2 = Button(root, text="ridge", borderwidth=2, relief="ridge")
btnRidge2.grid(row=2, column=4)

btnGroove2 = Button(root, text="groove", borderwidth=2, relief="groove")
btnGroove2.grid(row=2, column=5)

btnSolid2 = Button(root, text="solid", borderwidth=2, relief="solid")
btnSolid2.grid(row=2, column=6)

# ===== Dòng borderwidth = 3 =====

lblBW3 = Label(root, text="borderwidth = 3")
lblBW3.grid(row=3, column=0, sticky="w")

btnRaised3 = Button(root, text="raised", borderwidth=3, relief="raised")
btnRaised3.grid(row=3, column=1)

btnSunken3 = Button(root, text="sunken", borderwidth=3, relief="sunken")
btnSunken3.grid(row=3, column=2)

btnFlat3 = Button(root, text="flat", borderwidth=3, relief="flat")
btnFlat3.grid(row=3, column=3)

btnRidge3 = Button(root, text="ridge", borderwidth=3, relief="ridge")
btnRidge3.grid(row=3, column=4)

btnGroove3 = Button(root, text="groove", borderwidth=3, relief="groove")
btnGroove3.grid(row=3, column=5)

btnSolid3 = Button(root, text="solid", borderwidth=3, relief="solid")
btnSolid3.grid(row=3, column=6)

# ===== Dòng borderwidth = 4 =====

lblBW4 = Label(root, text="borderwidth = 4")
lblBW4.grid(row=4, column=0, sticky="w")

btnRaised4 = Button(root, text="raised", borderwidth=4, relief="raised")
btnRaised4.grid(row=4, column=1)

btnSunken4 = Button(root, text="sunken", borderwidth=4, relief="sunken")
btnSunken4.grid(row=4, column=2)

btnFlat4 = Button(root, text="flat", borderwidth=4, relief="flat")
btnFlat4.grid(row=4, column=3)

btnRidge4 = Button(root, text="ridge", borderwidth=4, relief="ridge")
btnRidge4.grid(row=4, column=4)

btnGroove4 = Button(root, text="groove", borderwidth=4, relief="groove")
btnGroove4.grid(row=4, column=5)

btnSolid4 = Button(root, text="solid", borderwidth=4, relief="solid")
btnSolid4.grid(row=4, column=6)

root.mainloop()