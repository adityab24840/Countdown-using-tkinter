from tkinter import *

t=0

def set_timer():
    global t
    t = t+int(e1.get())
    return t

def countdown():
    global t
    if t>0:
        l1.config(text=t)
        t=t-1
        l1.after(1000,countdown)
    else:
        print("End")
        l1.config("and Go!!")









root=Tk()


#design the gui
root.geometry("160x180")

l1=Label(root,font=("times 20"))
l1.grid(row=1,column=2)

#for taking time entry from user

times=StringVar()
e1=Entry(root,textvariable=times)
e1.grid(row=3,column=2)

b1=Button(root,text="Enter time",width="20",command=set_timer)
b1.grid(row=5, column=2,padx=20)

b2=Button(root,text="Start",width="20",command=countdown)
b2.grid(row=7, column=2, padx=20)

root.mainloop()


