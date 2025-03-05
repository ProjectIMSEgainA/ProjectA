# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:25:48 2025

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
    db=pymysql.connect(host = "Localhost", user = "root" , password = "root" , database = "IMS")
    cur=db.cursor()
    xcb = int(cb.get())
    sql = "select catName, description from category where catId = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    
    e5.insert(0,data[3])
    db.close()
    messagebox.showinfo("Hi there","Data found for catId: "+str(xcb))
    db.close()

    
def btclose():
    t.destroy()    
        
def updatedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
    cur=db.cursor()
    xa=int(cb.get())
    xb=e2.get()
    xc=e3.get()
    
    sql="update category set catName='%s',description='%s' where catId=%d"%(xb,xc,xa)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('Hi','Updated')
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
        
def CategoryId():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select catId from category"
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
canva = Canvas(t, width = 600,height = 60,bg = 'light blue')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from category Table" ,font=("Arial", 15, "bold"))      
   
a=Label(t,text='Category Id')
a.place(x=50,y=110)

b=Label(t,text='Category Name')
b.place(x=50,y=150)
c=Label(t,text='Description')
c.place(x=50,y=190)

   
#e1=Entry(t,width=30)
#e1.place(x=250,y=110)
cb =ttk.Combobox(t, width = 30)
cb.place(x =250, y = 110)
CategoryId()
e2=Entry(t,width=30)
e2.place(x=250,y=150)
e3=Entry(t,width=30)
e3.place(x=250,y=190)

s=Button(t,text='Find',font='arial',fg = 'Red',command=finddata)
s.place(x=50,y=250)
bt=Button(t,text='Close',font='arial',fg = 'pink',command=btclose)
bt.place(x=150,y=250)
ct=Button(t,text='Update',font='arial',fg = 'green',command=updatedata)
ct.place(x=250,y=250)
dt=Button(t,text='New',font='arial',fg = 'yellow',command=nw)
dt.place(x=350,y=250)
t.mainloop()