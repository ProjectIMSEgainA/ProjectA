import tkinter 
import pymysql
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry("600x600")

xa=[]
xb=[]
xc=[]
xd=[]
xe=[]
xf=[]
i = 0
def filldata():
    db=pymysql.connect(host="Localhost",user = "root", password = "root",database = "Ims")
    cur=db.cursor()
    sql="select * from store"
    cur.execute(sql)
    data = cur.fetchall()
    for res in data:
        xa.append(res[0])
        xb.append(res[1])
        xc.append(res[2])
        xd.append(res[3])
        xe.append(res[4])
        xf.append(res[5])
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
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
def nexta():
    global i
    i = i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
def Previous():
    global i
    i = i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
def last():
    global i
    i = len(xa)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,xa[i])
    e2.insert(0,xb[i])
    e3.insert(0,xc[i])
    e4.insert(0,xd[i])
    e5.insert(0,xe[i])
    e6.insert(0,xf[i])
    
s=Canvas(t,width=600,  height = 60, bg = "green")
s.place(x=0,y=0)
s.create_text(290,30, text = "Find Next Previous  From Store Table" , font= ("Times New Roman", 14, "bold"))

a=Label(t,text = "Store ID",font = ("Times New Roman",14,"bold"))
a.place(x=100,y=100)
e1=Entry(t,width=20)
e1.place(x=295,y=105)
b=Label(t,text = "Name",font = ("Times New Roman",14,"bold"))
b.place(x=100,y=150)
e2=Entry(t,width=20)
e2.place(x=300,y=155)
c=Label(t,text = "Address",font = ("Times New Roman",14,"bold"))
c.place(x=100,y=205)
e3=Entry(t,width=20)
e3.place(x=300,y=210)
d=Label(t,text = "City",font = ("Times New Roman",14,"bold"))
d.place(x=100,y=255)
e4=Entry(t,width=20)
e4.place(x=300,y=260)
e=Label(t,text = "Phone No",font = ("Times New Roman",14,"bold"))
e.place(x=100,y=310)
e5=Entry(t,width=20)
e5.place(x=300,y=315)
f=Label(t,text = "Registration No",font = ("Times New Roman",14,"bold"))
f.place(x=100,y=370)
e6=Entry(t,width=20)
e6.place(x=300,y=375)
bt=Button(t,text = "First",fg="blue",command = first )
bt.place(x=100,y=500)
bt2=Button(t,text = "Next",fg = "red",command = nexta)
bt2.place(x=200,y=500)
bt3=Button(t,text = "Previous",fg = "Green",command = previous)
bt3.place(x=300,y=500)
bt4=Button(t,text = "Last",fg = "black",command = last)
bt4.place(x=400,y=500)
filldata()
t.mainloop()
