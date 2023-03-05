from flask import Blueprint,request,render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
import pandas
from models.entities.Persona import persona
datos_blue=Blueprint('Datos',__name__)
db = MySQL()


@datos_blue.route('/datos', methods=['GET', 'POST'])
def datos():
      Persona=[]
      cursor = db.connection.cursor()
      Datafremenombre =pandas.read_sql("SELECT  nombre FROM registro",db.connection)
      cantidad=pandas.read_sql("select count(*) from registro",db.connection)
      Datafreresultado =pandas.read_sql("SELECT  FKresultado FROM registro",db.connection)
      abandono=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 0",db.connection)
      ultima_entreg=pandas.read_sql("select MAX(numero_entrega) from registro ",db.connection)
      
      dato_ultima_entrega=ultima_entreg.loc[0,'MAX(numero_entrega)']
      print(dato_ultima_entrega)
      estudiantes_nuevos=pandas.read_sql("select count(*) FROM registro WHERE numero_entrega='{}'""".format(dato_ultima_entrega),db.connection)
      print(estudiantes_nuevos)
      datos_estudiantes_nuevos=estudiantes_nuevos.loc[0, 'count(*)']
      datos_cantidad=cantidad.loc[0, 'count(*)']
      datos_abandono=abandono.loc[0,'count(*)']
      indice_abandono=(datos_cantidad/datos_abandono)/100
      numero=0
      for i in range(len(Datafremenombre)):
       numero=numero+1
       Persona.append(persona(numero,Datafremenombre.loc[i,'nombre'],Datafreresultado.loc[i,'FKresultado']))

     
    
      return render_template("index3.html",data=Persona,catidad_estu=datos_cantidad,abandonos=datos_abandono,abandono_in=indice_abandono,nuevos=datos_estudiantes_nuevos)