from tkinter import *

root=Tk()

root.title('PTB1')

def GiaiPTB1():
    a=float(entry1.get())
    b=float(entry2.get())
    if entry3.get()!="": entry3.delete(0,"end")
    if a==0 and b==0:
        entry3.insert(0,'Vô số nghiệm')
    elif a==0 and b!=0: entry3.insert(0,'Vô nghiệm')
    else: entry3.insert(0,"x="+str(-b/a))
    return
def GiaiTiep():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry3.delete(0,"end")
    return

label1=Label(root,text="Hệ số a:")
label1.grid(row=0,column=0,padx=10,pady=10)
entry1=Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=10)

label2=Label(root,text="Hệ số b:")
label2.grid(row=1,column=0,padx=1,pady=10)
entry2=Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=10)

button=Button(root,text="Giải",command=GiaiPTB1)
button.grid(row=2,column=0,padx=10,pady=10)
button=Button(root,text="Tiếp",command=GiaiTiep)
button.grid(row=2,column=1,padx=10,pady=10)
button=Button(root,text="Thoát",command=root.quit)
button.grid(row=2,column=2,padx=10,pady=10)

label3=Label(root,text="Kết quả:")
label3.grid(row=3,column=0,padx=1,pady=10)
entry3=Entry(root)
entry3.grid(row=3,column=1,padx=10,pady=10)

root.mainloop()