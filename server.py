'''
Created on Jan 10, 2017

@author: hanif, Jibril Hartri
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session,send_from_directory
from werkzeug.utils import secure_filename
from module.database import Database
import flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'user_photos/'
app.secret_key = "sabebdeh"
db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/utama')
def utama():
    try:
        if session['login_success'] != True:
            return redirect(url_for('login'))  #apakah udah login? kalau belum silahkan login dulu
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  

    data = db.read_pemain(None)
    data_pelatih = db.read_pelatih(None)
    data_wasit = db.read_wasit(None)
    
    if session['sebagai'] == 0:
        
        return render_template('utama.html', data = data,data_pelatih = data_pelatih, data_wasit = data_wasit ) #utama, sebagai admin bisa edit dan ngatur semua

    if session['sebagai'] == 1:
        return render_template('utama_pemain.html',data = data)
    
    if session['sebagai'] == 2:
        return render_template('utama_pelatih.html',data = data_pelatih)
    
    if session['sebagai'] == 3:
        return render_template('utama_wasit.html',data = data_wasit)
    
    
    return render_template('utama.html', data = data)

@app.route('/login',methods = ['GET','POST'])
def login():
    if flask.request.method == "POST":
        #ini bagian tentang loginnya
        username = flask.request.values.get('username')
        password = flask.request.values.get('password')
        
        
        cakupan = []

        cakupan.append(username)
        cakupan.append(password)
 
        data = db.check_login(cakupan)
      
        for baris in data:
            if baris[1] == username and baris[2] == password:
                
                session['login_success'] = True
                session['username'] = baris[1]
                session['sebagai'] = baris[3]
                session['approve'] = baris[4] # jika dia admin
                
                return redirect(url_for('utama'))
            else:
                flash("Maaf username atau password anda salah")
                return redirect(url_for('login'))
        if data == []:
            flash("Maaf username atau password anda salah")
            return redirect(url_for('login'))
        else:
            flash("Maaf username atau password anda salah")
            return redirect(url_for('login'))
    else:
        try:
            if session['login_success'] == True:
                return redirect(url_for('utama')) 
        except:
            return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    if flask.request.method == 'POST':
        username = flask.request.values.get('username')
        password = flask.request.values.get('password')
        re_password = flask.request.values.get('password2')
        sebagai = flask.request.values.get('sebagai')

        if password == re_password:
            #password yang diisi telah benar
            #langsung kuy daftar
            isi = [username,password,sebagai]
            
            data = db.daftar(isi)
            if (data == True):
                flash("Pendaftaran berhasil, silahkan login")
                return redirect(url_for('login'))
            else:
                flash("Kesalahan terjadi")
                return redirect(url_for('register'))
        else:
            flash("Silahkan periksa isian password anda")
            return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/add_pemain/')
def add_pemain():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  
    
    provinsi = db.read(None)

    return render_template('add_pemain.html',provinsi=provinsi)

@app.route('/add_wasit/')
def add_wasit():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  
    
    provinsi = db.read(None)
    return render_template('add_wasit.html',provinsi = provinsi)

@app.route('/add_pelatih')
def add_pelatih():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  

    provinsi = db.read(None)
    return render_template('add_pelatih.html',provinsi = provinsi)

@app.route('/add_wasit_save',methods= ['POST'])
def add_wasit_save():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login')) 
    
    if request.method == 'POST' and request.form['save']:
        f = request.files['photo']
        f.save('user_photos/' + secure_filename(f.filename))
        lihat = f.filename

        #Baca gelar2nya

        if request.form.get('WNP',None) == 'WNP':
            WNP = 1
        else:
            WNP = 0
        
        if request.form.get('WNM',None) == 'WNM':
            WNM = 1
        else:
            WNM = 0
        
        if request.form.get('WN',None) == 'WN':
            WN = 1
        else:
            WN = 0
        
        if request.form.get('FA',None) == 'FA':
            FA = 1
        else:
            FA = 0
        
        if request.form.get('IA',None) == 'IA':
            IA = 1
        else:
            IA = 0
        
        if request.form.get('IO',None) == 'IO':
            IO = 1
        else:
            IO = 0
        
        isi =''
        terkini = db.up_wasit()
        if terkini != []:
            for xyr in terkini:
                isi = xyr[0]
            sekarang = "{0:0>3}".format(isi)
        else:
            sekarang = "001"

        tgl = request.form.get('tanggal_lahir')
        id_wasit = request.form.get('pemprov') + "/" + tgl[2:4] + sekarang       
        gelar = [id_wasit,WNP,WNM,WN,FA,IA,IO]
        
        
        if db.addwasit(request.form,lihat,id_wasit,gelar):   
            flash("Wasit berhasil ditambahkan")
        else:
            flash("Kesalahan terjadi")
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))

        
        




@app.route('/add_pelatih_save',methods = ['POST'])
def add_pelatih_save():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  
    
    if request.method == 'POST' and request.form['save']:
        f = request.files['photo']
        f.save('user_photos/' + secure_filename(f.filename))
        lihat = f.filename

        #Baca gelar2nya

        if request.form.get('PNP',None) == "PNP":
            PNP = 1
        else:
            PNP = 0

        if request.form.get('PNM',None) == "PNM":
            PNM = 1
        else:
            PNM = 0

        if request.form.get('PN',None) == "PN":
            PN = 1
        else:
            PN = 0

        if request.form.get('INS',None) == "INS":
            INS = 1
        else:
            INS = 0

        if request.form.get('FST',None) == "FST":
            FST = 1
        else:
            FST = 0

        if request.form.get('FT',None) == "FT":
            FT = 1
        else:
            FT = 0

        if request.form.get('FI',None) == "FI":
            FI = 1
        else:
            FI = 0
        
        if request.form.get('NI',None) == "NI":
            NI = 1
        else:
            NI = 0

        if request.form.get('DI',None) == "DI":
            DI = 1
        else:
            DI = 0

        isi =''
        terkini = db.up_pelatih()
        if terkini != []:
            for xyr in terkini:
                isi = xyr[0]
            sekarang = "{0:0>3}".format(isi)
        else:
            sekarang = "001"

        tgl = request.form.get('tanggal_lahir')
        id_pelatih = request.form.get('pemprov') + "/" + tgl[2:4] + sekarang       
        gelar = [id_pelatih,PNP,PNM,PN,INS,FST,FT,FI,NI,DI]
        
        
        if db.addpelatih(request.form,lihat,id_pelatih,gelar):   
            flash("Pelatih berhasil ditambahkan")
        else:
            flash("Kesalahan terjadi")
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))


@app.route('/add_pemain_save', methods = ['POST', 'GET'])
def addpemain():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  

    if request.method == 'POST' and request.form['save']:
        f = request.files['photo']
        f.save('user_photos/' + secure_filename(f.filename))
        lihat = f.filename

        #Baca gelar2nya
        if request.form.get('GM',None) == "GM":
            GM = 1
        else:
            GM = 0
        
        if request.form.get('IM',None) == "GM":
            IM = 1
        else:
            IM = 0

        if request.form.get('FM',None) == "FM":
            FM = 1
        else:
            FM = 0
        
        if request.form.get('CM',None) == "CM":
            CM = 1
        else:
            CM = 0
        
        if request.form.get('WGM',None) == "WGM":
            WGM = 1
        else:
            WGM = 0
        
        if request.form.get('WIM',None) == "GM":
            WIM = 1
        else:
            WIM = 0
        
        if request.form.get('WFM',None) == "WFM":
            WFM = 1
        else:
            WFM = 0
        
        if request.form.get('WCM',None) == "WCM":
            WCM = 1
        else:
            WCM = 0
        
        if request.form.get('MN',None) == "MN":
            MN = 1
        else:
            MN = 0
        
        if request.form.get('MP',None) == "MP":
            MP = 1
        else:
            MP = 0
        
        if request.form.get('MNW',None) == "MNW":
            MNW = 1
        else:
            MNW = 0
        
        if request.form.get('MPW',None) == "MPW":
            MPW = 1
        else:
            MPW = 0

        isi =''
        terkini = db.up_pemain()
        if terkini != []:
            for xyr in terkini:
                isi = xyr[0]
            sekarang = "{0:0>3}".format(isi)
        else:
            sekarang = "001"

        tgl = request.form.get('tanggal_lahir')
        id_pemain = request.form.get('pemprov') + "/" + tgl[2:4] + sekarang       
        gelar = [id_pemain,GM,IM,FM,CM,WGM,WIM,WFM,WCM,MN,MP,MNW,MPW]
        


        if db.addpemain(request.form,lihat,id_pemain,gelar):
           
            flash("Pemain berhasil ditambahkan")
        else:
            flash("Kesalahan terjadi")
            
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))

@app.route('/view_pemain/<int:no>')
def viewpemain(no):
    data = db.read_pemain(no)

    if len(data) == 0:
        flash("Tidak ditemukan...")
        return redirect(url_for('utama'))
    else:
        return render_template('view_pemain.html' ,data = data)


@app.route('/update_pelatih/<int:id>')
def update_pelatih(id):
    provinsi = db.read(None)
    data = db.read_pelatih(id)
    
    if len(data) == 0:
        return redirect(url_for('utama'))
    else:
        session['update'] = id
        return render_template('update_pelatih.html', data = data,provinsi = provinsi)

@app.route('/update_wasit/<int:id>')
def update_wasit(id):
    provinsi = db.read(None)
    data = db.read_wasit(id)
    
    if len(data) == 0:
        return redirect(url_for('utama'))
    else:
        session['update'] = id
        return render_template('update_wasit.html', data = data,provinsi = provinsi)

@app.route('/update_pelatih_save',methods=['POST'])
def update_pelatih_save():
    if request.method == 'POST' and request.form['save']:
        f = request.files['photo']
        f.save('user_photos/' + secure_filename(f.filename))
        lihat = f.filename

        #Baca gelar2nya

        if request.form.get('WNP',None) == 'WNP':
            WNP = 1
        else:
            WNP = 0
        
        if request.form.get('WNM',None) == 'WNM':
            WNM = 1
        else:
            WNM = 0
        
        if request.form.get('WN',None) == 'WN':
            WN = 1
        else:
            WN = 0
        
        if request.form.get('FA',None) == 'FA':
            FA = 1
        else:
            FA = 0
        
        if request.form.get('IA',None) == 'IA':
            IA = 1
        else:
            IA = 0
        
        if request.form.get('IO',None) == 'IO':
            IO = 1
        else:
            IO = 0
       
        gelar = [WNP,WNM,WN,FA,IA,IO]
        
        
        if db.update_pelatih(session['update'], request.form,lihat,gelar,provinsi):
            flash("Wasit berhasil diupdate")
        else:
            flash("Kesalahan terjadi")
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))



@app.route('/update_wasit_save',methods=['POST'])
def update_wasit_save():
    if request.method == 'POST' and request.form['save']:
        f = request.files['photo']
        f.save('user_photos/' + secure_filename(f.filename))
        lihat = f.filename

        #Baca gelar2nya

        if request.form.get('WNP',None) == 'WNP':
            WNP = 1
        else:
            WNP = 0
        
        if request.form.get('WNM',None) == 'WNM':
            WNM = 1
        else:
            WNM = 0
        
        if request.form.get('WN',None) == 'WN':
            WN = 1
        else:
            WN = 0
        
        if request.form.get('FA',None) == 'FA':
            FA = 1
        else:
            FA = 0
        
        if request.form.get('IA',None) == 'IA':
            IA = 1
        else:
            IA = 0
        
        if request.form.get('IO',None) == 'IO':
            IO = 1
        else:
            IO = 0
        
       
        gelar = [WNP,WNM,WN,FA,IA,IO]
        
        
        if db.update_pelatih(session['update'], request.form,lihat,gelar,provinsi):   
            flash("Wasit berhasil diupdate")
        else:
            flash("Kesalahan terjadi")
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))

@app.route('/mutasi_pemain/')
def mutasi_pemain():
    data = db.mutasi_pemain()
    return render_template('mutasi_pemain.html', data = data)

@app.route('/mutasi_wasit/')
def mutasi_wasit():
    data = db.mutasi_wasit()
    return render_template('mutasi_wasit.html', data = data)

@app.route('/mutasi_pelatih/')
def mutasi_pelatih():
    data = db.mutasi_pelatih()
    return render_template('mutasi_pelatih.html', data = data)


@app.route('/update_pemain/<int:id>/')
def update_pemain(id):
    provinsi = db.read(None)
    data = db.read_pemain(id)
    
    if len(data) == 0:
        return redirect(url_for('utama'))
    else:
        session['update'] = id
        return render_template('update_pemain.html', data = data,provinsi = provinsi)

@app.route('/update_pemain_save', methods = ['POST'])
def updatepemain_save():
    if request.method == 'POST' and request.form['save']:
        provinsi = db.read(request.form.get('pemprov'))
        lihat = 'ndak_ada'

        try:
            f = request.files['photo']
            f.save('user_photos/' + secure_filename(f.filename))
            lihat = f.filename
        except:
            f = None
        

        #Baca gelar2nya
        if request.form.get('GM',None) == "GM":
            GM = 1
        else:
            GM = 0
        
        if request.form.get('IM',None) == "GM":
            IM = 1
        else:
            IM = 0

        if request.form.get('FM',None) == "FM":
            FM = 1
        else:
            FM = 0
        
        if request.form.get('CM',None) == "CM":
            CM = 1
        else:
            CM = 0
        
        if request.form.get('WGM',None) == "WGM":
            WGM = 1
        else:
            WGM = 0
        
        if request.form.get('WIM',None) == "GM":
            WIM = 1
        else:
            WIM = 0
        
        if request.form.get('WFM',None) == "WFM":
            WFM = 1
        else:
            WFM = 0
        
        if request.form.get('WCM',None) == "WCM":
            WCM = 1
        else:
            WCM = 0
        
        if request.form.get('MN',None) == "MN":
            MN = 1
        else:
            MN = 0
        
        if request.form.get('MP',None) == "MP":
            MP = 1
        else:
            MP = 0
        
        if request.form.get('MNW',None) == "MNW":
            MNW = 1
        else:
            MNW = 0
        
        if request.form.get('MPW',None) == "MPW":
            MPW = 1
        else:
            MPW = 0

        
        gelar = [GM,IM,FM,CM,WGM,WIM,WFM,WCM,MN,MP,MNW,MPW]
        
        if db.update_pemain(session['update'], request.form,lihat,gelar,provinsi):
            flash('Pemain telah berhasil di update')
           
        else:
            flash('Kesalahan terjadi..')
        
        session.pop('update', None)
        
        return redirect(url_for('utama'))
    else:
        return redirect(url_for('utama'))
    
@app.route('/delete_pemain/<int:id>/')
def delete_pemain(id):
    data = db.delete_pemain(id)
    
    if data:
        flash('Data telah dihapus')
        return redirect(url_for('utama'))
    else:
        flash('kesalahan terjadi')
        return redirect(url_for('utama'))

@app.route('/delete_pelatih/<int:id>/')
def delete_pelatih(id):
    data = db.delete_pelatih(id)

    if data:
        flash('Data telah dihapus')
        return redirect(url_for('utama'))
    else:
        flash('kesalahan terjadi')
        return redirect(url_for('utama'))
        
@app.route('/delete_wasit/<int:id>')
def delete_wasit(id):
    data = db.delete_wasit(id)

    if data:
        flash('data telah dihapus')
        return redirect(url_for('utama'))
    else:
        flash('kesalahan terjadi')
        return redirect(url_for('utama'))

@app.route('/logout')
def logout():
    session.pop('login_success',None)
    session.pop('username',None)
    session.pop('sebagai',None)
    session.pop('approve',None)
    return redirect(url_for('index'))

@app.route('/foto/<path:path>')
def send_userphotos(path):
    return send_from_directory('user_photos/',path)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

def cek_login():
    try:
        if session['login_success'] != True:
            flash('silahkan login terlebih dahulu!')
            return redirect(url_for('login'))  
    except:
        flash('silahkan login terlebih dahulu!')
        return redirect(url_for('login'))  


if __name__ == '__main__':
    print(" * Menjalankan program Sistem Informasi Catur")
    app.run(debug = True, port=8181, host="0.0.0.0")