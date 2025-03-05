
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:48:50 2025

@author: yasha
"""

import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

t=tkinter.Tk()
t.geometry('600x500')
def finddata():
        
        db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
        cur = db.cursor()
        xcb = int(cb.get())
        sql = "select catId,prodName,price,qty from products where prodId = %d"%(xcb)
        cur.execute(sql)
        data = cur.fetchone()
        e2.insert(0,str(data[0]))
        e3.insert(0,data[1])
        e4.insert(0,str(data[2]))
        e5.insert(0,str(data[3]))
        
       
        db.close()
        messagebox.showinfo("Hi there","Data found for catId: ")
        
      
        
def close():
        t.destroy()
        
def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
        cur=db.cursor()
        xa=int(cb.get())
        
        xb=int(e2.get())
        xc=e3.get()
        xd=int(e4.get())
        xe=int(e5.get())
        sql="update products set catId=%d,prodName='%s',price=%d,qty=%d where prodId=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
def ProductsId():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select prodId from products"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst
       
         
        
def nw():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
canva = Canvas(t, width = 600,height = 60,bg = 'light green')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from Products Table" ,font=("Arial", 15, "bold"))      
   
a=Label(t,text='Product Id')
a.place(x=50,y=110)
b=Label(t,text='Category Id')
b.place(x=50,y=150)
c=Label(t,text='Product Name')
c.place(x=50,y=190)
d=Label(t,text='Price')
d.place(x=50,y=230)
e=Label(t,text='Quantity')
e.place(x=50,y=270)

   
e1=Entry(t,width=30)
e1.place(x=250,y=110)
cb =ttk.Combobox(t, width = 30)
cb.place(x =250, y = 110)
ProductsId()
e2=Entry(t,width=30)
e2.place(x=250,y=150)
e3=Entry(t,width=30)
e3.place(x=250,y=190)
e4=Entry(t,width=30)
e4.place(x=250,y=230)
e5=Entry(t,width=30)
e5.place(x=250,y=270)
s=Button(t,text='Find',font='arial',fg = 'Red',command=finddata)
s.place(x=50,y=300)
bt=Button(t,text='Close',font='arial',fg = 'purple',command=close)
bt.place(x=150,y=300)
ct=Button(t,text='Update',font='arial',fg = 'green',command=updatedata)
ct.place(x=250,y=300)
dt=Button(t,text='New',font='arial',fg = 'pink',command=nw)
dt.place(x=350,y=300)
t.mainloop()