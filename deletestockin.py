import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
def deletestockin():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "delete from stockin where supid = %d"%(xcb)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi there","Data deleted from stockin table for supplier id:"+str(xcb))
    
def suppliersid():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select supid from stockin"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] =lst
 
    

def btclose():
    t.destroy()
canva = Canvas(t, width = 600,height = 60,bg = 'purple')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Delete Data from Stockin Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Supplier id')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 17)
cb.place(x = 320, y = 120)
suppliersid()
bt = Button(t, text = "Delete", width = 25, fg = 'Red', command = deletestockin)
bt2 = Button(t, text = 'Close', width = 25, fg = 'Orange', command = btclose)
bt2.place(x = 350, y = 400)

bt.place(x = 50, y = 400)



t.mainloop()