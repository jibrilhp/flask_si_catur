'''
Created on Jan 10, 2017

@author: hanif, Jibril Hartri Putra
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","","catur" )
    
    def read_pemain(self, nama):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if nama == None:
                cursor.execute("SELECT * FROM pemain order by nama_pemain asc")
            else: 
                cursor.execute("SELECT * FROM pemain where id = %s order by nama_pemain asc", (nama,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    
    def up_pemain(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT no FROM pemain order by no desc")
            return cursor.fetchall()
        except:
            return []
        finally:
            cursor.close()

    def read(self,provinsi):
        con = Database.connect(self)
        #baca provinsi
        cursor = con.cursor()

        try:
            if provinsi == None:
                cursor.execute("SELECT * FROM provinsi")
            else:
                cursor.execute("SELECT * FROM provinsi WHERE kd_provinsi = %s",(provinsi))
            
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def addpemain(self,data,lihat,id_pemain,gelar):
        con = Database.connect(self)
        cursor = con.cursor()
        print(("INSERT INTO gelar_pemain (id_pemain, gm, im, fm, cm, wgm, wim, wfm, wcm, mn, mp, mnw, mpw) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_pemain,gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],gelar[12])))
        try:
            cursor.execute("INSERT INTO pemain (fide_id, id_pemain, nama_pemain, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, telepon, kode_pos, email, rating_fide, rating_national, pemprov, data_prestasi, foto, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(data['id_fide'],id_pemain,data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],lihat,'Aktif'))
            cursor.execute("INSERT INTO gelar_pemain (id_pemain, gm, im, fm, cm, wgm, wim, wfm, wcm, mn, mp, mnw, mpw) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_pemain,gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],gelar[12]))
            con.commit()
            
            

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

        
    def addgelar_pemain(self,gelar):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            sql = "INSERT INTO gelar_pemain(id_pemain, gm, im, fm, cm, wgm, wim, wfm, wcm, mn, mp, mnw, mpw) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],gelar[12],gelar[13])
            print(sql)
            cursor.execute("INSERT INTO gelar_pemain(id_pemain, gm, im, fm, cm, wgm, wim, wfm, wcm, mn, mp, mnw, mpw) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],gelar[12],gelar[13]))
            con.commit()
            return True
        except:
            con.rollback()
            return False
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
            

            cursor.execute("INSERT INTO pengguna( username, password, sebagai) VALUES (%s,%s,%s)", (username,pwd,sebagai))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()