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
i = 0

def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
    cur = db.cursor()
    sql = "select * from customers"
    cur.execute(sql)
    data = cur.fetchall()
    for res in data:
        xa.append(res[0])
        xb.append(res[1])
        xc.append(res[2])
        xd.append(res[3])
        xe.append(res[4])
        db.close()  
def first():
    global i
    i = 0
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
def nexta():
    global i
    i = i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
def previous():
    global i
    i = i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])    
def last():
    global i 
    i =len(xa)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    
canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "Find Next Previous Table for customers" ,font=("Times New Roman", 15, "bold"))
        
a=Label(t,text = "Customer ID", font = ("Times New Roman",12,"bold"))
a.place(x=100,y=100)
e1=Entry(t,width = 20)
e1.place(x=300,y=105)
b=Label(t,text = "Customer Name", font = ("Times New Roman",12,"bold"))
b.place(x=100,y=150)
e2 = Entry(t,width = 20)
e2.place(x=300,y=155)
c=Label(t,text = "Address", font = ("Times New Roman",15,"bold"))
c.place(x=100,y=200)
e3 = Entry(t,width = 20)
e3.place(x=300,y=205)
d=Label(t,text = "Phone No", font = ("Times New Roman",12,"bold"))
d.place(x=100,y=250)
e4 = Entry(t,width = 20)
e4.place(x=300,y=255)
e=Label(t,text = "City", font = ("Times New Roman",12,"bold"))
e.place(x=100,y=300)
e5 = Entry(t,width = 20)
e5.place(x=300,y=305)


bt = Button(t, text = 'First',width = 10, fg = 'Green', command = first)
bt.place(x = 50, y = 400)
bt = Button(t, text = 'Next', width = 10, fg = 'Green',command = nexta )
bt.place(x = 150, y = 400)
bt = Button(t, text = 'Last', width = 10, fg = 'Green', command = last)
bt.place(x = 350, y = 400)
bt2 = Button(t, text = 'Previuos', width = 10, fg = 'Green',command = previous)
bt2.place(x = 250, y = 400)

filldata()

t.mainloop()  