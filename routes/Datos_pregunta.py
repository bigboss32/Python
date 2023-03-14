from flask import Blueprint, request,render_template,redirect
from os import remove
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
from models.entities.Encuestas import encuesta
Datos_pregunta_bleu = Blueprint('Datos_pregunta', __name__)
db = MySQL()

@Datos_pregunta_bleu.route('/Datos_pregunta',methods=['GET', 'POST'])
@login_required
def datos_pregunta():
   
    Data=pandas.read_sql("select cedula,numero_entrega,nombre from registro WHERE idRegistro='{}'""".format(request.form['ver']),db.connection)
    cedula=Data.loc[0, 'cedula']
    entrega=Data.loc[0, 'numero_entrega']
    nombre=Data.loc[0, 'nombre']
    Preguntas=pandas.read_sql("SELECT * FROM  registro_encuesta JOIN registro  USING(cedula,numero_entrega,nombre) where cedula='{}'""".format(cedula)+"and numero_entrega='{}'""".format(entrega) + "and nombre='{}'""".format(nombre),db.connection)
    en=[]



    prueba2=Preguntas.iloc[:, 1:16]
    respuestas=prueba2.iloc[0]
    
    Preguntas=Preguntas.iloc[:, 1:16]
 
    print(Preguntas.loc[0])
    Preguntas.loc[0].to_csv("Metodos\example.csv")

    final=pandas.read_csv("Metodos\example.csv",header=[0])
    
    print(final)
    print()
    print()
    
    pregun=[]
    id=0
    for i in range(len(final)):
         id=id+1
         pregun.append(encuesta(id,final.loc[i,'Unnamed: 0'],final.loc[i,'0']))
    return render_template("data.html",data=Data.loc[0,'nombre'],a=pregun,cedula=cedula)