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
    cvs=request.form['csv']
    print(cvs[0])

    datos=pandas.read_sql("SELECT * FROM registro_encuesta",db.connection)
   
    filas=[]
    for i in range(len(datos)):
      
            
            filas.append(csv(

                        datos.loc[i,'Carrera'],
                        datos.loc[i,'nombre'],
                        datos.loc[i,'cedula'],
                        datos.loc[i,'edad_de_ingreso'],
                        datos.loc[i,'Actualmente_trabaja'],
                        datos.loc[i,'Tipo_de_población_a_la_que_pertenece'],
                        datos.loc[i,'ESTADO_CIVIL'],
                        datos.loc[i,'Cómo_financia_sus_estudios'],
                        datos.loc[i,'CIRCUNSCRIPCION'],
                        datos.loc[i,'Dispone_de_un_computador_permanentemente'],
                        datos.loc[i,'Posee_conexión_permanente_a_internet'],
                        datos.loc[i,'sexo'],
                        datos.loc[i,'estrato'],
                        datos.loc[i,'FKresultado']





            ))
            
    return render_template("csv_descargar.html",filas=filas)