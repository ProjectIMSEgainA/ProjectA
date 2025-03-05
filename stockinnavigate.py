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
    db = pymysql.connect(host = 'Localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql="select * from stockin"
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
    i = i+1
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

    
a = Label(t, text = 'Supplier id')
a.place(x = 50, y = 100)
e1 = Entry(t, width = 20)
e1.place(x = 400, y = 100)
b = Label(t, text = 'Category id')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Product id')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Datein')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
f= Label(t, text = 'Quantity')
f.place(x= 50, y = 260)
e5 = Entry(t, width = 20)
e5.place(x=400, y=260)
s=Button(t, text = 'First',font='arial', fg = 'Black', command=first)
s.place(x=50,y=400)
bt=Button(t, text = 'Next',font='arial', fg = 'Orange', command=nexta)
bt.place(x = 150, y = 400)
ct=Button(t, text = 'Previuos',font='arial', fg = 'Red', command=previous)
ct.place(x = 250, y = 400)
dt=Button(t, text ='Last',font='arial',fg = 'Blue', command=last)
dt.place(x=350,y=400)
filldata()
t.mainloop()