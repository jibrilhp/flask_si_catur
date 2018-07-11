'''
Created on Jan 10, 2017

@author: hanif, Jibril Hartri Putra
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","","catur" )
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else: 
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
            
    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
            
    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
        
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()

    def check_login(self, cakupan):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            username = cakupan[0]
            pwd = cakupan[1]
            cursor.execute("SELECT * FROM pengguna WHERE username = %s and password = %s  limit 1", (username,pwd) )
            return cursor.fetchall()

        except:
            return []
        finally:
            con.close()
    
    def daftar(self, isi):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            username = isi[0]
            pwd = isi[1]
            sebagai = isi[2]
            
            if (sebagai == "admin" ):
                sebagai = 0
            if (sebagai == "pemain"):
                sebagai = 1
            if (sebagai == "pelatih"):
                sebagai = 2
            if (sebagai == "wasit"):
                sebagai = 3
            

            cursor.execute("INSERT INTO `pengguna`( `username`, `password`, `sebagai`) VALUES (%s,%s,%s)", (username,pwd,sebagai))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()