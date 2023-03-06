from flask import Blueprint,request,render_template, redirect, url_for, flash
from flask_login import  login_user, logout_user, login_required
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
from models.entities.User import User

db = MySQL()



sesion_blue=Blueprint('Inicio_de_sesion',__name__)






@sesion_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect("/datos")
            else:
                flash("Invalid password...")
                return render_template('inicio.html',message=flash)
        else:
            usario="usuario no encontrado"
            return render_template('inicio.html')
    else:
        return render_template('inicio.html')


@sesion_blue.route('/logout')
def logout():
    logout_user()
    return render_template('inicio.html')



@sesion_blue.route('/home')
def home():
    return render_template('index3.html')


@sesion_blue.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"




















@sesion_blue.route('/recuperacion')
def recuperacion():
 return render_template("partials/recuperacion.html")