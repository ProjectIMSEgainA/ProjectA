# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:57:57 2025

@author: acer
"""

import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
def findsuppliers():
    db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
    cur = db.cursor()
    xcb = int(cb.get())

    sql = "select supname , address, catid from suppliers where supid = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    e4.insert(0,data[2])
    db.close()
    messagebox.showinfo("Hi there","Suppliers data find")
    '''e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)'''
    
def SuppliersId():
    db = pymysql.connect(host = 'Localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select supid from suppliers"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst
    
def CategoryId():
    db = pymysql.connect(host = 'Localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select catid from suppliers"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst

    

def btclose():
    t.destroy()
canva = Canvas(t, width = 600,height = 60,bg = 'Yellow')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from Supplier Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Supplier id')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 17)
cb.place(x = 400, y = 100)
SuppliersId()
b = Label(t, text = 'Supplier Name')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Address')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Category id')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
bt = Button(t, text = "Find", width = 25, fg = 'Black', command = findsuppliers)
bt2 = Button(t, text = 'Close', width = 25, fg = 'Orange', command = btclose)
bt2.place(x = 350, y = 400)

bt.place(x = 50, y = 400)



t.mainloop()
