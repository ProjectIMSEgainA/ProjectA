# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:27:17 2025

@author: yasha
"""
import tkinter
import pymysql 
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.geometry("600x600")
def savecategory():
    db=pymysql.connect(host = "Localhost", user = "root" , password = "root" , database = "Ims")
    cur=db.cursor()
    xa=int(b.get())
    xb=c.get()
    xc=e.get()
    
    
    sql = "insert into category values(%d,'%s','%s')"%(xa,xb,xc)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi","Data Saved")
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
canva = Canvas(t, width = 600,height = 60,bg = 'light blue')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from category Table" ,font=("Arial", 15, "bold"))
    

a=Label(t,text='catId')
a.place(x=50,y=110)
b=Entry(t,width=20)
b.place(x=400,y=110)
d=Label(t,text='catName')
d.place(x=50,y=150)
c=Entry(t,width=20)
c.place(x=400,y=150)

f=Label(t,text='description')
f.place(x=50,y=190)
e=Entry(t,width=20)
e.place(x=400,y=190)
bt=Button(t,text = "Save",fg = 'Red',command = savecategory)
bt.place(x=250,y=240)






t.mainloop()