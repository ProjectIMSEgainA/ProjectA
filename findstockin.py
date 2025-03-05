import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
def findstockin():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "select catid, prodid, datein, qty from stockin where supid = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    e4.insert(0,data[2])
    e5.insert(0,data[3])
    db.close()
    messagebox.showinfo("Hi there"," stockin data find")
    
    
def SuppliersId():
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
    


def btclose():
    t.destroy()
canva = Canvas(t, width = 600,height = 60,bg = 'grey')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from Stockin Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Supplier id')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 17)
cb.place(x = 400, y = 100)
SuppliersId()
b = Label(t, text = 'Category id')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Product id')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Data in')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
f= Label(t, text = 'Quantity')
f.place(x= 50, y = 260)
e5 = Entry(t, width = 20)
e5.place(x=400, y=260)
bt = Button(t, text = 'Find', width = 25, fg = 'Black', command = findstockin)
bt2 = Button(t, text = 'close', width = 25, fg = 'Brown', command = btclose)
bt2.place(x = 350, y = 400)

bt.place(x = 50, y = 400)



t.mainloop()