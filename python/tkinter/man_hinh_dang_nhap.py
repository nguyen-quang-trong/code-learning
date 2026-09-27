from tkinter import *

root=Tk()
root.withdraw()

hopthoai=Toplevel(root)
hopthoai.title("Enter New Password")

hopthoai.protocol("WM_DELETE_WINDOW", root.destroy)

khungNhap=Frame(hopthoai)
khungNhap.grid(row=0,column=0)
khungNut=Frame(hopthoai)
khungNut.grid(row=1,column=0)

lblOldPW=Label(khungNhap,text="Old Password:")
lblOldPW.grid(row=0,column=0,sticky="w")
lblNewPW=Label(khungNhap,text="New Password:")
lblNewPW.grid(row=1,column=0,sticky="w")
lblNewPWAgain=Label(khungNhap,text="Enter New Password Again:")
lblNewPWAgain.grid(row=2,column=0,sticky="w")

entryOldPW=Entry(khungNhap,show="*")
entryOldPW.grid(row=0,column=1)
entryNewPW=Entry(khungNhap,show="*")
entryNewPW.grid(row=1,column=1)
entryNewPWAgain=Entry(khungNhap,show="*")
entryNewPWAgain.grid(row=2,column=1)

btnOk=Button(khungNut,text="OK")
btnOk.grid(row=0,column=2)
btnCancel=Button(khungNut,text="Cancel")
btnCancel.grid(row=0,column=3)

root.mainloop()