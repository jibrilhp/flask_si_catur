'''
Created on Jan 10, 2017

@author: hanif, Jibril Hartri
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database
import flask

app = Flask(__name__)
app.secret_key = "sabebdeh"
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/utama')
def utama():
    if session['login_success'] != True:
        return redirect(url_for('login'))  #apakah udah login? kalau belum silahkan login dulu
        
    data = db.read(None)

    if session['sebagai'] == 0:
        return render_template('utama.html', data = data) #utama, sebagai admin bisa edit dan ngatur semua

    if session['sebagai'] == 1:
        return render_template('utama_pemain.html',data = data)
    
    if session['sebagai'] == 2:
        return render_template('utama_pelatih.html',data = data)
    
    if session['sebagai'] == 3:
        return render_template('utama_wasit.html',data = data)
    
    
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
    

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")
            
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
        
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')
           
        else:
            flash('A phone number can not be updated')
        
        session.pop('update', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:
        
        if db.delete(session['delete']):
            flash('A phone number has been deleted')
           
        else:
            flash('A phone number can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    print(" * Menjalankan program Sistem Informasi Catur")
    app.run(debug = True, port=8181, host="0.0.0.0")