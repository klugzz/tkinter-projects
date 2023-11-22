from tkinter import *
from tkinter import messagebox as b
a=Tk()
a.title('Digit')
a.geometry('500x400')
def process():
    en = int(Entry.get(en_1))
    if en >=0 and en <=9 :
        la = Label(a,text='SingleDigit',font=('Times New Roman',16),fg="red")
        la.place(x=50,y=150)
    elif en >=10 and en <=99:
        la = Label(a,text='DoubleDigit',font=('Times New Roman',16),fg="red")
        la.place(x=50,y=150)
    else:
        la = Label(a,text='Wrong Value',font=('Times New Roman',16),fg="red")
        la.place(x=50,y=150)
la_lbl = Label(a,text='DIGITS',font=('Times New Roman',16))
la_lbl.pack()
la_lbl = Label(a,text='Value',font=('Times New Roman',16)).place(x=20,y=50)
en_1 = Entry(a,font=('Times New Roman',16),width=15)
en_1.place(x=100,y=52)
btn = Button(a,text='Submit',font=('Times New Roman',16),command=process)
btn.place(x=50,y=100)
a.mainloop()