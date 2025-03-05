import pymysql
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

t = tkinter.Tk()
t.geometry('600x500')

def findbilling():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "select orderNo, custId,dispatchdate,amount from billing where billNo = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,data[0])
    e3.insert(0,data[1])
    e4.insert(0,str(data[2]))
    e5.insert(0,data[3])
    db.close()
    messagebox.showinfo('Hi there','Data found for Bill No: '+str(xcb))
    
def updatebilling():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    xe2 = int(e2.get())
    xe3 = int(e3.get())
    xe4 = e4.get()
    xe5 = int(e5.get())
    sql = "update billing set orderNo = %d, custId = %d, dispatchdate = '%s', amount = %d where billno = %d"%(xe2,xe3,xe4,xe5,xcb)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('Hi there','Data updated for Bill No: '+str(xcb))
    cb.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    
def findbillno():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select billNo from billing"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst
    
def btclose():
    t.destroy()    
    

canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find and Update all data from Billing Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Bill No')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 20)
cb.place(x = 400, y = 100)
findbillno()
b = Label(t, text = 'Order No')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 23)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Customer Id')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 23)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Dispatch Date')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 23)
e4.place(x = 400, y = 220)
f = Label(t, text = 'Amount')
f.place(x = 50, y = 260)
e5 = Entry(t, width = 23)
e5.place(x = 400, y = 260)

bt = Button(t, text = 'Find', bg = 'Green', width = 15, command = findbilling)
bt.place(x = 50, y = 400)
bt2 = Button(t, text = 'Update' ,bg = 'Yellow', width =15, command = updatebilling)
bt2.place(x = 250, y = 400)
bt3 = Button(t, text = 'Close', bg = 'Red', width = 15, command = btclose)
bt3.place(x = 450, y = 400)
t.mainloop()