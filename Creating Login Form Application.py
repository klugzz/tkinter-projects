from tkinter import *
from tkinter import messagebox
def login():
    user=str(Entry.get(t1))
    pass1=int(Entry.get(t2))
    if user == "admin" and pass1==12345:
        messagebox.showinfo("Result","LOGIN SUCCESSFULLY")
    else:
        messagebox.showinfo("Error","INCORRECT USERNAME OR PASSWORD...TRY AGAIN!")
a=Tk()
l1=Label(a,text="USERNAME").place(x=20,y=30)
t1=Entry(a,bd=3)
t1.place(x=100,y=30)
l2=Label(a,text="PASSWORD").place(x=20,y=70)
t2=Entry(a,bd=3)
t2.place(x=100,y=70)
b=Button(a,text="LOGIN",command=login).place(x=100,y=100)