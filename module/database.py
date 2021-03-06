'''
Created on Jan 10, 2017

@author: hanif, Jibril Hartri Putra
'''

import pymysql
import datetime as dt

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","","catur" )
    
    def read_pelatih(self,nama):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            if nama == None:
                cursor.execute("SELECT pelatih.no , pelatih.fide_id , pelatih.id_pelatih , pelatih.nama_pelatih , pelatih.jenis_kelamin , pelatih.tempat_lahir , pelatih.tanggal_lahir , pelatih.alamat , pelatih.klasifikasi , pelatih.kode_pos , pelatih.email , pelatih.rating_fide , pelatih.rating_national , provinsi.nm_provinsi , pelatih.data_prestasi , pelatih.foto , pelatih.status , pelatih.tanggal, gelar_pelatih.pnp, gelar_pelatih.pnm,gelar_pelatih.pn,gelar_pelatih.ins,gelar_pelatih.fst,gelar_pelatih.ft,gelar_pelatih.fi,gelar_pelatih.ni,gelar_pelatih.di FROM (( pelatih INNER JOIN gelar_pelatih ON pelatih.id_pelatih = gelar_pelatih.id_pelatih) INNER JOIN provinsi ON pelatih.pemprov = provinsi.kd_provinsi) order by pelatih.nama_pelatih asc ")
            else:
                cursor.execute("SELECT pelatih.no , pelatih.fide_id , pelatih.id_pelatih , pelatih.nama_pelatih , pelatih.jenis_kelamin , pelatih.tempat_lahir , pelatih.tanggal_lahir , pelatih.alamat , pelatih.klasifikasi , pelatih.kode_pos , pelatih.email , pelatih.rating_fide , pelatih.rating_national , provinsi.nm_provinsi , pelatih.data_prestasi , pelatih.foto , pelatih.status , pelatih.tanggal, gelar_pelatih.pnp, gelar_pelatih.pnm,gelar_pelatih.pn,gelar_pelatih.ins,gelar_pelatih.fst,gelar_pelatih.ft,gelar_pelatih.fi,gelar_pelatih.ni,gelar_pelatih.di FROM (( pelatih INNER JOIN gelar_pelatih ON pelatih.id_pelatih = gelar_pelatih.id_pelatih) INNER JOIN provinsi ON pelatih.pemprov = provinsi.kd_provinsi) where pelatih.no = %s order by pelatih.nama_pelatih asc ",(nama))
            return cursor.fetchall()
        except:
            return []
        finally:
            con.close()
        
    def read_wasit(self,nama):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            if nama == None:
                cursor.execute("SELECT wasit.no , wasit.fide_id , wasit.id_wasit , wasit.nama_wasit , wasit.jenis_kelamin , wasit.tempat_lahir , wasit.tanggal_lahir , wasit.alamat , wasit.klasifikasi , wasit.kode_pos , wasit.email , wasit.rating_fide , wasit.rating_national , provinsi.nm_provinsi , wasit.data_prestasi , wasit.foto , wasit.status , wasit.tanggal, gelar_wasit.wnp, gelar_wasit.wnm,gelar_wasit.wn,gelar_wasit.fa,gelar_wasit.ia,gelar_wasit.io FROM (( wasit INNER JOIN gelar_wasit ON wasit.id_wasit = gelar_wasit.id_wasit) INNER JOIN provinsi ON wasit.pemprov = provinsi.kd_provinsi) order by wasit.nama_wasit asc ")
            else:
                cursor.execute("SELECT wasit.no , wasit.fide_id , wasit.id_wasit , wasit.nama_wasit , wasit.jenis_kelamin , wasit.tempat_lahir , wasit.tanggal_lahir , wasit.alamat , wasit.klasifikasi , wasit.kode_pos , wasit.email , wasit.rating_fide , wasit.rating_national , provinsi.nm_provinsi , wasit.data_prestasi , wasit.foto , wasit.status , wasit.tanggal, gelar_wasit.wnp, gelar_wasit.wnm,gelar_wasit.wn,gelar_wasit.fa,gelar_wasit.ia,gelar_wasit.io FROM (( wasit INNER JOIN gelar_wasit ON wasit.id_wasit = gelar_wasit.id_wasit) INNER JOIN provinsi ON wasit.pemprov = provinsi.kd_provinsi) where wasit.no = %s order by wasit.nama_wasit asc ",(nama))
            return cursor.fetchall()
        except:
            return []
        finally:
            con.close()

    def read_pemain(self, nama):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if nama == None:
                cursor.execute("SELECT pemain.no , pemain.fide_id , pemain.id_pemain , pemain.nama_pemain , pemain.jenis_kelamin , pemain.tempat_lahir , pemain.tanggal_lahir , pemain.alamat , pemain.telepon , pemain.kode_pos , pemain.email , pemain.rating_fide , pemain.rating_national , provinsi.nm_provinsi , pemain.data_prestasi , pemain.foto , pemain.status , pemain.tanggal, gelar_pemain.gm, gelar_pemain.im,gelar_pemain.fm,gelar_pemain.cm,gelar_pemain.wgm,gelar_pemain.wim,gelar_pemain.wfm,gelar_pemain.wcm,gelar_pemain.wcm,gelar_pemain.mn,gelar_pemain.mp,gelar_pemain.mnw,gelar_pemain.mpw  FROM  (( pemain INNER JOIN gelar_pemain ON pemain.id_pemain = gelar_pemain.id_pemain) INNER JOIN provinsi ON pemain.pemprov = provinsi.kd_provinsi) order by pemain.nama_pemain asc")
            else: 
                cursor.execute("SELECT pemain.no , pemain.fide_id , pemain.id_pemain , pemain.nama_pemain , pemain.jenis_kelamin , pemain.tempat_lahir , pemain.tanggal_lahir , pemain.alamat , pemain.telepon , pemain.kode_pos , pemain.email , pemain.rating_fide , pemain.rating_national , provinsi.nm_provinsi , pemain.data_prestasi , pemain.foto , pemain.status , pemain.tanggal, gelar_pemain.gm, gelar_pemain.im,gelar_pemain.fm,gelar_pemain.cm,gelar_pemain.wgm,gelar_pemain.wim,gelar_pemain.wfm,gelar_pemain.wcm,gelar_pemain.wcm,gelar_pemain.mn,gelar_pemain.mp,gelar_pemain.mnw,gelar_pemain.mpw  FROM  (( pemain INNER JOIN gelar_pemain ON pemain.id_pemain = gelar_pemain.id_pemain) INNER JOIN provinsi ON pemain.pemprov = provinsi.kd_provinsi) where pemain.no = %s order by nama_pemain asc", (nama,))

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

    def up_pelatih(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT no FROM pelatih order by no desc")
            return cursor.fetchall()
        except:
            return []
        finally:
            cursor.close()

    def up_wasit(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT no FROM wasit order by no desc")
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

    def addpelatih(self,data,gambar,id_pelatih,gelar):
        con = Database.connect(self)
        cursor = con.cursor()
        
        
        try:
            cursor.execute("INSERT INTO pelatih (fide_id, id_pelatih, nama_pelatih, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, telepon, kode_pos, email, rating_fide, rating_national, klasifikasi, pemprov, data_prestasi, foto, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(data['id_fide'],id_pelatih,data['nama_pelatih'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['klasifikasi'],data['pemprov'],data['data_prestasi'],gambar,'Aktif'))
            cursor.execute("INSERT INTO gelar_pelatih (id_pelatih, pnp, pnm, pn, ins, fst, ft, fi, ni, di) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_pelatih,gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9]))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def addwasit(self,data,gambar,id_wasit,gelar):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO wasit (fide_id, id_wasit, nama_wasit, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat, telepon, kode_pos, email, rating_fide, rating_national, klasifikasi, pemprov, data_prestasi, foto, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(data['id_fide'],id_wasit,data['nama_wasit'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['klasifikasi'],data['pemprov'],data['data_prestasi'],gambar,'Aktif'))
            cursor.execute("INSERT INTO gelar_wasit (id_wasit, wnp, wnm, wn, fa, ia, io) VALUES (%s,%s,%s,%s,%s,%s,%s)",(id_wasit,gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6]))    
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
        
    def delete_wasit(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM  wasit  WHERE  wasit . no  = %s",(id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
    
    def delete_pelatih(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM  pelatih  WHERE  pelatih . no  = %s",(id))
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
    
    def update_pelatih(self,id,data,gambar,gelar,provinsi):
        con = Database.connect(self)
        cursor = con.cursor()

        id_pemain = data['id_pemain']
        now = dt.datetime.now()
        

        try:
            
            #tambah ke tabel mutasi pemain , insert on update aja..
            if gambar != 'ndak_ada':
                cursor.execute("UPDATE  pelatih  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s,klasifikasi=%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],data['klasifikasi'],id))
                cursor.execute("UPDATE gelar_pelatih SET pnp=%s,pnm=%s,pn=%s,ins=%s,fst=%s,ft=%s,fi=%s,ni=%s,di=%s WHERE gelar_pelatih.id_pelatih = %s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],id_pemain))
                cursor.execute("INSERT INTO mutasi_pelatih(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
            else:
                cursor.execute("UPDATE  pelatih  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s.klasifikasi=%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],data['klasifikasi'],id))
                cursor.execute("UPDATE gelar_pelatih SET pnp=%s,pnm=%s,pn=%s,ins=%s,fst=%s,ft=%s,fi=%s,ni=%s,di=%s WHERE gelar_pelatih.id_pelatih = %s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],id_pemain))
                cursor.execute("INSERT INTO mutasi_pelatih(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
                

            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update_wasit(self,id,data,gambar,gelar,provinsi):
        con = Database.connect(self)
        cursor = con.cursor()

        id_pemain = data['id_pemain']
        now = dt.datetime.now()
        

        try:
            
            #tambah ke tabel mutasi pemain , insert on update aja..
            if gambar != 'ndak_ada':
                cursor.execute("UPDATE  wasit  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s,klasifikasi=%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],data['klasifikasi'],id))
                cursor.execute("UPDATE gelar_wasit SET wnp=%s,wnm=%s,wn=%s,fa=%s,ia=%s,io=%s WHERE gelar_wasit.id_wasit =%s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],id_pemain))
                cursor.execute("INSERT INTO mutasi_wasit(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
            else:
                cursor.execute("UPDATE  pemain  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s,klasifikasi=%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],data['klasifikasi'],id))
                cursor.execute("UPDATE gelar_wasit SET wnp=%s,wnm=%s,wn=%s,fa=%s,ia=%s,io=%s WHERE gelar_wasit.id_wasit =%s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],id_pemain))
                cursor.execute("INSERT INTO mutasi_wasit(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
                

            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update_pemain(self,id,data,gambar,gelar,provinsi):
        con = Database.connect(self)
        cursor = con.cursor()

        id_pemain = data['id_pemain']
        now = dt.datetime.now()
        

        try:
            
            #tambah ke tabel mutasi pemain , insert on update aja..
            if gambar != 'ndak_ada':
                cursor.execute("UPDATE  pemain  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],id))
                cursor.execute("UPDATE gelar_pemain SET gm=%s,im=%s,fm=%s,cm=%s,wgm=%s,wim=%s,wfm=%s,wcm=%s,mn=%s,mp=%s,mnw=%s,mpw=%s WHERE gelar_pemain.id_pemain = %s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],id_pemain))
                cursor.execute("INSERT INTO mutasi_pemain(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
            else:
                cursor.execute("UPDATE  pemain  SET  fide_id =%s, nama_pemain =%s, jenis_kelamin =%s, tempat_lahir =%s, tanggal_lahir =%s, alamat =%s, telepon =%s, kode_pos =%s, email =%s, rating_fide =%s, rating_national =%s, pemprov =%s, data_prestasi =%s, foto =%s, status =%s WHERE no = %s ",(data['id_fide'],data['nama_pemain'],data['jenis_kelamin'],data['tempat_lahir'],data['tanggal_lahir'],data['alamat'],data['telepon'],data['kode_pos'],data['email'],data['rating_fide'],data['rating_national'],data['pemprov'],data['data_prestasi'],gambar,data['status'],id))
                cursor.execute("UPDATE gelar_pemain SET gm=%s,im=%s,fm=%s,cm=%s,wgm=%s,wim=%s,wfm=%s,wcm=%s,mn=%s,mp=%s,mnw=%s,mpw=%s WHERE gelar_pemain.id_pemain = %s",(gelar[0],gelar[1],gelar[2],gelar[3],gelar[4],gelar[5],gelar[6],gelar[7],gelar[8],gelar[9],gelar[10],gelar[11],id_pemain))
                cursor.execute("INSERT INTO mutasi_pemain(id_pemain, nama, awal, akhir, tanggal) VALUES (%s,%s,%s,%s,%s)",(id_pemain,data['nama_pemain'],data['pemprov_awal'],provinsi,now))
                

            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete_pemain(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM  pemain  WHERE  pemain . no  = %s",(id))
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

    def mutasi_pemain(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM mutasi_pemain")
            return cursor.fetchall()
        except:
            return []
        finally:
            con.close()

    def mutasi_pelatih(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM mutasi_pelatih")
            return cursor.fetchall()
        except:
            return []
        finally:
            con.close()

    def mutasi_wasit(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM mutasi_wasit")
            return cursor.fetchall()
        except:
            return []
        finally:
            con.close()

