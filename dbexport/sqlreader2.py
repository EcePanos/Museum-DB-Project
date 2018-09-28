import MySQLdb
from Tkinter import *
import tkMessageBox

def login():
    global db
    global cursor
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user=yourName.get(), # your username
                      passwd=yourpass.get(), # your password
                      db="mydb") # name of the data base
    cursor = db.cursor()
    app1.destroy()
app1=Tk()
app1.title("Log In")
app1.geometry('450x300+200+200')
labelText1=StringVar()
labelText1.set("Username:")
label1=Label(app1,textvariable=labelText1,height=4)
label1.pack()
custName=StringVar(None)
yourName=Entry(app1,textvariable=custName)
yourName.pack()
labelText2=StringVar()
labelText2.set("Password:")
label2=Label(app1,textvariable=labelText2,height=4)
label2.pack()
custpass=StringVar(None)
yourpass=Entry(app1,textvariable=custpass,show="*")
yourpass.pack()
button0=Button(app1,text="Confirm",width=20,command=login)
button0.pack(side='bottom',padx=15,pady=15)
app1.mainloop()

#db = MySQLdb.connect(host="localhost", # your host, usually localhost
 #                    user="root", # your username
  #                    passwd="password", # your password
   #                   db="mydb") # name of the data base

def selectartists():
    text.delete(1.0,END)
    seq=('SELECT * FROM artist')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectartworks():
    text.delete(1.0,END)
    seq=('SELECT * FROM artwork')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectemployees():
    text.delete(1.0,END)
    seq=('SELECT * FROM employee')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectassignments():
    text.delete(1.0,END)
    seq=('SELECT * FROM employee_assigned_to_room')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectrooms():
    text.delete(1.0,END)
    seq=('SELECT * FROM room')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectsuppliers():
    text.delete(1.0,END)
    seq=('SELECT * FROM supplier')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectorders():
    text.delete(1.0,END)
    seq=('SELECT * FROM supplier_equips_room')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def selectvisitors():
    text.delete(1.0,END)
    seq=('SELECT * FROM visitor_group')
    cursor.execute(seq)
    for entries in cursor.fetchall():
        text.insert(END,entries)
        text.insert(END,"\n")
    return
def execute():
    seq=text.get(1.0,END)
    cursor.execute(seq)
    db.commit()
    return

app=Tk()
app.title("Modern Art Museum DBMS")
app.geometry=('1024x600+200+200')
button1=Button(app,text="List Artists",width=20,command=selectartists)
button1.pack(padx=15,pady=15)
button2=Button(app,text="List Artworks",width=20,command=selectartworks)
button2.pack(padx=15,pady=15)
button3=Button(app,text="List Employees",width=20,command=selectemployees)
button3.pack(padx=15,pady=15)
button4=Button(app,text="List Assignments",width=20,command=selectassignments)
button4.pack(padx=15,pady=15)
button5=Button(app,text="List Rooms",width=20,command=selectrooms)
button5.pack(padx=15,pady=15)
button6=Button(app,text="List Suppliers",width=20,command=selectsuppliers)
button6.pack(padx=15,pady=15)
button7=Button(app,text="List Supply Orders",width=20,command=selectorders)
button7.pack(padx=15,pady=15)
button8=Button(app,text="List Visitor Groups",width=20,command=selectvisitors)
button8.pack(padx=15,pady=15)
S = Scrollbar(app)
text=Text(app,height=3,width=50)
S.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)
S.config(command=text.yview)
text.config(yscrollcommand=S.set)
text.insert(END,"Insert SQL query here")
button9=Button(app,text="Commit SQL query",width=20,command=execute)
button9.pack(padx=15,pady=15)
app.mainloop()

#cursor.execute("INSERT INTO artist (idArtist,F_Name,L_Name,Age,Address,Phone,Email) VALUES (123,'mitsos','kitsou',18,'nowhere','123','mpla')")
 
    
   # if check=="3":
    #    db.close()
     #   commit=0


