try:
    from tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def process():
    try:
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number1)
        number2=int(number2)
        if operator=='add':
            answer=number1+number2
        if operator=='sub':
            answer=number1-number2
        if operator=='mul':
            answer=number1*number2
        if operator=='div':
            answer==number1/number2
        Entry.insert(E4,0,answer)
    except ValueError:
        messagebox.showinfo('warning',"please enter the integr")
top=Tk()
top.title("CALCULATOR")
L1=Label(top,text="CALC",).grid(row=0,column=1)
L2=Label(top,text="number1",).grid(row=1,column=0)
L3=Label(top,text="number2",).grid(row=2,column=0)
L4=Label(top,text="operator",).grid(row=3,column=0)
L5=Label(top,text="answer",).grid(row=4,column=0)
E1=Entry(top,bd=5)
E1.grid(row=1,column=4)
E2=Entry(top,bd=5)
E2.grid(row=2,column=4)
E3=Entry(top,bd=5)
E3.grid(row=3,column=4)
E4=Entry(top,bd=5)
E4.grid(row=4,column=4)
B=Button(top,text="Submit",command=process).grid(row=5,column=1,)
mainloop()