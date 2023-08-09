from tkinter import*
from PIL import Image,ImageTk
import tkinter.messagebox as m 
import sqlite3
# from operator import itemgetter

main=Tk()
main.title("Snake game")
main.geometry("450x500")
main.resizable(0,0)

# conn=sqlite3.connect("database1.db")
# c=conn.cursor()
# c.execute("""CREATE TABLE address(
#              name1 text,
#              name2 text,
#              Age integer,
#              email text,
#              name3 text,
#              password text
#     )""")
# print("table is created")
# conn.commit()
# conn.close()
 
my_image=ImageTk.PhotoImage(Image.open("C:\\Users\\manse\\OneDrive\\Desktop\\project\\cutu2.jpg"))
my_label=Label(image=my_image)
my_label.pack()
  
Text=Label(text="Login and Registration",font=50,bg="lavender")
Text.place(x=30,y=120)

def submit():
        conn=sqlite3.connect('database1.db')
        c=conn.cursor()
        c.execute ("INSERT INTO addresses VALUES(:name1,:name2,:Age,:Email,:name3,:password)",{
        'name1':e1.get(),
        'name2':e2.get(),
        'Age':e3.get(),
        'Email':e4.get(),
        'name3':e5.get(),
        'password':e6.get(),
        })
      

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)

        conn.comit()

        m.showinfo("Addresses",'Inserted successfully')

def record():
    conn=sqlite3.connect('database1.db')
    c=conn.cursor()

    c.execute("SELECT *,oid From addresses")
    records=c.fetchall()
    print (records)
    
    print_record=' '
    for record in records:
        print_record += str(record[0]) +' '+ str(record[1])+' ' + int(record[2])+' ' + str(record[3])+' ' +str(record[4]+' '+str(record[5])+' ')

    conn.commit()

# delete_box=Entry(main,width=30)
# delete_box.place(x=90,y=120)

# delete_box_label=Label(main,text="Delete ID")
# delete_box_label.place(x=90,y=130)

# delete_btn=Button(main,text="Delete",command=delete_box)
# delete_btn.place(x=110,y=140)

def delete():
    conn=sqlite3.connect('database1.db')
    c=conn.cursor()

    c.execute("DELETE from addresses WHERE oid = ")
    conn.commit()
    m.showinfo( title = "Record", message = "Data updated sucessfully")

def update():
    conn=sqlite3.connect('database1.db')
    c=conn.cursor()

    # record_id=delete_box.get()

def registration():
    game=Tk()
    game.title("Register")
    game.geometry("600x550")
    game.resizable(0,0)
    
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
   
    my_image2=ImageTk.PhotoImage(Image.open("C:\\Users\\manse\\OneDrive\\Desktop\\project\\bg3.jpg"))
    my_label2=Label(image=my_image2)
    my_label2.pack()

    global e1,e2,e3,e4,e5,e6

    register=Label(game,text="Registration Form", fg="darkolivegreen3",font=("bold",38))
    register.place(x=152,y=24)
    
    name1=Label(game,text="First name",fg="skyblue4",font=2)
    name1.place(x=100,y=120)
    name2=Label(game,text="Last name",fg="skyblue4",font=12)
    name2.place(x=100,y=150)
    Age=Label(game,text="Age",fg="skyblue4",font=12)
    Age.place(x=110,y=180)
    Email=Label(game,text="Email",fg="skyblue4",font=12)
    Email.place(x=100,y=205)
    name3=Label(game,text="Username",fg="skyblue4",font=12)
    name3.place(x=100,y=230)
    password=Label(game,text="password",fg="skyblue4",font=12)
    password.place(x=100,y=255)
    e1=Entry(game,width=20)
    e1.place(x=200,y=125)
    e2=Entry(game)
    e2.place(x=200,y=157)
    e3=Entry(game)
    e3.place(x=200,y=185)
    e4=Entry(game)
    e4.place(x=200,y=210)
    e5=Entry(game)
    e5.place(x=200,y=234)
    e6=Entry(game)
    e6.place(x=200,y=259)

    submit=Button(game,text="Submit",font=25,bg="thistle",command=INSERT)
    submit.place(x=190,y=380)
    btn=Button(game,text="Exit",bg="ivory4",command=game.destroy)
    btn.place(x=430,y=500)

def login():
    log=Tk()
    log.title("Login")
    log.geometry("400x400")
    log.resizable(0,0)

   #  con=mysql.connector(host="local host",user="root",password=" ",database="login and register")
   #  cursor = con.cursor()
   #  conn = mysql.connector.connect(host="localhost", user="root", password="" , database="loginandregister")
   #  cursor2 = conn.cursor()
  
    bigText = Label(text="Login", font="verdana 20 bold")
    bigText.place(x=140, y=30)

    username = Label(log, text="Username")
    username.place(x=100, y=150)
    password2 = Label(log, text="Password")
    password2.place(x=100,y=180)

    e1 = Entry()
    e1.place(x=160,y=150)
    e1.insert(0,'Username')
    e2 = Entry()
    e2.place(x=160,y=180)
    e2.insert(0,'password')
    submit2=Button(log,text="Login")
    submit2.place(x=190,y=230)
    def check ():
       a=Toplevel()
   #     sqlCommand1 = "select email from register"
   #     sqlCommand2 = "select password from register"

   #    #  cursor.execute(sqlCommand1)
   #    #  cursor2.execute(sqlCommand2)
   #     email = e1.get()
   #     password = e2.get()
        
   #     if emai==email and password==password2:
   #         m.show(title="Done",message="Login is Done")
   #     else:
   #         m.show(title="error",message="Something went wrong")

   #  login = Button(login, text="Login", fg="green", command=check)
   #  login.place(x=160, y=200)
   #  btnExit = Button(login, text="Exit", bg="pink", command=login.destroy)
   #  btnExit.place(x=350, y=350)

   #  a.mainloop()


def registration_destroy(): 
   main.destroy()
   registration()


def login_destroy(): 
   main.destroy()
   login()

goToLogin = Button(main,text="Login",fg="deepskyblue2",font="verdana 10 bold",command=login_destroy)
goToLogin.place(x=50,y=200)

goToRegister = Button(main,text="Register",fg="deepskyblue2",font="verdana 10 bold",command=registration_destroy)
goToRegister.place(x=120,y=200)

btnExit = Button(main,text="Exit",bg="white",font="bold")
btnExit.place(x=374,y=460)

main.mainloop()

# game.mainloop()