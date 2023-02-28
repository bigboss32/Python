from flask import Blueprint,request,render_template, redirect, url_for, flash
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
db = MySQL()



sesion_blue=Blueprint('Inicio_de_sesion',__name__)

from flask_mysqldb import MySQL

from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User





@sesion_blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return render_template("index3.html")
            else:
                flash("Invalid password...")
                return render_template('inicio.html')
        else:
            flash("User not found...")
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