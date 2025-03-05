import pymysql
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

t = tkinter.Tk()
t.geometry('600x500')

def findproducts():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    xcb = int(cb.get())
    sql = "select catId, prodName, price, qty from Products where prodId = %d"%(xcb)
    cur.execute(sql)
    data = cur.fetchone()
    e2.insert(0,str(data[0]))
    e3.insert(0,str(data[1]))
    e4.insert(0,data[2])
    e5.insert(0,str(data[3]))
    db.close()
    messagebox.showinfo("Hi there","Data found for Product Id: "+str(xcb))
    
def productId():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select prodId from products"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst
    
def btclose():
    t.destroy()    

canva = Canvas(t, width = 600,height = 60,bg = 'light green')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Data from Products Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Product Id')
a.place(x = 50, y = 100)
cb = ttk.Combobox(t, width = 17)
cb.place(x = 400, y = 100)
productId()
b = Label(t, text = 'Category Id')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Product Name')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Price')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
f = Label(t,text = 'Quantity')
f.place(x= 50, y = 260)
e5 = Entry(t, width =20)
e5.place(x = 400, y = 260)


bt = Button(t, text = 'Find', fg = 'Blue',width = 25, command = findproducts)
bt.place(x = 50, y = 400)
bt2 = Button(t, text = 'Close',fg = 'Red',width = 25, command = btclose)
bt2.place(x = 350, y = 400)
t.mainloop()