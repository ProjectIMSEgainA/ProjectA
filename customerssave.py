import tkinter 
import pymysql
from tkinter import *
from tkinter import messagebox 
t=tkinter.Tk()
t.geometry("600x500")
def savecustomers():
    db=pymysql.connect(host = "Localhost",user = "root", password = "root",database = "ims")
    cur=db.cursor()
    xa=int(e1.get())
    xb=e2.get()
    xc=e3.get()
    xd=e4.get()
    xe=e5.get()
    sql="insert into customers values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi","Saved")
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
def btclose():
    t.destroy()
s=Canvas(t,width = 600, height = 60,bg="orange")
s.place(x=0,y=0)
s.create_text(290,30,text = "Insert Data Into Customers Table", font = ("Times New Roman",14,"bold"))
a=Label(t,text = "Customer ID", font = ("Times New Roman",12,"bold"))
a.place(x=100,y=100)
e1 = Entry(t,width = 20)
e1.place(x=300,y=105)
b=Label(t,text = "Customer Name", font = ("Times New Roman",12,"bold"))
b.place(x=100,y=150)
e2 = Entry(t,width = 20)
e2.place(x=300,y=155)
c=Label(t,text = "Address", font = ("Times New Roman",15,"bold"))
c.place(x=100,y=200)
e3 = Entry(t,width = 20)
e3.place(x=300,y=205)
d=Label(t,text = "Phone No", font = ("Times New Roman",12,"bold"))
d.place(x=100,y=250)
e4 = Entry(t,width = 20)
e4.place(x=300,y=255)
e=Label(t,text = "City", font = ("Times New Roman",12,"bold"))
e.place(x=100,y=300)
e5 = Entry(t,width = 20)
e5.place(x=300,y=305)
Bt=Button(t,text = "Save",fg="green",width = 20,command = savecustomers)
Bt.place(x=100,y=400)
Bt2=Button(t,text = "Close",fg="red",width = 20,command = btclose)
Bt2.place(x=300,y=400)

t.mainloop()