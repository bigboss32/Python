from flask import Blueprint,render_template,request,redirect
from os import remove
import time
import pandas
from models.entities.historial import Registro
from flask_login import login_required
from flask_mysqldb import MySQL
db = MySQL()
historial_usuarios_blue=Blueprint('historial_usuarios',__name__)


@historial_usuarios_blue.route('/Historia_usuarios')
@login_required
def historial():
    exportar=[]
    Datafremenombre =pandas.read_sql("SELECT * FROM user ",db.connection)
    nombre=Datafremenombre.iloc[:, -1]
    correo=Datafremenombre.iloc[:, 1]
    id=Datafremenombre.iloc[:, 0]
    for i in range(len(nombre)):
       exportar.append(Registro(id[i],nombre.iloc[i],correo.iloc[i]))
   
    return render_template("historial_usuario.html",historial=exportar)

@historial_usuarios_blue.route('/eliminar_usuarios',methods=['GET', 'POST'])
@login_required
def eliminar_user():

    nombre=request.form['eliminar']
    print(nombre)
    cursor = db.connection.cursor()
    sql="DELETE FROM user WHERE id ="+nombre
    cursor.execute(sql)
    cursor.connection.commit()

   
    return redirect("/Historia_usuarios")
   
