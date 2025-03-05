import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

t = tkinter.Tk()
t.geometry('600x500')

def deletebilling():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "delete from billing where billNo = %d"%(xcb)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi there","Data deleted from table for billNo: "+str(xcb))
    
def billno():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select billNo from billing"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] =lst
    
def btclose():
    t.destroy()

canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Delete Data from Billing Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Bill No')
a.place(x =50, y= 120)
cb = ttk.Combobox(t, width = 30)
cb.place(x = 320, y = 120)
billno()

bt = Button(t, text = "Delete", width = 25, fg = 'Red', command = deletebilling)
bt.place(x = 50, y = 400)
bt2 = Button(t, text = 'Close', width = 25, fg = 'Red', command = btclose)
bt2.place(x = 350, y = 400 )
t.mainloop()
t.mainloop()