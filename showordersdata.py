import tkinter
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import*

def showorderdash():

    t = tkinter.Tk()
    t.geometry('600x600')
    
    def showordersdata():
        db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
        cur = db.cursor()
        sql = "select * from orders"
        cur.execute(sql)
        data = cur.fetchall()
        res = ''
        for i in data:
            res = res + str(i[0])+"\t"
            res = res + str(i[1])+"\t"
            res = res + str(i[2])+"\t"
            res = res + str(i[3])+"\t"
            res = res + str(i[4])+"\t"
            res = res + str(i[5])+"\t"
            res = res + str(i[6])+"\t"
            res = res+"\n"
        db.close()
        ta.insert(END,res)
    
    canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
    canva.place(x = 0, y = 0)
    canva.create_text(290,30,text = "show all data from Billing Table" ,font=("Arial", 15, "bold"))
    ta=Text(t,width=70,height=30)
    ta.place(x=20,y=100)
    showordersdata()
    t.mainloop()