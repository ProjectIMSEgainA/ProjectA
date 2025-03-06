import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry("600x500")
def deletestore():
    db=pymysql.connect(host = "Localhost",user = "root", password = "root", database = "ims")
    cur =  db.cursor()
    xa=int(cb.get())
    sql="delete from store where storeid = (%d)"%(xa)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("Hi","Delted from Store Table")
    e1.delete(0,100)
    
def showstoreid():
    db=pymysql.connect(host = "Localhost",user = "root", password = "root", database = "ims")
    cur =  db.cursor() 
    sql = "select storeid from store"
    cur.execute(sql)
    data = cur.fetchall()
    lst = []
    for i in data:
        lst.append(i[0])
    db.close()
    cb['values'] = lst

def btclose():
    t.destroy()

d=Canvas(t,width=600,height = 60,bg="pink")
d.place(x=0,y=0)
d.create_text(290,30,text = "Delete Data From Store Table",font = ("Times New Roman",15,"bold"))
a=Label(t,text = "Store ID",font = ("Times New Roman",14,"bold"))
a.place(x=100,y=150)
#e1=Entry(t,width = 25)
#e1.place(x=300,y=155)
cb = ttk.Combobox(t,width = 20)
cb.place(x=305,y=155)
showstoreid()
bt=Button(t,text = "Delete",fg="red",width = 20, command = deletestore)
bt.place(x=100,y=300)
bt2=Button(t,text = "Close",fg = "red",width=20,command = btclose)
bt2.place(x=350,y=300,)

t.mainloop()
