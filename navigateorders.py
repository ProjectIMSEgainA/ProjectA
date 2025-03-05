import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


t = tkinter.Tk()
t.geometry('600x500')

xa = []
xb = []
xc = []
xd = []
xe = []
xf = []
xg = []

i = 0

def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
    cur = db.cursor()
    sql = "select * from orders"
    cur.execute(sql)
    data = cur.fetchall()
    for res in data:
        xa.append(res[0])
        xb.append(res[1])
        xc.append(res[2])
        xd.append(res[3])
        xe.append(res[4])
        xf.append(res[5])
        xg.append(res[6])
    db.close()  
def first():
    global i
    i = 0
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
    e7.insert(0,xg[i])

def nexta():
    global i
    i = i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
    e7.insert(0,xg[i])
    
def previous():
    global i
    i = i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
    e7.insert(0,xg[i])
    
def last():
    global i
    i = len(xa)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e7.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
    e7.insert(0,xg[i])
    

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


bt = Button(t, text = 'First',width = 10, fg = 'Green', command = first)
bt.place(x = 50, y = 400)
bt = Button(t, text = 'Next', width = 10, fg = 'Green', command = nexta)
bt.place(x = 150, y = 400)
bt = Button(t, text = 'Previous', width = 10, fg = 'Green', command = previous )
bt.place(x = 250, y = 400)
bt2 = Button(t, text = 'Last', width = 10, fg = 'Green', command = last)
bt2.place(x = 350, y = 400)

filldata()

t.mainloop()