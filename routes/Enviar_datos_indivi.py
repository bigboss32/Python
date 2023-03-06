from flask import Blueprint, request,render_template,redirect
from os import remove
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
Enviar_datos_indi_bleu = Blueprint('Enviar_datos_indivi', __name__)
db = MySQL()

@Enviar_datos_indi_bleu.route('/individual',methods=['GET', 'POST'])

@login_required
def informe_indiv():
    print(request.form['analizar'])
    nombre=request.form['analizar']
  
    Persona=[]
    Carrera=[]
    cantidad=pandas.read_sql("select count(*) from registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    Datafreresultado =pandas.read_sql("SELECT  FKresultado FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    abandono=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 0 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    graduado=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 1 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradatoorginal=pandas.read_sql("select Carrera FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradato=carreradatoorginal.drop_duplicates()
    
    cuenta_carrera = carreradatoorginal['Carrera'].value_counts()
    print(cuenta_carrera[0])
    for i in range(len(carreradato)):
     Carrera.append(carrera(i+1,carreradato.loc[i,'Carrera'],cuenta_carrera[i]))
   
   
     
    
    estudiantes_nuevos=pandas.read_sql("select count(*) FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    Datafremenombre =pandas.read_sql("SELECT nombre FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)

    datos_estudiantes_nuevos=estudiantes_nuevos.loc[0, 'count(*)']
    datos_cantidad=cantidad.loc[0, 'count(*)']
    Datafreresultadodos =pandas.read_sql("SELECT  Carrera FROM registro",db.connection)
    datos_abandono=abandono.loc[0,'count(*)']
    indice_abandono=(100*datos_abandono)/datos_cantidad
    datos_graduado=graduado.loc[0,'count(*)']

    numero=0
    
    for i in range(len(Datafremenombre)):
       numero=numero+1
       if Datafreresultado.loc[i,'FKresultado']==0:
            Persona.append(persona(numero,Datafremenombre.loc[i,'nombre'],Datafreresultado.loc[i,'FKresultado'],"Abandono",Datafreresultadodos.loc[i,'Carrera']))
            
                
       else:
            Persona.append(persona(numero,Datafremenombre.loc[i,'nombre'],Datafreresultado.loc[i,'FKresultado'],"Graduado",Datafreresultadodos.loc[i,'Carrera']))
     
    nuevos=datos_estudiantes_nuevos
      

    jsonabandono = json.dumps({'salary': int(datos_abandono)})
    jsongraduado = json.dumps({'salary': int(datos_graduado)})
    return render_template("index3.html",data=Persona,catidad_estu=datos_cantidad,abandonos=datos_abandono,abandono_in=indice_abandono,nuevos=nuevos,a=jsonabandono,g=jsongraduado,informe=nombre,datoscarrea=Carrera)
    

@Enviar_datos_indi_bleu.route('/Eliminar',methods=['GET', 'POST'])
@login_required
def Eliminar():

    nombre=request.form['eliminar']
    file="Archivo/"+nombre
    cursor = db.connection.cursor()
    sql=" DELETE FROM registro WHERE Numero_entrega ="+nombre[0]
    cursor.execute(sql)
    cursor.connection.commit()
    remove(file)
    return redirect("/Historia_cvs")