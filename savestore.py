import tkinter
import pymysql 
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.geometry("600x500")
s=Canvas(t,width=600, height=60, bg = 'Green')
s.create_text(290,30,text = "Insert Data Into Store Table",font = ("Times New Roman" , 15, "bold"))
s.place(x=0,y=0)
def savestore():
    db=pymysql.connect(host = "Localhost", user = "root" , password = "root" , database = "ims")
    cur=db.cursor()
    xa=int(e1.get())
    xb=e2.get()
    xc=e3.get()
    xd=e6.get()
    xe=e4.get()
    xf=int(e5.get())
    sql = "insert into store values(%d,'%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi","Data Saved")
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e6.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
def btclose():
    t.destroy()
a=Label(t,text = "Store ID")
a.place(x=100,y=100)
e1=Entry(t,width = 20)
e1.place(x=300,y=100)
b=Label(t,text = "Name")
b.place(x=100,y=150)
e2=Entry(t,width = 20)
e2.place(x=300,y=150)
c=Label(t,text = "Address")
e3=Entry(t,width = 20)
e3.place(x=300,y=200)
c.place(x=100,y=200)
cx=Label(t,text="City")
cx.place(x=100,y=250)
e6=Entry(t,width = 20)
e6.place(x=300,y=250)
d=Label(t,text = "Phone No")
d.place(x=100,y=300)
e4=Entry(t,width =20)
e4.place(x=300,y=300)
r=Label(t,text="Registration No")
r.place(x=100,y=350)
e5=Entry(t,width=20)
e5.place(x=300,y=350)
bt=Button(t,text = "Save",width=20,fg="Green",command = savestore)
bt.place(x=50,y=450)
bt2=Button(t,text= "Close",width=20,fg="Red",command=btclose)
bt2.place(x=400,y=450)
t.mainloop()            