from tkinter import *
from tkinter import messagebox as b
a=Tk()
a.title('WORKING TIME')
a.geometry('400x300')
def process():
    name = en_1.get()
    age = int(en_2.get())
    degre = (Entry.get(en_3))
    Label(a,text=f'Hello {name}',font=('Times New Roman',16)).place(x=100,y=220)
    if degre == 'ug' and age >=20 and age <=30:
        Label(a,text=f'Working Time 9 a.m to 8 p.m',font=('Times New Roman',16)).place(x=100,y=250)
    elif degre >='pg' and age >=20 and age <=30 :
        Label(a,text='Working Time 8  p.m to 9 a.m',font=('Times New Roman',16)).place(x=100,y=250)
    else:
        Label(a,text='Not Eligible',font=('Times New Roman',16)).place(x=100,y=250)
Label(a,text='GRADE',font=('Times New Roman',16)).pack()
Label(a,text='Name',font=('Times New Roman',16)).place(x=50,y=50)
Label(a,text='Age',font=('Times New Roman',16)).place(x=50,y=90)
Label(a,text='UG or PG',font=('Times New Roman',16)).place(x=50,y=130)
en_1 = Entry(a,font=('Times New Roman',16),width=15)
en_1.place(x=150,y=52)
en_2 = Entry(a,font=('Times New Roman',16),width=15)
en_2.place(x=150,y=92)
en_3 = Entry(a,font=('Times New Roman',16),width=15)
en_3.place(x=150,y=132)
btn = Button(a,text='Submit',font=('Times New Roman',16),command=process)
btn.place(x=100,y=170)
a.mainloop()
