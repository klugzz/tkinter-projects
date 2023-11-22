try:
    from tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
global answer
def add():
    try:
        global answer
        number1=int(Entry.get(E1))
        number2=int(Entry.get(E2))
        answer=number1+number2
        
    except ValueError:
        messagebox.showinfo('warning',"please enter the integer")
def sub():
    try:
        global answer
        number1=int(Entry.get(E1))
        number2=int(Entry.get(E2))
        answer=number1-number-2
    except ValueError:
        messagebox.showinfo('warning',"please enter the integer")
def mul():
    try:
        global answer
        number1=int(Entry.get(E1))
        number2=int(Entry.get(E2))
        answer=number1*number2
    except VAlueError:
        messagebox.showinfo('Warning',"please enter the integer")
def div():
    try:
        global answer
        number1=int(Entry.get(E1))
        number2=int(Entry.get(E2))
        answer=number1/number2
    except ValueError:
        messagebox.showinfo('warning',"please enter the integer")
def process():
    global answer
    messagebox.showinfo('result',answer)
    
    top=Tk()
    top.title("CALCULATOR")
    L1=Label(top, text="CALC",).grid(row=0,column=1)
    L2=Label(top, text="number1",).grid(row=1,column=0)
    L3=Label(top, text="number2",).grid(row=2,column=0)
    E1=Entry(top,bd=5)
    E1.grid(row=1,column=4)
    E2=Entry(top,bd=5)
    E2.grid(row=2,column=4)
    B=Button(top,text="Submit",command=process).grid(row=3,column=2,)
    add=Button(top,text="add",command=add).grid(row=5,column=1,)
    sub=Button(top,text="sub",command=sub).grid(row=5,column=2,)
    mul=Button(top,text="mul",command=mul).grid(row=5,column=3,)
    div=Button(top,text="div",command=div).grid(row=6,column=2,)
    