import tkinter
import pymysql
from tkinter import*

t=tkinter.Tk()
t.geometry('600x600')

def showproductsdata():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
    cur = db.cursor()
    sql = "select * from products"
    cur.execute(sql)
    data = cur.fetchall()
    show = ''
    for i in data:
        show = show +str(i[0])+"\t"
        show = show +str(i[1])+"\t"
        show = show +str(i[2])+"\t"
        show = show +str(i[3])+"\t"
        show = show +str(i[4])+"\t"
        show = show +"\n"
    db.close()
    ta.insert(END,show)
canva = Canvas(t, width = 600,height = 60,bg = 'light green')
canva.place(x = 0, y = 0)
canva.create_text(290,30,text = "show all data from Products Table" ,font=("Arial", 15, "bold"))
ta=Text(t,width=70,height=30)
ta.place(x=20,y=100)
showproductsdata()
t.mainloop()