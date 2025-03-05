import tkinter
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import*

t = tkinter.Tk()
t.geometry('600x550')

def saveorders():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    xe1 = int(e1.get())
    xe2 = int(e2.get())
    xe3 = int(e3.get())
    xe4 = int(e4.get())
    xe5 = e5.get()
    xe6 = e6.get()
    xe7 = int(e7.get())
    sql = "insert into orders values (%d, %d, %d, %d, '%s', '%s',%d)"%(xe1,xe2,xe3,xe4,xe5,xe6,xe7)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('Hi there','Data inserted in Orders Table')
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)

def btclose():
    t.destroy()    

canva = Canvas(t,width = 600, height = 60, bg = 'Orange')
canva.place(x=0, y = 0)
canva.create_text(290,30,text = "Insert data into Orders Table", font = ("Arial",15,"bold"))

a = Label(t, text = 'Order No')
a.place(x = 50, y = 100)
e1 = Entry(t, width = 20)
e1.place(x = 400, y = 100)
b = Label(t, text = 'Customer Id')
b.place(x = 50 ,y = 140)
e2 = Entry(t, width = 20)
e2.place(x = 400, y = 140)
c = Label(t, text = 'Category Id')
c.place(x = 50 , y = 180)
e3 = Entry(t, width = 20)
e3.place(x = 400, y = 180)
d = Label(t, text = 'Product Id')
d.place(x = 50, y = 220)
e4 = Entry(t, width = 20)
e4.place(x = 400, y = 220)
f = Label(t,text = 'Product Name')
f.place(x= 50, y = 260)
e5 = Entry(t, width =20)
e5.place(x = 400, y = 260)
g = Label(t,text = 'Date Of Order')
g.place(x= 50, y = 300)
e6 = Entry(t, width =20)
e6.place(x = 400, y = 300)
h = Label(t,text = 'Quantity')
h.place(x= 50, y = 340)
e7 = Entry(t, width =20)
e7.place(x = 400, y = 340)


bt = Button(t, text = 'Save', width = 25, fg = 'Green', command = saveorders)
bt.place(x = 50, y = 450)
bt2 = Button(t, text = 'Close', width = 25, fg = 'Red', command = btclose)
bt2.place(x = 350, y = 450)
t.mainloop()