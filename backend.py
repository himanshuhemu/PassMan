
from Crypto.Cipher import XOR
import base64
import sqlite3
import string
from random import *

def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  ans= cipher.decrypt(base64.b64decode(ciphertext)).decode("utf-8")
  return ans    


def open_db(tb_name):
    db_con = sqlite3.connect(tb_name , timeout=10)
    db_cursor = db_con.cursor() 
    return db_con,db_cursor

###############################################################################
def genStr():
    stri = "".join(choice(string.ascii_letters) for x in range(randint(4, 6)))
    return stri
    
s=genStr()    
    
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
                    #print(user_name)
                    pas = curs.execute('SELECT password FROM login_det WHERE uname = ?', (user_name,)).fetchone()
                    #print(password)
                    password=hash(password)
                    tbname=curs.execute('SELECT tbname FROM login_det WHERE  uname=?',(user_name,)).fetchone()
                    #print(tbname[0])
                    if int(password) == int(pas[0]):
                        #print("welcome user"+ user_name)
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
        return msg,info,tbname        
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
    msg= ' ' 
    e_passwd=encrypt(tb_name,passwd)
    try:
        conn, curs =open_db("data.db")
        curs.execute(' CREATE TABLE IF NOT EXISTS '+tb_name+'(ID TEXT NOT NULL ,PASSWD TEXT NOT NULL)')
        curs.execute('INSERT INTO '+tb_name+'(ID,PASSWD) VALUES(?,?)',(Id,e_passwd))
        msg="Record Saved"
        conn.commit()
        conn.close()
    except IOError:
        msg="Error"
    return msg
    
def search(srch_id,tb_name):
    mseg= ' ' 
    try:
        conn,curs=open_db("data.db")
        pas=curs.execute('select PASSWD from '+tb_name+' Where ID = ?',(srch_id,)).fetchone()
        mseg="Search Success"
        conn.close()
    except IOError:
        mseg='Error'
    return pas,mseg
    
def entry_del(Id,tb_name):
         msg='Id not exists'
         try:   
            conn, curs=open_db("data.db")
            p=curs.execute('DELETE from '+tb_name+' WHERE ID = ?',(Id,)).fetchall()
            msg='Deleted'
            conn.commit()
            conn.close()
         except IOError:
             msg="Error"
         return msg    
