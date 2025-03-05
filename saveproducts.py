import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')
rt=[]

def fillcategory():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    sql="select catid from category" 
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        rt.append(res[0])
    e2['values']=rt
    db.close()
def savebilling():
    if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
        messagebox.showerror('Hi','Pls fill all data')
    else:
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur = db.cursor()
        xe1 = int(e1.get())
        xe2 = int(e2.get())
        xe3 = e3.get()
        xe4 = int(e4.get())
        xe5 = int(e5.get())
        sql = "insert into products values (%d,%d, '%s', %d, %d)"%(xe1, xe2, xe3, xe4, xe5)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi there","Product data is saved")
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        

def btclose():
    t.destroy()

canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Insert Data into Product Table" ,font=("Arial", 15, "bold"))

a = Label(t, text = 'Product ID')
a.place(x = 50, y = 100)
e1 = Entry(t, width = 20)
e1.place(x = 400, y = 100)
b = Label(t, text = 'Category ID')
b.place(x = 50 ,y = 140)

e2 = ttk.Combobox(t, width = 20)
e2.place(x = 400, y = 140)
fillcategory()
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


bt = Button(t, text = 'Save', width = 25, fg = 'Green', command = savebilling)
bt.place(x = 50, y = 400)
bt2 = Button(t, text = 'Close', width = 25, fg = 'Red', command = btclose)
bt2.place(x = 350, y = 400)
t.mainloop()
