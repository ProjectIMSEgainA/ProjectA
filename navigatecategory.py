# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:30:28 2025

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

i=0
def filldata():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur=db.cursor()
    sql="select * from category"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        xa.append(res[0])
        xb.append(res[1])
        xc.append(res[2])
       
    db.close()
def first():
    global i
    i=0
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
   
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
 
def nexta():
    global i
    i=i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
   
def previous():
    global i
    i=i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
   
def last():
    global i
    i=len(xa)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    
canva = Canvas(t, width = 600,height = 60,bg = 'light blue')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Navigate Data from Category Table" ,font=("Arial", 15, "bold"))
a = Label(t, text = 'Category Id')
a.place(x = 50, y = 100)
e1 = Entry(t, width = 20)
e1.place(x = 400, y = 100)
b = Label(t, text = 'Category Name')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Description')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)

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