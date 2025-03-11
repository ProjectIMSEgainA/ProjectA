import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
from saveorders import*
from deleteorders import*
from findorders import*
from updateorders import*
from showordersdata import*
from navigateorders import*



t = tkinter.Tk()
t.geometry('450x450') 
canva = Canvas(t, width = 450,height = 60,bg = 'Orange')
canva.place(x = 0, y = 0)
canva.create_text(220,30,text = "order Dashboard" ,font=("Arial", 15, "bold"))

bt1 = Button(t, text = 'Insert', width = 20, fg= 'Green', command = saveorderdash)
bt1.place(x = 50, y = 200)
bt2 = Button(t, text = 'Delete', width = 20, fg ='Red', command = deleteorderdash)
bt2.place(x = 250, y = 200)
bt3 = Button(t, text = 'Find', width = 20, fg = 'Green' , command = findorderdash)
bt3.place(x = 50, y = 250)
bt4 = Button(t, text = 'Update', width = 20, fg = 'Green', command = updateorderdash)
bt4.place(x = 250, y = 250)
bt5 = Button(t, text = 'Show_Data', width = 20, fg = 'Green', command = showorderdash)
bt5.place(x = 50, y = 300)
bt5 = Button(t, text = 'Navigator', width = 20, fg = 'Green', command = navigateorderdash)
bt5.place(x = 250, y = 300)

t.mainloop()