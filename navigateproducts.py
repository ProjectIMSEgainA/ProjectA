# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:40:31 2025

@author: yasha
"""

import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
xa=[]
xb=[]
xc=[]
xd=[]
xe=[]
i=0
def filldata():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur=db.cursor()
    sql="select * from products"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        xa.append(res[0])
        xb.append(res[1])
        xc.append(res[2])
        xd.append(res[3])
        xe.append(res[4])
    db.close()
def first():
    global i
    i=0
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
def nexta():
    global i
    i=i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
def previous():
    global i
    i=i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
def last():
    global i
    i=len(xa)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
canva = Canvas(t, width = 600,height = 60,bg = 'light green')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Navigate Data from Products Table" ,font=("Arial", 15, "bold"))
a = Label(t, text = 'Product Id')
a.place(x = 50, y = 100)
e1 = Entry(t, width = 20)
e1.place(x = 400, y = 100)
b = Label(t, text = 'Category Id')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Product Name')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Price')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
f = Label(t,text = 'Quantity')
f.place(x= 50, y = 260)
e5 = Entry(t, width =20)
e5.place(x = 400, y = 260)
s=Button(t,text='First',font='arial',fg = 'Red',command=first)
s.place(x=50,y=300)
bt=Button(t,text='Next',font='arial',fg = 'purple',command=nexta)
bt.place(x=150,y=300)
ct=Button(t,text='Last',font='arial',fg = 'green',command=last)
ct.place(x=250,y=300)
dt=Button(t,text='Previous',font='arial',fg = 'pink',command=previous)

dt.place(x=350,y=300)
filldata()
t.mainloop()