from tkinter import *
import tkinter.font as f
a = Tk()
d = f.Font(family='Times New Roman', size=24, weight='bold')
e = f.Font(family='Times New Roman', size=18, weight='bold')
l1=Label(a,text="WELCOME TO SYSTECH ",fg="red")
l1.pack()
l1['font']=d
l2=Label(a,text="STUDENT FORM",fg="blue")
l2.pack()
l2['font']=e
def texting():
    global selection
    name=e1.get()
    age=int(e2.get())
    phone=int(e3.get())
    city=e4.get()
    l5=Label(a,text="THE RESULT",fg="red").place(x=600,y=500)
    t = Text(a,height=12,
     width=40)
    t.insert(INSERT, name)
    t.insert(INSERT, "\n")
    t.insert(INSERT, age)
    t.insert(INSERT,"\n")
    t.insert(INSERT, phone)
    t.insert(INSERT, "\n")
    t.insert(INSERT, city)
    t.insert(INSERT, "\n")
    t.insert(INSERT, selection)
    t.pack(side=BOTTOM)
def select():
    global selection
    if v.get()==1:
        s="UG"
    elif v.get()==2:
        s="PG"
    selection ="your Qualification is " + s
img= PhotoImage(file='Submit.png')
l3 = Label(a, text="ENTER YOUR NAME")
l3.place(x=430,y=140)
l4 = Label(a, text="ENTER YOUR AGE")
l4.place(x=430,y=180)
l5 = Label(a,text="ENTER YOUR PHONE NUMBER")
l5.place(x=430,y=200)
l6 = Label(a, text="ENTER YOUR CITY")
l6.place(x=430,y=220)
l7 = Label(a,text="CHOOSE YOUR QUALIFICATION")
l7.place(x=430,y=240)
e1 = Entry(a, bd =2)
e1.place(x=620,y=140)
e2 = Entry(a, bd =2)
e2.place(x=620,y=180)
e3 = Entry(a ,bd =2)
e3.place(x=620,y=200)
e4 = Entry(a, bd =2)
e4.place(x=620,y=220)
b= Button(a, image=img,command= texting,
borderwidth=0,width=100,height=50)
b.place(x=650,y=300)
v= IntVar()
x1 = RadioButton(a, text="UG", variable=v, value=1,command=select)
x2 = RadioButton(a, text="PG", variable=v, value=2,command=select)
x1.place(x=620,y=240)
x2.place( x=620,y=260)