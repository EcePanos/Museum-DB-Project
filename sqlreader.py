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





def searchartist():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM artist WHERE idArtist=',artistid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchartwork():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM artwork WHERE idArtwork=',artworkid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchemployee():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM employee WHERE idEmployee=',employeeid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchassignment():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM employee_assigned_to_room WHERE Room_idRoom=',assignmentid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchroom():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM room WHERE idRoom=',roomid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchsupplier():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM supplier WHERE idSupplier=',supplierid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchorder():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM supplier_equips_room WHERE Room_idRoom=',orderid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
    return
def searchgroup():
    result.delete(1.0,END)
    string=""
    seq=('SELECT * FROM visitor_group WHERE idVisitor_Group=',groupid.get())
    string=string.join(seq)
    cursor.execute(string)
    for entries in cursor.fetchall():
        result.insert(END,entries)
        result.insert(END,"\n")
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





app2=Tk()
app2.title("Detailed Search")
app2.geometry('800x320+200+200')
buttona=Button(app2,text="Search Artist",width=20,command=searchartist)
buttona.grid(row=0,column=0)

artist=StringVar(None)
artistid=Entry(app2,textvariable=artist)
artistid.grid(row=0,column=1)
artistid.insert(0,"Artist id")

buttonb=Button(app2,text="Search Artwork",width=20,command=searchartwork)
buttonb.grid(row=1,column=0)

artwork=StringVar(None)
artworkid=Entry(app2,textvariable=artwork)
artworkid.grid(row=1,column=1)
artworkid.insert(0,"Artwork id")

buttonc=Button(app2,text="Search Employee",width=20,command=searchemployee)
buttonc.grid(row=2,column=0)

employee=StringVar(None)
employeeid=Entry(app2,textvariable=employee)
employeeid.grid(row=2,column=1)
employeeid.insert(0,"Employee id")

buttond=Button(app2,text="Search Assingment",width=20,command=searchassignment)
buttond.grid(row=3,column=0)

assignment=StringVar(None)
assignmentid=Entry(app2,textvariable=assignment)
assignmentid.grid(row=3,column=1)
assignmentid.insert(0,"Room id")

buttone=Button(app2,text="Search Room",width=20,command=searchroom)
buttone.grid(row=4,column=0)

room=StringVar(None)
roomid=Entry(app2,textvariable=room)
roomid.grid(row=4,column=1)
roomid.insert(0,"Room id")

buttonf=Button(app2,text="Search Supplier",width=20,command=searchsupplier)
buttonf.grid(row=5,column=0)

supplier=StringVar(None)
supplierid=Entry(app2,textvariable=supplier)
supplierid.grid(row=5,column=1)
supplierid.insert(0,"Supplier id")

buttong=Button(app2,text="Search Order",width=20,command=searchorder)
buttong.grid(row=6,column=0)

order=StringVar(None)
orderid=Entry(app2,textvariable=order)
orderid.grid(row=6,column=1)
orderid.insert(0,"Room id")

buttonh=Button(app2,text="Search Group",width=20,command=searchgroup)
buttonh.grid(row=7,column=0)

group=StringVar(None)
groupid=Entry(app2,textvariable=group)
groupid.grid(row=7,column=1)
groupid.insert(0,"Group id")


result=Text(app2,height=3,width=80)
result.grid(row=8,column=0)
result.insert(END,"Results appear here")

app.mainloop()
app2.mainloop()

#cursor.execute("INSERT INTO artist (idArtist,F_Name,L_Name,Age,Address,Phone,Email) VALUES (123,'mitsos','kitsou',18,'nowhere','123','mpla')")
 
    
 


