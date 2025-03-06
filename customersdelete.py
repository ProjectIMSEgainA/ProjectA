import tkinter
import pymysql
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry("600x500")
def customersdelete():
    db=pymysql.connect(host = "Localhost",user = "root",password = "root", database = "Ims")
    cur = db.cursor()
    xcb=int(cb.get())
    sql="delete from customers where custid = %d"%(xcb)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi","Delete From Customer Table:"+str(xcb))
    cb.delete(0,100)
def showcustid():
    db=pymysql.connect(host = "Localhost",user = "root",password = "root", database = "Ims")
    cur = db.cursor()
    sql="select custid from customers"
    cur.execute(sql)
    data = cur.fetchall()
    lst=[]
    for i in data:
        lst.append(i[0])
        db.close()
        cb["values"] =lst
def btclose():
    t.destroy()
s=Canvas(t,width = 600,height=60,bg = "red")
s.place(x=0,y=0)
s.create_text(290,30,text = "Delete Data From Customers Table",font = ("Times New Roman",15,"bold"))
a=Label(t,text = "Customer ID", font = ("Times New Roman",15,"bold"))
a.place(x=100,y=150)
cb=ttk.Combobox(t,width = 20)
cb.place(x=300,y=155)
showcustid()
Bt=Button(t,text = "Delete", fg = "red",width = 20,command = customersdelete)
Bt.place(x=100,y=300)
Bt2=Button(t,text = "Close", fg = "red",width = 20, command = btclose)
Bt2.place(x=350,y=300)
t.mainloop()