from flask import Blueprint,request,render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL
resgitro_blue=Blueprint('Registrase',__name__)

db = MySQL()

@resgitro_blue.route('/registro', methods=['GET', 'POST'])
def regsitro():
    if request.method == 'POST':
        print("holaaaa")
        print(request.form['nom'])
        print(request.form['correo'])
        print(request.form['contra'])
        print(request.form['contrados'])
        if request.form['contra']==request.form['contrados']:
            
            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s)', (request.form['nom'],generate_password_hash(request.form['contra']),request.form['correo']))
            cursor.connection.commit()
            return render_template('inicio.html')
        else:
             print("hola2")
             return render_template("partials/register.html")

    else:
        print("hola")
        return render_template("partials/register.html")