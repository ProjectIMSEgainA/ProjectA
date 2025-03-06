import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry("600x500")  
def findstore():
    db=pymysql.connect(host = "Localhost", user = "root", password = "root", database  = "ims")
    cur =db.cursor()
    xa = int(cb.get())
    sql = "select name, address, city, phoneNo , regNo from store where storeid=%d"%(xa)
    cur.execute(sql)
    db.commit()
    data = cur.fetchone()
    db.close()
    messagebox.showinfo("Hi there","Data Found For Store ID :"+str(xa))
    e2.insert(0,data[0])
    e3.insert(0,data[1])
    e4.insert(0,data[2])
    e5.insert(0,data[3])
    e6.insert(0,str(data[4]))
def showstoreid():
    db=pymysql.connect(host ="Localhost", user = "root", password ="root", database ="ims")
    cur=db.cursor()
    sql = "select storeid from store"
    cur.execute(sql)
    data = cur.fetchall()
    lst=[]
    for i in data:
        lst.append(i[0])
    db.close()
    cb["values"] = lst
    
def btclose():
    t.destroy()
s=Canvas(t, width = 600, height = 60,bg="Orange")
s.place(x=0,y=0)
s.create_text(290,30,text= "Find Data From Store Table",font = ("Times New Roman",14,"bold"))
a=Label(t,text = "Store ID", font = ("Times New Roman",14,"bold"))
a.place(x=100,y=100)
cb=ttk.Combobox(t,width=20)
cb.place(x=300,y=105)
showstoreid()
b=Label(t,text = "Name",font = ("Times New Roman",14,"bold"))
b.place(x=100,y=150)
e2=Entry(t,width=20)
e2.place(x=300,y=155)
c=Label(t,text = "Address",font = ("Times New Roman",14,"bold"))
c.place(x=100,y=205)
e3=Entry(t,width=20)
e3.place(x=300,y=210)
d=Label(t,text = "City",font = ("Times New Roman",14,"bold"))
d.place(x=100,y=255)
e4=Entry(t,width=20)
e4.place(x=300,y=260)
e=Label(t,text = "Phone No",font = ("Times New Roman",14,"bold"))
e.place(x=100,y=310)
e5=Entry(t,width=20)
e5.place(x=300,y=315)
f=Label(t,text = "Registration No",font = ("Times New Roman",14,"bold"))
f.place(x=100,y=370)
e6=Entry(t,width=20)
e6.place(x=300,y=375)
bt=Button(t,text = "Find",fg="blue",width = 20,command = findstore)
bt.place(x=100,y=450)
bt2=Button(t,text = "Close",fg = "red", width = 20,command = btclose)
bt2.place(x=300,y=450)
t.mainloop()
