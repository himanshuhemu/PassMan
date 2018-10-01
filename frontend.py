
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import backend as bk

 
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
s_lbl3=Label(tab1 , text="Note")
s_lbl3.grid(column =0, row=5)
s_lbl4=Label(tab1 , text=">Password must be 8 character long ")
s_lbl4.grid(column =1, row=6)    
s_lbl5=Label(tab1 , text=">It must contain Capital Letter")
s_lbl5.grid(column =1, row=7)    
s_lbl5=Label(tab1 , text=">It must contain a Special Character")
s_lbl5.grid(column =1, row=8)    
s_lbl5=Label(tab1 , text=">It must contain a Number")
s_lbl5.grid(column =1, row=9)        

def clicked():
        uname=s_txt.get()    
        upas=s_txt1.get()
        if bk.evlt(upas):
            msg=bk.signUp(uname,upas)
        else:
            msg="Password not Valid "
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
    menu = Menu(newwin) 
    def qt():
        newwin.destroy()
    new_item = Menu(menu)    
    menu.add_cascade(label='File', menu=new_item)
    new_item.add_command(label='Log Out' , command = qt)
    new_item = Menu(menu, tearoff=0)
    newwin.config(menu=menu)   
    
    tab_control = ttk.Notebook(newwin)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 =ttk.Frame(tab_control)
    tab_control.add(tab3, text='Entry')
    tab_control.add(tab4, text='Search')
    tab_control.add(tab5, text='Delete')
     
    n_lbl=Label(tab3, text="Do A Entry ",font=("Arial Bold", 20))
    n_lbl.grid(column=0, row=0)

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
        msg=bk.entry(uid,upas,tb)
        messagebox.showinfo("Info",msg)
    btn3 = Button(tab3 , text ="Submit" , command = clk)
    btn3.grid(column =1 , row =3)
    
    s_lbl=Label(tab4, text="Search A Password ",font=("Arial Bold", 10))
    s_lbl.grid(column=0, row=0)

    s_lbl = Label(tab4 , text="ID")
    s_lbl.grid(column=0,row=1)
    s_txt1= Entry(tab4 , width=20)
    s_txt1.grid(column=1 , row=2)
    s_lbl2 = Label(tab4 ,text = "Password")
    s_lbl2.grid(column=0,row=3)
    p_ans=Label(tab4 , text= ' ')
    p_ans.grid(column=1,row=3)
    def ck():
        s_id=s_txt1.get()
        ans1,msg=bk.search(s_id,tb)
        d_ans=decrypt(tb,ans1[0])
        p_ans["text"]=d_ans
        messagebox.showinfo('Info',msg)        
    btn4= Button(tab4 , text="Search" , command = ck)
    btn4.grid(column=0,row=3)
    
    d_lbl=Label(tab5, text="Delete A Record",font=("Arial Bold", 10))
    d_lbl.grid(column=0, row=0)
    
    d_lbl = Label(tab5 , text="ID")
    d_lbl.grid(column=0,row=1)
    d_txt= Entry(tab5 , width=20)
    d_txt.grid(column=1 , row=1)
    def dk():
        dlt=d_txt.get()
        mesg=bk.entry_del(dlt,tb)
        messagebox.showinfo('Info ' ,mesg)
    btn5= Button(tab5 , text="Delete" , command = dk)
    btn5.grid(column=0,row=3)
    
    
def clicked2():
    uname=l_txt.get()    
    upas=l_txt1.get()
    msg1,infom,tb = bk.user_login(uname,upas)
    #messagebox.showinfo('Title',msg1) 
    if infom is True:
        messagebox.showinfo('Info',msg1)
        new_winF(tb)
    else :
        messagebox.showerror('Info',msg1)
btn2 = Button(tab2 , text = "Log In" , command = clicked2)
btn2.grid(column=1, row=3)        
#tab_control.pack(expand=1, fill='both')
tab_control.grid() 
window.mainloop()