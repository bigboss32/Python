from flask import Blueprint, request,redirect,render_template
import os
from werkzeug.utils import secure_filename
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import joblib
import numpy as np
from models.entities.Descargar_csv import csv
csv_descargar_blue = Blueprint('csv_descargar', __name__)
db = MySQL()

@csv_descargar_blue.route('/csv_descargar', methods=['POST'])
    
@login_required
def csv_descargar():
    print(request.form['csv'])

    datos=pandas.read_sql("select * from registro_encuesta",db.connection)
    print(datos.loc[0,'Carrera'])
    print(datos.loc[0,'edad_de_ingreso'])
    print(datos.loc[0,'Actualmente_trabaja'])
    print(datos.loc[0,'Tipo_de_población_a_la_que_pertenece'])
    print(datos.loc[0,'ESTADO_CIVIL'])
    print(datos.loc[0,'Cómo_financia_sus_estudios'])
    print(datos.loc[0,'CIRCUNSCRIPCION'])
    print(datos.loc[0,'Dispone_de_un_computador_permanentemente'])
    print(datos.loc[0,'Posee_conexión_permanente_a_internet'])
    print(datos.loc[0,'sexo'])
    print(datos.loc[0,'estrato'])
    filas=[]
    for i in range(len(datos)):
      
            
            filas.append(csv(

                        datos.loc[i,'Carrera'],
                        datos.loc[i,'edad_de_ingreso'],
                        datos.loc[i,'Actualmente_trabaja'],
                        datos.loc[i,'Tipo_de_población_a_la_que_pertenece'],
                        datos.loc[i,'ESTADO_CIVIL'],
                        datos.loc[i,'Cómo_financia_sus_estudios'],
                        datos.loc[i,'CIRCUNSCRIPCION'],
                        datos.loc[i,'Dispone_de_un_computador_permanentemente'],
                        datos.loc[i,'Posee_conexión_permanente_a_internet'],
                        datos.loc[i,'sexo'],
                        datos.loc[i,'estrato']





            ))
            
    return render_template("csv_descargar.html",filas=filas)