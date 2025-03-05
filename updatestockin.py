import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
def finddata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "select catid, prodid, datein, qty from stockin where supid = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    e4.insert(0,str(data[2]))
    e5.insert(0,(data[3]))
    db.close()
    messagebox.showinfo("Hi there","Data found for supid:")
    

def btclose():
           t.destroy()
    
def updatedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database = 'IMS')
    cur = db.cursor()
    xa=int(cb.get())
    xb=int(e2.get())
    xc=int(e3.get())
    xd=e4.get()
    xe=int(e5.get())
    sql="update stockin set catid=%d, prodid=%d, datein='%s',qty=%d where supId=%d"%(xb,xc,xd, xe,xa)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('Hi','Updated')
    #e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
def SupplierId():
    db = pymysql.connect(host = 'Localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select supid from stockin"
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

    
canva = Canvas(t, width = 600,height = 60,bg = 'Red')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from Stockin Table" ,font=("Arial", 15, "bold"))



a = Label(t, text = 'Supplier id')
a.place(x = 50, y = 100)
b = Label(t, text = 'Category id')
b.place(x = 50 ,y = 140)
c = Label(t, text = 'Product id')
c.place(x = 50 , y = 180)
d = Label(t, text = 'Data in')
d.place(x = 50, y = 220)
f= Label(t, text = 'Quantity')
f.place(x= 50, y = 260)


cb=ttk.Combobox(t,width = 17)
cb.place(x=400, y=100)
SupplierId()
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
e5 = Entry(t, width = 20)
e5.place(x=400, y=260)

s=Button(t, text = 'Find',font='arial', fg = 'red', command=finddata)
s.place(x=50,y=400)
bt=Button(t, text = 'Close',font='arial', fg = 'black', command=btclose)
bt.place(x = 150, y = 400)
ct=Button(t, text = 'Update',font='arial', fg = 'grey', command=updatedata)
ct.place(x = 250, y = 400)
dt=Button(t, text ='New',font='arial',fg = 'Blue', command=nw)
dt.place(x=350,y=400)
t.mainloop()
