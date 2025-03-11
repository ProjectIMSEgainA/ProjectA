import tkinter
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import*

def findorderdash():

    t = tkinter.Tk()
    t.geometry('600x550')
    
    def findorders():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur = db.cursor()
        xcb = int(cb.get())
        sql = "select custId, catId, prodId, prodName, dateoforder,qty from orders where orderNo = %d"%(xcb)
        cur.execute(sql)
        data = cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        db.close()
        messagebox.showinfo("Hi there","Data found for Order No: "+str(xcb))
        
    def showorderno():
        db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
        cur = db.cursor()
        sql = "select orderNo from orders"
        cur.execute(sql)
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i[0])
        db.close()
        cb['values'] = lst
    
    def btclose():
        t.destroy()
    
    canva = Canvas(t, width = 600, height = 60, bg = 'Orange')
    canva.place(x = 0, y = 0)
    canva.create_text(290,30,text = "Find data from Orders Table",font = ("Arial",15,"bold"))
    
    a = Label(t, text = 'Order No')
    a.place(x = 50, y = 100)
    cb = ttk.Combobox(t, width = 17)
    cb.place(x = 400, y = 100)
    showorderno()
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
    
    
    bt = Button(t, text = 'Find', bg = 'Green', width = 15, command = findorders)
    bt.place(x = 50, y = 400)
    
    bt3 = Button(t, text = 'Close', bg = 'Red', width = 15, command = btclose)
    bt3.place(x = 450, y = 400)
    t.mainloop()