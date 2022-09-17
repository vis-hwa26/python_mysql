#main program
import tkinter
from tkinter import *
import pymysql as sqlcon
from tkinter import messagebox
#connection to mysql
con=sqlcon.connect(host="localhost",user="root",password="root",db="project") 
cur=con.cursor()
cur.execute("create database if not exists hospital")#Creating Database
cur.execute("use hospital")
#Creating the Table
cur.execute("create table if not exists appointment_details"
            "("
            "Aadhar_no varchar(12) primary key,"
            "doctor varchar(25),"
            "date varchar(20),"
            "time varchar(10))")




#To register    
def register():
    global e1,e2,e3,e4,e5,e6,root1
    root1=tkinter.Tk()
    root1.geometry("500x500")
    label=tkinter.Label(root1,text="REGISTER YOURSELF",font='arial 15 bold')
    label.place(x=130,y=0)
    l1=tkinter.Label(root1,text="AADHAR CARD NO.")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=tkinter.Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=tkinter.Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=tkinter.Label(root1,text="GENDER M\F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=tkinter.Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=tkinter.Label(root1,text="BLOOD GROUP")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=tkinter.Button(root1,text="SUBMIT",command=entry)
    b1.place(x=150,y=370)
    cur.execute("create table if not exists register"
            "("
            "Aadharcard_no varchar(12) primary key,"
            "Name varchar(50),"
            "Age varchar(5),"
            "Gender varchar(5),"
            "phone_no varchar(10),"
            "blood_grp varchar(5))")

#Inserting Into Table    
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
    query="""INSERT INTO register(Aadharcard_no,Name,Age,Gender,phone_no,blood_grp)
            VALUES("{}","{}","{}","{}","{}","{}")""".format(p1,p2,p3,p4,p5,p6)
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Data","you have been registerd")
    root1.destroy()

    
#To take appointment    
def takeappo():
    global x1,root2
    root2=tkinter.Tk()
    root2.geometry("250x250")
    label=tkinter.Label(root2,text="SHOW APPOINTMENTS",font='arial 10 bold')
    label.place(x=35,y=0)
    l1=tkinter.Label(root2,text="AADHAAR NO.")
    l1.place(x=10,y=50)
    x1=tkinter.Entry(root2)
    x1.place(x=100,y=50)
    b1=tkinter.Button(root2,text='Submit',command=getinfo)
    b1.place(x=50,y=200)
    b2=tkinter.Button(root2,text="Get appointment",command=get_apoint)
    b2.place(x=120,y=200)
    b3=tkinter.Button(root2,text="all_apoint",command=all_apoint)
    b3.place(x=90,y=150)

#To display all appointments..    
def all_apoint():
    cur.execute( """select * from appointment_details""")
    data=cur.fetchall()
    for i in data:
        print(i)
    root2.destroy()    

#Displaying a Table using QUERY.
#Details of alredy taken appoinment.    
def getinfo():
    global x1
    o1=x1.get()
    cur.execute("select * from appointment_details"
    "where Aadhar_no='{}'".format(o1))
    data=cur.fetchone()
    print(data)
    messagebox.showinfo("Data","info in shell")
    root2.destroy()
 
#Taking Appointment    
def get_apoint():
    global a1,doc1,date1,time1,root3
    root3=tkinter.Tk()
    root3.geometry("400x400")
    name=tkinter.Label(root3,text="Appointment")
    name.place(x=170,y=0)
    a=tkinter.Label(root3,text="Aadharno")
    a.place(x=10,y=80)
    a1=tkinter.Entry(root3)
    a1.place(x=100,y=80)
    doc=tkinter.Label(root3,text='Doctor')
    doc.place(x=10,y=150)
    doc1=tkinter.Entry(root3)
    doc1.place(x=100,y=150)
    date=tkinter.Label(root3,text="Date")
    date.place(x=10,y=220)
    date1=tkinter.Entry(root3)
    date1.place(x=100,y=220)
    time=tkinter.Label(root3,text="Time")
    time.place(x=10,y=290)
    time1=tkinter.Entry(root3)
    time1.place(x=100,y=290)
    b1=tkinter.Button(root3,text="Submit",command=insert)
    b1.place(x=170,y=360)
    root2.destroy()


# Inserting into table     
def insert():
    global a1,doc1,date1,time1
    c1=a1.get()
    c2=doc1.get()
    c3=date1.get()
    c4=time1.get()
    query="""INSERT INTO appointment_details(Aadhar_no,doctor,date,time)
                        VALUES("{}","{}","{}","{}")""".format(c1,c2,c3,c4)
    cur.execute(query)
    con.commit()
    messagebox.showinfo("Data","You have been Appointed")
    root3.destroy()

#Doctors List.
def lst_doc():
    root4=tkinter.Tk()
    root4.geometry("500x500")
    
    l=["Dr. sharma","Dr. Verma","Dr. Kumar","Dr. Khan","Dr. Kohli","Dr. singh",
       "Dr. Sidharth","Dr. tendulkar","Dr. Virat","Dr. Leo","Dr. Irfan","Dr. John",
       "Dr. Sanjay","Dr. Shahid"]
    m=["Orthopaedic surgeon","Orthopaedic surgeon","Nephrologist",
       "Nephrologist","Gynaecologist","Gynaecologist","Physician",
       "Physician","Neurologist","Neurologist",'X-ray','X-ray','X-ray','X-ray']
    n=[10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    l1=tkinter.Label(root4,text='NAME OF DOCTORS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=tkinter.Label(root4,text=i)
       l.place(x=20,y=count)

    l2=tkinter.Label(root4,text='DEPARTMENT')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=tkinter.Label(root4,text=i)
       l3.place(x=140,y=count1)
  
    l4=tkinter.Label(root4,text='ROOM NO')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=tkinter.Label(root4,text=i)
       l5.place(x=260,y=count2)   

#List of services available.       
def ser_avail():
    root5=tkinter.Tk()
    root5.geometry("400x400")
    l1=tkinter.Label(root5,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    l2=tkinter.Label(root5,text='ROOM NO.')
    l2.place(x=140,y=10)
    f=["ULTRASOUND","X-RAY","CT Scan","MRI","BLOOD COLLECTION",
       "DIALYSIS","ECG","CHEMIST","LAB"]
    count1=20
    for i in f:
       count1=count1+20
       l3=tkinter.Label(root5,text=i)
       l3.place(x=20,y=count1)
    
    g=[1,2,3,4,5,6,7,8,9]
    count2=20
    for i in g:
       count2=count2+20
       l4=tkinter.Label(root5,text=i)
       l4.place(x=140,y=count2)
    l5=tkinter.Label(root5,text='To avail any of these please contact on our'
                     'no.:- 7042****55')
    l5.place(x=20,y=240)

#Using Fetchone().
def search_one():
    global A
    p1=A.get()
    query2="""Select * from register where Aadharcard_no={}""".format(p1)
    cur.execute(query2)
    data=cur.fetchone()
    print(data)
    print("_________________________________________________")
    root6.destroy()

#Using Fetchall().    
def search_all():
    cur.execute("""SELECT * FROM register""")
    data=cur.fetchall()
    for i in data:
        print(i)
    print("_________________________________________________")    
    root6.destroy()
    
#searching the data.
def search_data():
    global A,root6
    root6=tkinter.Tk()
    root6.geometry("350x350")
    l1=tkinter.Label(root6,text="Aadharno.",font="Arial 15")
    l1.place(x=10,y=0)
    A=tkinter.Entry(root6,width=20)
    A.place(x=120,y=5)
    b1=tkinter.Button(root6,text="Search",command=search_one)
    b1.place(x=120,y=50)
    l2=tkinter.Label(root6,text="------To serach specific Data"
                     "click here^^------")
    l2.place(x=20,y=100)
    b2=tkinter.Button(root6,text="Searchall",command=search_all)
    b2.place(x=120,y=200)
    l3=tkinter.Label(root6,text="------To show all data^^------")
    l3.place(x=20,y=250)

#modification of existing data.
def mod_sub():
    global root7
    root7=tkinter.Tk()
    root7.geometry("300x300")
    b1=tkinter.Button(root7,text="UPDATE",font="arial 20",command=update)
    b1.place(x=20,y=20)
    b2=tkinter.Button(root7,text="DELETE",font="arial 20",command=delete)
    b2.place(x=20,y=150)

#Deleting the data.
def delete():
    global m2,root10
    root10=tkinter.Tk()
    root10.geometry("300x300")
    l1=tkinter.Label(root10,text="******DELETE******",font="arial 20")
    l1.place(x=10,y=10)
    l2=tkinter.Label(root10,text="Aadharno.",font="arial 16")
    l2.place(x=10,y=100)
    m2=tkinter.Entry(root10)
    m2.place(x=150,y=100)
    b1=tkinter.Button(root10,text="Submit",command=do_del,font="arial 10")
    b1.place(x=130,y=220)
    root7.destroy()

def do_del():
    global m2
    s1=m2.get()
    cur.execute("DELETE from register where Aadharcard_no='{}'".format(s1))
    con.commit()
    #con.close()
    messagebox.showinfo("Data","Details Deleted")
    root10.destroy()

#Updating the data.
def update():
    global m1,root8
    root8=tkinter.Tk()
    root8.geometry("300x300")
    l1=tkinter.Label(root8,text="******Modification******",font="arial 20")
    l1.place(x=10,y=10)
    l2=tkinter.Label(root8,text="Aadharno.",font="arial 16")
    l2.place(x=10,y=100)
    m1=tkinter.Entry(root8)
    m1.place(x=150,y=100)
    b1=tkinter.Button(root8,text="Submit",command=modify,font="arial 20")
    b1.place(x=130,y=220)
    root7.destroy()
    
def modify():
    global p1,x4,x5,root9
    root9=tkinter.Tk()
    root9.geometry("500x500")
    global m1
    p1=m1.get()
    cur.execute('select * from register where Aadharcard_no={}'.format(p1))
    
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)
    l1=tkinter.Label(root9,text='DATA MODIFICATION',font="arial 15 bold")
    l1.place(x=75,y=10)
    l2=tkinter.Label(root9,text='WHAT YOU WANT TO CHANGE')
    l2.place(x=50,y=200)
    l3=tkinter.Label(root9,text='1.NAME')
    l3.place(x=50,y=220)
    l4=tkinter.Label(root9,text='2.AGE')
    l4.place(x=50,y=240)
    l5=tkinter.Label(root9,text='3.GENDER')
    l5.place(x=50,y=260)
    l6=tkinter.Label(root9,text='4.PHONE')
    l6.place(x=50,y=280)
    l7=tkinter.Label(root9,text='5.BLOOD GROUP')
    l7.place(x=50,y=300)
    x2=tkinter.Label(root9,text='ENTER TO CHANGE')
    x2.place(x=30,y=330)
    x4=tkinter.Entry(root9)
    x4.place(x=160,y=330)
    choice=x4.get()
    b=tkinter.Button(root9,text='Submit',font="arial 16",command=do_modify) 
    b.place(x=130,y=400)
    L1=tkinter.Label(root9,text='OLD DETAILS')
    L1.place(x=50,y=50)
    L2=tkinter.Label(root9,text='ENTER NEW DETAIL:')
    L2.place(x=30,y=360)
    x5=tkinter.Entry(root9)
    x5.place(x=160,y=360)
    new=x5.get()
    for i in dat:
            name=tkinter.Label(root9,text='NAME:-')
            name.place(x=50,y=80)
            name1=tkinter.Label(root9,text=i[1])
            name1.place(x=150,y=80)
            age=tkinter.Label(root9,text='AGE:-')
            age.place(x=50,y=100)
            age1=tkinter.Label(root9,text=i[2])
            age1.place(x=150,y=100)
            gen=tkinter.Label(root9,text='GENDER:-')
            gen.place(x=50,y=120)
            gen1=tkinter.Label(root9,text=i[3])
            gen1.place(x=150,y=120)
            pho=tkinter.Label(root9,text='PHONE:-')
            pho.place(x=50,y=140)
            pho1=tkinter.Label(root9,text=i[4])
            pho1.place(x=150,y=140)
            bg=tkinter.Label(root9,text='BLOOD GROUP:-')
            bg.place(x=50,y=160)
            bg1=tkinter.Label(root9,text=i[5])
            bg1.place(x=150,y=160)
    root8.destroy()        
             

def do_modify():
    global ad,p1,x4,x5
    choice=x4.get()
    new=x5.get()
    if choice=='1':
        d1 = "update register set Name = '{}'"
        "WHERE Aadharcard_no = '{}'".format(new,p1)
        cur.execute(d1)
        con.commit()
        con.close()
    elif choice=='2':
        d2 = "update register set Age = '{}' "
        "WHERE Aadharcard_no = '{}'".format(new,p1)
        cur.execute(d2)
        con.commit()
        con.close()
    elif choice=='3':
        d3="update register set Gender = '{}' "
        "WHERE Aadharcard_no = '{}'".format(new,p1)
        cur.execute(d3)
        con.commit()
        con.close()
    elif choice=='4':
        d4="update register set phone_no = '{}' "
        "WHERE Aadharcard_no = '{}'".format(new,p1)
        cur.execute(d4)
        con.commit()
        con.close()
    elif choice=='5':
        d5="update register set blood_grp = '{}'"
        "WHERE Aadharcard_no = '{}'".format(new,p1)
        cur.execute(d5)
        con.commit()
        con.close()
    else:
        pass
    messagebox.showinfo("Data","Details Updated")
    root9.destroy()

root=tkinter.Tk()
root.geometry("800x800")
l1=tkinter.Label(root,text="CITY HOSPITAL",font="arial 40 bold",bg='light blue')
l1.place(x=200,y=0)
b1=tkinter.Button(text="Registration",font="arial 20 bold",bg='yellow',
                  command=register)
b1.place(x=100,y=100)
b2=tkinter.Button(text="Appointment",font="arial 20 bold",bg='yellow',
                  command=takeappo)
b2.place(x=450,y=100)
b3=tkinter.Button(text="List of Doctors",font="arial 20 bold",bg='yellow',
                  command=lst_doc)
b3.place(x=100,y=200)
b4=tkinter.Button(text="Services available",font='arial 20 bold',bg='yellow',
                  command=ser_avail)
b4.place(x=450,y=200)
b7=tkinter.Button(text="View data",font='arial 20 bold',bg='yellow',
                  command=search_data)
b7.place(x=100,y=300)
b5=tkinter.Button(text="Modify existing data",font='arial 20 bold',bg='yellow',
                  command=mod_sub)
b5.place(x=450,y=300)
b6=tkinter.Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='violet')
b6.place(x=350,y=400)
canvas=Canvas(root,width=600,height=600)
canvas.place(x=0,y=480)
my_image=PhotoImage(file='C:\\Users\\VIPUL PATEL\\Documents\\hos.gif')
canvas.create_image(240,0, anchor = NW, image=my_image)





