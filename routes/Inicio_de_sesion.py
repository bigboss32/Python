from flask import Blueprint,request,render_template, redirect, url_for, flash
from models.entities.user import User
from flask_mysqldb import MySQL
db = MySQL()



sesion_blue=Blueprint('Inicio_de_sesion',__name__)



@sesion_blue.route('/Inicio_de_sesion')
def sesion():
 return render_template("partials/login-v2.html")

@sesion_blue.route('/registro', methods=['GET', 'POST'])
def regsitro():
    if request.method == 'POST':
        print("holaaaa")
        print(request.form['nom'])
        print(request.form['correo'])
        print(request.form['contra'])
        print(request.form['contrados'])
        fullname = "mi"
        phone = 12324
        email = "carlos@a"
        cursor = db.connection.cursor()
       
      
        cursor.execute('INSERT INTO usuario (Nombre, contrase, correo) VALUES (%s, %s, %s)', (fullname,phone,email))
        cursor.connection.commit()
        return redirect(url_for('login'))
    else:
        print("hola")

        return render_template("partials/register.html")

@sesion_blue.route('/recuperacion')
def recuperacion():
 return render_template("partials/recuperacion.html")