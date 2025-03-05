import pymysql
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

t = tkinter.Tk()    
def findcategory():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "select catName, description from category where catId = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,data[1])
    e4.insert(0,data[2])
    db.close()
    
    messagebox.showinfo("Hi there","Data found for catId Id: "+str(xcb))
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
    
def btclose():
    t.destroy()    

canva = Canvas(t, width = 600,height = 60,bg = 'light blue')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from category Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Category Id')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 17)
cb.place(x = 400, y = 100)
CategoryId()
b = Label(t, text = 'Category Name')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Description')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)



bt = Button(t, text = 'Find', fg = 'Blue',width = 25, command = findcategory)
bt.place(x = 50, y = 400)
bt2 = Button(t, text = 'Close',fg = 'Red',width = 25, command = btclose)
bt2.place(x = 350, y = 400)
t.mainloop()