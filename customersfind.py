import tkinter 
import pymysql
from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
t=tkinter.Tk()
t.geometry("600x500")
def customersfind():
    db=pymysql.connect(host = "Localhost",user = "root",password = "root", database = "Ims")
    cur=db.cursor()
    xcb=int(cb.get())
    sql="select custname,address,phoneNo,city from customers where custid = %d"%(xcb)
    cur.execute(sql)
    db.commit()
    data = cur.fetchone()
    db.close()
    messagebox.showinfo("Hi","Data Found From Customers Table:"+str(xcb))
    e2.insert(0,data[0])
    e3.insert(0,data[1])
    e4.insert(0,data[2])
    e5.insert(0,data[3])
def showcustid():
    db=pymysql.connect(host = "Localhost",user = "root",password = "root", database = "Ims")
    cur=db.cursor()
    sql = "select custid from customers"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
        db.close()
        cb["values"] = lst
        
def btclose():
    t.destroy()
s=Canvas(t,width = 600, height = 60,bg="orange")
s.place(x=0,y=0)
s.create_text(290,30,text = "Find Data from Customers Table", font = ("Times New Roman",14,"bold"))
a=Label(t,text = "Customer ID", font = ("Times New Roman",12,"bold"))
a.place(x=100,y=100)
cb=ttk.Combobox(t,width = 20)
cb.place(x=300,y=105)
showcustid()
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
Bt=Button(t,text = "Find",fg="green",width = 20,command = customersfind)
Bt.place(x=100,y=400)
Bt2=Button(t,text = "Close",fg="red",width = 20,command = btclose)
Bt2.place(x=300,y=400)
t.mainloop()