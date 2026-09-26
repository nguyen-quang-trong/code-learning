from tkinter import *
import math
root=Tk()
root.title('PTB2')
def GiaiPTB2():
    a=float(entry1.get())
    b=float(entry2.get())
    c=float(entry3.get())
    if entry4.get()!="": entry4.delete(0,"end")
    d=(b*b)-(4*a*c)
    if d<0: entry4.insert(0,"Vô nghiệm")
    elif d==0: entry4.insert(0,"Nghiệm kép x1=x2="+str(-b/(2*a)))
    else: entry4.insert(0,"x1="+str((-b+math.sqrt(d))/(2*a))+";x2="+str((-b-math.sqrt(d))/(2*a)))
    return
def GiaiTiep():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry3.delete(0,"end")
    entry4.delete(0,"end")
    return

label1=Label(root,text="Hệ số a:")
label1.grid(row=0,column=0,padx=10,pady=10)
entry1=Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=10)

label2=Label(root,text="Hệ số b:")
label2.grid(row=1,column=0,padx=1,pady=10)
entry2=Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=10)

label3=Label(root,text="Hệ số c:")
label3.grid(row=2,column=0,padx=1,pady=10)
entry3=Entry(root)
entry3.grid(row=2,column=1,padx=10,pady=10)

button=Button(root,text="Giải",command=GiaiPTB2)
button.grid(row=3,column=0,padx=10,pady=10)
button=Button(root,text="Tiếp",command=GiaiTiep)
button.grid(row=3,column=1,padx=10,pady=10)
button=Button(root,text="Thoát",command=root.quit)
button.grid(row=3,column=2,padx=10,pady=10)

label4=Label(root,text="Kết quả:")
label4.grid(row=4,column=0,padx=1,pady=10)
entry4=Entry(root)
entry4.grid(row=4,column=1,padx=10,pady=10)

root.mainloop()