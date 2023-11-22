from tkinter import *
import tkinter.font as f
from tkinter import messagebox as m
a=Tk()
a.title('Reverse')
a.geometry('800x400')
def process():
    en = int(Entry.get(en_a))
    reverse = 0
    while (en > 0):
        remainder = en %10
        reverse = (reverse*10)+remainder
        en = en//10
    m.showinfo('result',reverse)
p=f.Font(family = 'Arial Black',size=20,weight='bold')
l=f.Font(family = 'Times New Roman',size=25,weight='bold')
e=f.Font(family = 'Times New Roman',size=20,weight='bold')
la=Label(a,text = 'REVERSE',bg='white',fg='purple2')
la.pack()
la['font'] = p
la_a = Label(a,text = 'Number',fg='hot pink')
la_a.place(x=100,y=100)
la_a['font'] = l

en_a = Entry(a,borderwidth=2)
en_a.place(x=250,y=105)
en_a['font'] = e
btn = Button(a,text='Submit',font=('Times New Roman',16),command=process)
btn.place(x=200,y=180)
a.mainloop()
