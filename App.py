

import flask
from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL

from routes.Subir import Subir_blue
from routes.Predicion import Predicion_blue
from routes.Crud import Crud_blue
from routes.Historia_cvs import historial_blue
from routes.Cargar import Cargar_cvs_blue
from routes.Inicio_de_sesion import sesion_blue
#
from models.ModelUser import ModelUser
#
from models.entities.user import User


# creating instance of the class
app = Flask(__name__)
db = MySQL(app)
@app.route('/')
def prueba():
       
        fullname = "carlos"
        phone = 12324
        email = "carlos@a"
        cursor = db.connection.cursor()
       
      
        cursor.execute('INSERT INTO usuario (Nombre, contrase, correo) VALUES (%s, %s, %s)', (fullname,phone,email))
        cursor.connection.commit()
        return ""




@app.route('/aa', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
     u = User(0, request.form['correo'], request.form['contra'])
     print(u.Nombre)
     logged_user = ModelUser.login(db, u)
     
     print(logged_user)
     if logged_user != None:
        if logged_user.contrase==True:
            return render_template("index3.html")
        else:
            flash("Invalid password...")
            return render_template('partials/login-v2.html')
     else:
        flash("User not found...")
        return render_template('partials/login-v2.html')
    else:
        return render_template('partials/login-v2.html')


app.register_blueprint(Subir_blue)
app.register_blueprint(Predicion_blue)
app.register_blueprint(Crud_blue)
app.register_blueprint(historial_blue)
app.register_blueprint(Cargar_cvs_blue)
app.register_blueprint(sesion_blue)







