import tkinter
import tkinter.messagebox
from tkinter import  *
import random as rd
from PIL import ImageTk,Image
import datetime
from turtle import bgcolor, color 
import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="Asingh@6388")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists hello")
cur.execute("use hello")

cur.execute("create table if not exists apt"
            "("
            "idno varchar(12) primary key,"
            "name char(20),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")



#  Message for registration by ashutosh
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
        
    cur.execute('insert into apt values(%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,))
    con.commit()
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

#  For registration by ashutosh
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    root1.config(background='#B2DFEE')
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold',bg='#B2DFEE')
    label.pack()
    frame=Frame(root1,height=500,width=200,bg='#B2DFEE')
    frame.pack()
    l1=Label(root1,text="PATIENT ID",bg='#B2DFEE')
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=Label(root1,text="NAME",bg='#B2DFEE')
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=Label(root1,text="AGE",bg='#B2DFEE')
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=Label(root1,text="GENDER M\F",bg='#B2DFEE')
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=Label(root1,text="PHONE",bg='#B2DFEE')
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=Label(root1,text="BLOOD GROUP",bg='#B2DFEE')
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=Button(root1,text="SUBMIT",command=entry,bg='#B2DFEE')
    b1.place(x=150,y=370)
    
    root.resizable(True,True)
    root1.mainloop()
  
#  Message for appointment and by Piyush
def apo_details():
    global x2
    p1 = x2.get()
    doctors_info = {
        1: [("Dr. Varun", 201, 3), ("Dr. Hrithik", 202, 3)],
        2: [("Dr. Sidharth", 207, 5), ("Dr. Abhishek", 208, 5)],
        3: [("Dr. Salman", 203, 3), ("Dr. Shahrukh", 204, 3)],
        4: [("Dr. Ajay", 209, 6), ("Dr. Ranveer", 200, 6)],
        5: [("Dr. Akshay", 205, 4), ("Dr. Amir", 206, 4)],
        6: [("Dr. Irfan", 1, 1), ("Dr. John", 2, 1), ("Dr. Sanjay", 3, 1), ("Dr. Shahid", 4, 1)],
    }

    if int(p1) in doctors_info:
        doctor, room, days = rd.choice(doctors_info[int(p1)])
        appointment_no = rd.choice([23, 34, 12, 67, 53, 72])
        appointment_date = datetime.date.today() + datetime.timedelta(days=days)
        details = f"Your appointment is fixed with {doctor} (Room no: {room})\nDate: {appointment_date}\nAppointment no: {appointment_no}"
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS", details)
    else:
        tkinter.messagebox.showwarning('WRONG INPUT', 'PLEASE ENTER VALID VALUE')
#  For appointment by Ashutosh
def get_apoint():
    global x1,x2
    p1=x1.get()  
    cur.execute('select * from apt where idno=(%s)',(p1,)) # here i am just matching the patient id which is stored in database 
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")# when id is not found then it will show error and next piece of command occurs when id matches
    else:
        root3=Tk()
        root3.config(background='#B2DFEE')
        label=Label(root3,text="APPOINTMENT",font='arial 25 bold',bg='#B2DFEE')
        label.pack()
        frame=Frame(root3,height=500,width=300,bg='#B2DFEE')
        frame.pack()
        if i[3]=='M' or i[3]=='m':
                x="Mr."
                name2=Label(root3,text=i[1],bg='#B2DFEE')
                name2.place(x=140,y=80)
        else:
                x="Mrs\Ms."
                name2=Label(root3,text=i[1],bg='#B2DFEE')
                name2.place(x=170,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME',bg='#B2DFEE')
            name.place(x=50,y=80)
            name1=Label(root3,text=x,bg='#B2DFEE')
            name1.place(x=120,y=80)
            age=Label(root3,text='AGE:-',bg='#B2DFEE')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2],bg='#B2DFEE')
            age1.place(x=100,y=100)
            phone=Label(root3,text='PHONE:-',bg='#B2DFEE')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[4],bg='#B2DFEE')
            phone1.place(x=100,y=120)
            bg=Label(root3,text='BLOOD GROUP:-',bg='#B2DFEE')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[5],bg='#B2DFEE')
            bg1.place(x=150,y=140)


        L=Label(root3,text='DEPARTMENTS',bg='#B2DFEE')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.Cardiologist ",bg='#B2DFEE')
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.Rheumatologist',bg='#B2DFEE')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Psychitrist',bg='#B2DFEE')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Neurologist',bg='#B2DFEE')
        L4.place(x=50,y=310)
        L5=Label(root3,text='5.Otolaryngonologist',bg='#B2DFEE')
        L5.place(x=50,y=330)
        L6=Label(root3,text='6.MI Room',bg='#B2DFEE')
        L6.place(x=50,y=350)
        L7=Label(root3,text='Enter',bg='#B2DFEE')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=150,y=370)        
        B1=Button(root3,text='Submit',command=apo_details,bg='#B2DFEE')
        B1.place(x=120,y=440)   
        root3.resizable(True,True)
        root3.mainloop()

