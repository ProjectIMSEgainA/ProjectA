import tkinter 
import pymysql
from tkinter import*
t=tkinter.Tk()
t.geometry("600x500")
def showcustomersdata():
    db=pymysql.connect(host = "Localhost", user = "root", password = "root",database = "Ims")
    cur=db.cursor()
    sql = "select * from customers"
    cur.execute(sql)
    data = cur.fetchall()
    show = ''
    for i in data:
        show = show +str(i[0])+"\t"
        show = show +str(i[1])+"\t"
        show = show +str(i[2])+"\t"
        show = show +str(i[3])+"\t"
        show = show +str(i[4])+"\t"
        show = show + "\n"
    db.close()
    ta.insert(END,show)
d=Canvas(t,width = 600, height = 60,bg= "orange" )
d.place(x=0,y=0)
d.create_text(290,30,text = "Show Data Customers Table",font = ("Times New Roman",15,"bold"))
ta=Text(t,width=70,height=30)
ta.place(x=20,y=100)
showcustomersdata()
t.mainloop()