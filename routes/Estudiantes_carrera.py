from flask import Blueprint, request,render_template,redirect
from os import remove
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
from models.entities.Encuestas import encuesta
from models.entities.Descargar_csv import obj
Estudiantes_carrera_bleu = Blueprint('Estudiantes_carrera', __name__)
db = MySQL()
@Estudiantes_carrera_bleu.route('/Estudiantes_carrera',methods=['GET', 'POST'])
@login_required
def Estudiantes_carrera():
        
 carrera=request.form["carrera"]
 iduse=request.form["id"]   
                
 print(iduse)      
 datos=pandas.read_sql("SELECT * FROM registro_encuesta WHERE carrera = '{}' AND usuario = {}".format(carrera, iduse),db.connection)
   
 filas=[]
 for i in range(len(datos)):
      
            
            filas.append(obj(

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
            
 return render_template("Estudiantes_carrera.html",filas=filas,carrera=carrera)