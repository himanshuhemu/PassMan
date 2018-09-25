import sqlite3
import string
from random import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *

def open_db(tb_name):
    db_con = sqlite3.connect(tb_name , timeout=10)
    db_cursor = db_con.cursor() 
    return db_con,db_cursor

###############################################################################
def genStr():
    stri = "".join(choice(string.ascii_letters) for x in range(randint(4, 6)))
    return stri
    
    
    
def signUp(usname , passw):
    passw=hash(passw)
    conn,cus = open_db("data.db")
    cus.execute('create table if not exists login_det (uname text PRIMARY KEY NOT NULL,password text NOT NULL ,tbname text NOT NULL)')
    tbnm=genStr()
    try:
        cus.execute('insert into login_det( uname , password , tbname ) values (?,?,?)',(usname , passw , tbnm ))
        msg="Success"
        conn.commit()
    except sqlite3.Error as e:     
        if e:
            msg=e
    finally:
        conn.close()                  
    return msg
def user_login(user_name , password):
        msg=' '
        info=False
        tbname=[]
        conn, curs = open_db("data.db")        
        try:
            statement = curs.execute('SELECT uname FROM login_det')

            for row in statement:
                if user_name in row:  # compare one by one
                    print(user_name)
                    pas = curs.execute('SELECT password FROM login_det WHERE uname = ?', (user_name,)).fetchone()
                    password=hash(password)
                    tbname=curs.execute('SELECT tbname FROM login_det WHERE  uname=?',(user_name,)).fetchone()
                    #print(tbname[0])
                    if int(password) == int(pas[0]):
                        print("welcome user"+ user_name)
                        msg="Welcome "+user_name
                        info=True
###########   do stuff after the login
                        #entry
                        #print("DO the entry ")
                        #entry('hemu@gmail.com','idntknw',tbname[0]) 
                        #search('hemu@gmail.com',tbname[0])    
                        #entry_del('hemu@gmail.com',tbname[0])                
                        
                        
                        ###########
                    else:
                        msg ="password incorrect!" # ID is matched
                    return msg,info,tbname[0]    
            msg = "Incorrect ID! You are not a user"
        except IOError:
                msg = "Error occured"
        finally:
                conn.close()
        return msg,info,tbname[0]        
def user_del(user_name):
        conn, curs = open_db("data.db")        
        try:
            statement = curs.execute('SELECT uname FROM login_det')

            for row in statement:
                if user_name in row:  # compare one by one
                    print(user_name)
                    curs.execute('DELETE  FROM login_det WHERE uname = ?', (user_name,))
                    print("User deleted")
                    return 
            print("Incorrect ID! If you are not a user")
        except IOError:
                print("delete statement could not execute!")
        finally:
            conn.commit()    
            conn.close()
        
def entry(Id,passwd,tb_name):
    conn, curs =open_db("data.db")
    curs.execute(' CREATE TABLE IF NOT EXISTS '+tb_name+'(ID TEXT NOT NULL ,PASSWD TEXT NOT NULL)')
    curs.execute('INSERT INTO '+tb_name+'(ID,PASSWD) VALUES(?,?)',(Id,passwd))
    conn.commit()
    conn.close()
  
def search(srch_id,tb_name):
    conn,curs=open_db("data.db")
    pas=curs.execute('select passwd from '+tb_name+' Where ID = ?',(srch_id,)).fetchone()
    print(pas[0])
    conn.close()
        
def entry_del(Id,tb_name):
    conn, curs=open_db("data.db")
    p=curs.execute('DELETE from '+tb_name+' WHERE ID = ?',(Id,)).fetchall()
    conn.commit()
    conn.close()
######################################################
    #testing
#signUp('ter','12345')
#user_login('abc','12345')
#######################################################

####GUI ahead ..........#####


 
window = Tk()
 
window.title("Password Manager")
window.geometry('400x400')   

menu = Menu(window) 
 
new_item = Menu(menu)
def ext():
    window.destroy()
    
menu.add_cascade(label='File', menu=new_item)
new_item.add_command(label='Exit' , command = ext)
new_item = Menu(menu, tearoff=0)
window.config(menu=menu)   
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Sign Up')
 
tab_control.add(tab2, text='Log In')
#####tab1 stuff ####
lbl = Label(tab1, text="Sign Up", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
    
s_lbl1=Label(tab1 , text = "Username ")
s_lbl1.grid(column=0,row=1)
s_lbl2=Label(tab1 ,text="Password")
s_lbl2.grid(column=0,row=2)
s_txt = Entry(tab1,width=20)
s_txt.grid(column=1, row=1)
s_txt1 = Entry(tab1,width=20)
s_txt1.grid(column=1, row=2)
    
def clicked():
        uname=s_txt.get()    
        upas=s_txt1.get()
        msg=signUp(uname,upas)
        messagebox.showinfo('Message title', msg) 
    
btn = Button(tab1, text="Click Me", command=clicked) 
btn.grid(column=1, row=3)

#tab2 stuff#####
l_lbl=Label(tab2, text="Log In",font=("Arial Bold", 20))
l_lbl.grid(column=0, row=0)
    
l_lbl1=Label(tab2 , text = "Username ")
l_lbl1.grid(column=0,row=1)
l_lbl2=Label(tab2 ,text="Password")
l_lbl2.grid(column=0,row=2)
l_txt = Entry(tab2,width=20)
l_txt.grid(column=1, row=1)
l_txt1 = Entry(tab2,width=20)
l_txt1.grid(column=1, row=2)


    
    
    



     
def new_winF(tb): # new window definitio
        
    
    newwin = Toplevel(tab2)
    newwin.geometry('400x400')
    tab_control = ttk.Notebook(newwin)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 =ttk.Frame(tab_control)
    tab_control.add(tab3, text='Entry')
    tab_control.add(tab4, text='Search')
    tab_control.add(tab5, text='Delete')
    
    n_lbl1=Label(tab3 , text = "ID")
    n_lbl1.grid(column=0,row=1)
    n_lbl2=Label(tab3 ,text="Password")
    n_lbl2.grid(column=0,row=2)
    n_txt = Entry(tab3,width=20)
    n_txt.grid(column=1, row=1)
    n_txt1 = Entry(tab3,width=20)
    n_txt1.grid(column=1, row=2)
    tab_control.grid()
    def clk():
        uid=n_txt.get()
        upas=n_txt1.get()
        entry(uid,upas,tb)
        
    btn3 = Button(tab3 , text ="Submit" , command = clk)
    btn3.grid(column =1 , row =3)
    
    
    
    
def clicked2():
    uname=l_txt.get()    
    upas=l_txt1.get()
    msg1,infom,tb = user_login(uname,upas)
    #messagebox.showinfo('Title',msg)
    if infom is True:
        messagebox.showinfo('tit',msg1)
        new_winF(tb)
btn2 = Button(tab2 , text = "Log In" , command = clicked2)
btn2.grid(column=1, row=3)        
#tab_control.pack(expand=1, fill='both')
tab_control.grid() 
window.mainloop()