from tkinter import *
import tkinter.font as f
def radio():
    selection = "your Qualification is " +str(v.get())
    t = Text(a,height=12,width=40)
    t.insert(INSERT, selection)
    t.pack(side=BOTTOM)
a= Tk()
d = f.Font(family='Times New Roman', size=24, weight='bold')
l1=Label(a,text="CHOOSE YOUR QUALIFICATION:",fg="red")
l1.pack()
l1['font']=d
v = StringVar()
x1 = Radiobutton(a, text="UG", variable=v, value="UG",command=radio)
x2 = Radiobutton(a, text="PG", variable=v, value="PG",command=radio)
x1.pack( )
x2.pack( )