#  For Adhaar no input by piyush
def apoint():
    global x1
    root2=Tk()
    root2.config(background='#B2DFEE')
    label=Label(root2,text="APPOINTMENT",font='arial 25 bold',bg='#B2DFEE')
    label.pack()
    frame=Frame(root2,height=200,width=200,bg='#B2DFEE')
    frame.pack()
    l1=Label(root2,text="PATIENT ID ",bg='#B2DFEE')
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2)
    x1.place(x=100,y=130)
    b1=Button(root2,text='Submit',command=get_apoint,bg='#B2DFEE')
    b1.place(x=100,y=160)
    root2.resizable(True,True)
    root2.mainloop()
    
#  List of doctors by kunal
def lst_doc():
    root4=Tk()
    
    l=["Dr. Varun","Dr. Hrithik","Dr. Salman","Dr. Shahrukh","Dr. Akshay","Dr. Amir","Dr. Sidharth","Dr. Abhishek","Dr. Ajay","Dr. Ranveer",'Dr. Irfan','Dr. John','Dr. Sanjay','Dr. Shahid']
    m=["Cardiologist","Cardiologist","Psychitrist","Psychitrist","Otolaryngonologist","Otolaryngonologist","Rheumatologist","Rheumatologist","Neurologist","Neurologist",'MI room','MI room','MI room','MI room']
    n=[201,202,203,204,205,206,207,208,209,200,401,402,403,404]

    frame=Frame(root4,height=500,width=500,bg='#B2DFEE')
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF DOCTORS',bg='#B2DFEE') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(root4,text=i,bg='#B2DFEE')
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT',bg='#B2DFEE')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(root4,text=i,bg='#B2DFEE')
       l3.place(x=140,y=count1)

    l4=Label(root4,text='ROOM NO',bg='#B2DFEE')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(root4,text=i,bg='#B2DFEE')
       l5.place(x=260,y=count2)
    root.resizable(False,False)
    root4.mainloop()
#by aditya
def ser_avail():
    root5=Tk()
    frame=Frame(root5,height=500,width=500, bg='#B2DFEE' )
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE',fg = 'black',bg='#B2DFEE')
    l1.place(x=20,y=10)
    f=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root5,text=i,bg='#B2DFEE')
       l3.place(x=20,y=count1)
    l2=Label(root5,text='ROOM NO.',bg='#B2DFEE')
    l2.place(x=140,y=10)
    g=[101,102,103,104,105,301,302,303,304]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root5,text=i,bg='#B2DFEE')
       l4.place(x=140,y=count2)
    l5=Label(root5,text='To avail any of these please contact on our no.:- 8969484804',bg='#B2DFEE')
    l5.place(x=20,y=240)
    root5.resizable(False,False)
    root5.mainloop()
       
# by ashutosh
root=Tk()
root.title("Hospital")
root.config(background="#66CDAA")



label=Label(root,text="HopeTech",fg="black",font="arial 40 bold",bg='#7D9EC0')



b1=Button(text="Registration",font="arial 20 bold",bg='#B2DFEE',fg='black',command=register)
b2=Button(text="Appointment",font="arial 20 bold",bg='#B2DFEE',fg='black',command=apoint)
b3=Button(text="List of Doctors",font="arial 20 bold",bg='#B2DFEE',fg='black',command=lst_doc)
b4=Button(text="Services available",font='arial 20 bold',bg='#B2DFEE',fg='black',command=ser_avail)
#b5=Button(text="VIEW",font='arial 20 bold',bg='cyan',command=view_data)
b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='#B2DFEE',fg='black')



label.pack()

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="WELCOME TO\n HMS BY HopeTech", bg='black', fg='white', font=('Courier',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

b1.pack(side=LEFT,padx=40)
b2.pack(side=LEFT,padx=40)
b3.pack(side=LEFT,padx=40)
b4.pack(side=LEFT,padx=40)
#b5.pack(side=LEFT,padx=15)
b6.pack(side=LEFT,padx=40)
frame=Frame(root,height=650,width=65,bg="#66CDAA")



frame.pack()
root.resizable(True,True)
root.mainloop()