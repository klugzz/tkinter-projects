from tkinter import *
from tkinter import messagebox
import calendar
a=Tk()
a.title("Calendar")
def calm():
    try:
        year =int(Entry.get(t1))
        month = int(Entry.et(t2))
        messagebox.showinfo("Calendar",calendar.month(year,month))
    except:
        messagebox.showinfo("Error","Enter value...")
l3=Label(a,text="MONTHLY CALENDAR",).grid(row=0,column=1)
l1=Label(a,text="ENTER ANY YEAR:...",).grid(row=1,column=0)
l2=Label(a,text="ENTER ANY MONTH:...",).grid(row=2,column=0)
t1=Entry(a,bd=2)
t1.grid(row=1,column=2)
t2=Entry(a,bd=2)
t2.grid(row=2,column=2)
b=Button(a,text="CLICK",command=calendar).grid(row=3,column=2)
        