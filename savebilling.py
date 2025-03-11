import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def savebilllingdash():

    t = tkinter.Tk()
    t.geometry('700x500')
    to_email = ""
    def savebilling():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            messagebox.showerror('Hi','No data found')
        else:
            checkbillno()
            db=pymysql.connect(host='localhost',user='root',password='root',database='IMS')
            cur = db.cursor()
            xe1 = int(e1.get())
            xe2 = int(e2.get())
            xe3 = int(e3.get())
            xe4 = e4.get()
            xe5 = int(e5.get())
            sql = "insert into billing values (%d,%d, %d, '%s', %d)"%(xe1, xe2, xe3, xe4, xe5)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo("Hi there","Billing data is saved")
            findemail()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
    
    def checkbillno():
        db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'IMS')
        cur = db.cursor()
        xe1 = int(e1.get())
        sql = "select count(*) from billing where billNo = %d"%(xe1)
        cur.execute(sql)
        data = cur.fetchone()
        if data[0]==0:
            messagebox.showinfo("hi","Available to use this Bill No")
        else:
            messagebox.showinfo("hi","This billNo already exist please select new billNo")
            t.destroy()
        db.close()
    
    def custData():
        db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
        cur = db.cursor()
        sql = "select custId from customers"
        cur.execute(sql)
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i[0])
        db.close()
        e3['values']=lst
    
    def orderNo():
        db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
        cur = db.cursor()
        sql = "select orderNo from orders"
        cur.execute(sql)
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i[0])
        db.close()
        e2['values']=lst
        
    def findemail():
        db=pymysql.connect(host='localhost',user='root',password='root',database='Ims')
        cur = db.cursor()
        xe3 = int(e3.get())
        sql = "select email from customers where custId = %d"%(xe3)
        cur.execute(sql)
        data = cur.fetchone()
        global to_email
        to_email = data[0]
        sendmail()
        
    def sendmail():
        global to_email
        from_address = "khanshariq.2895@gmail.com"
        to_address = to_email
        
        
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Bill"
        msg['From'] = from_address
        msg['To'] = to_address
        
        # Create the message (HTML).
        html = "Your total bill is <br>"+str(e5.get())+"<br> and the date of Dispatch of your order is "+e4.get()
        
        
        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')
        messagebox.showinfo('Hi there', 'Mail Sent')
    
    
        
        # Attach parts into message container
        msg.attach(part1)
        
        # Credentials
        username = 'khanshariq.2895@gmail.com'  
        password = 'vjjoplvixduasozh'
        
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
    
    def btclose():
        t.destroy()
    
    canva = Canvas(t, width = 600,height = 60,bg = 'Orange')
    canva.place(x = 0, y = 0)
    canva.create_text(290,30,text = "Insert Data into Billing Table" ,font=("Arial", 15, "bold"))
    
    a = Label(t, text = 'Bill No')
    a.place(x = 50, y = 100)
    e1 = Entry(t, width = 20)
    e1.place(x = 400, y = 100)
    btcheck = Button(t,text ='check',width = 17, command = checkbillno)
    btcheck.place(x = 550, y = 100)
    b = Label(t, text = 'Order No')
    b.place(x = 50 ,y = 140)
    e2 = ttk.Combobox(t, width = 17)
    e2.place(x = 400, y = 140)
    orderNo()
    c = Label(t, text = 'Customer Id')
    c.place(x = 50 , y = 180)
    e3 = ttk.Combobox(t, width = 17)
    e3.place(x = 400, y = 180)
    custData()
    d = Label(t, text = 'Dispatch Date')
    d.place(x = 50, y = 220)
    e4 = Entry(t, width = 20)
    e4.place(x = 400, y = 220)
    f = Label(t,text = 'Amount')
    f.place(x= 50, y = 260)
    e5 = Entry(t, width =20)
    e5.place(x = 400, y = 260)
    
    
    
    bt = Button(t, text = 'Save', width = 25, fg = 'Green', command = savebilling)
    bt.place(x = 50, y = 400)
    bt2 = Button(t, text = 'Close', width = 25, fg = 'Red', command = btclose)
    bt2.place(x = 350, y = 400)
    t.mainloop()
