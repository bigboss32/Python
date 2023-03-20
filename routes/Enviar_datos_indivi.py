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

    nombre=request.form['analizar']
  
    Persona=[]
    Carrera=[]
    cantidad=pandas.read_sql("select count(*) from registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
   
    abandono=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 0 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    graduado=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 1 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradatoorginal=pandas.read_sql("select Carrera FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradato=carreradatoorginal.drop_duplicates()

    datosgenreal=pandas.read_sql("SELECT  idRegistro,cedula,nombre,Carrera,FKresultado FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    
    

    cuenta_carrera = carreradatoorginal['Carrera'].value_counts()
               
    for i in range(len(carreradato)):
        programa=carreradato.iloc[i,0]
        cuenta=cuenta_carrera[carreradato.iloc[i,0]]
        item=i+1
        Carrera.append(carrera(item,programa,cuenta))
   
   
     
    
    estudiantes_nuevos=pandas.read_sql("select count(*) FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)


    datos_estudiantes_nuevos=estudiantes_nuevos.loc[0, 'count(*)']
    datos_cantidad=cantidad.loc[0, 'count(*)']
   
    
    datos_abandono=abandono.loc[0,'count(*)']
    indice_abandono=(100*datos_abandono)/datos_cantidad
    datos_graduado=graduado.loc[0,'count(*)']

    numero=0
    print(datosgenreal)
    print(datosgenreal.loc[1,'nombre'])
    
    for i in range(len(datosgenreal)):
      
      
       Persona.append(persona(datosgenreal.loc[i,'idRegistro'],datosgenreal.loc[i,'nombre'],datosgenreal.loc[i,'FKresultado'],datosgenreal.loc[i,'cedula'],datosgenreal.loc[i,'Carrera']))
            
                

     
    nuevos=datos_estudiantes_nuevos
      

    jsonabandono = json.dumps({'salary': int(datos_abandono)})
    jsongraduado = json.dumps({'salary': int(datos_graduado)})
    return render_template("index3.html",data=Persona,catidad_estu=datos_cantidad,abandonos=datos_abandono,graduado=datos_graduado,abandono_in=indice_abandono,nuevos=nuevos,a=jsonabandono,g=jsongraduado,informe=nombre,datoscarrea=Carrera)
    

    print(request.form['abandono'])
    nombre=request.form['abandono']
  
    Persona=[]
    Carrera=[]
    cantidad=pandas.read_sql("select count(*) from registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
   
    abandono=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 0 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    graduado=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 1 AND numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradatoorginal=pandas.read_sql("select Carrera FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    carreradato=carreradatoorginal.drop_duplicates()

    datosgenreal=pandas.read_sql("SELECT  idRegistro,cedula,nombre,Carrera,FKresultado FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)
    
    

    cuenta_carrera = carreradatoorginal['Carrera'].value_counts()
               
    for i in range(len(carreradato)):
        programa=carreradato.iloc[i,0]
        cuenta=cuenta_carrera[carreradato.iloc[i,0]]
        item=i+1
        Carrera.append(carrera(item,programa,cuenta))
   
   
     
    
    estudiantes_nuevos=pandas.read_sql("select count(*) FROM registro WHERE numero_entrega='{}'""".format(nombre[0]),db.connection)


    datos_estudiantes_nuevos=estudiantes_nuevos.loc[0, 'count(*)']
    datos_cantidad=cantidad.loc[0, 'count(*)']
   
    
    datos_abandono=abandono.loc[0,'count(*)']
    indice_abandono=(100*datos_abandono)/datos_cantidad
    datos_graduado=graduado.loc[0,'count(*)']

    numero=0
    print(datosgenreal)
    print(datosgenreal.loc[1,'nombre'])
    
    for i in range(len(datosgenreal)):
       numero=numero+1
      
       Persona.append(persona(numero,datosgenreal.loc[i,'nombre'],datosgenreal.loc[i,'FKresultado'],datosgenreal.loc[i,'cedula'],datosgenreal.loc[i,'Carrera']))
            
                

     
    nuevos=datos_estudiantes_nuevos
      

    jsonabandono = json.dumps({'salary': int(datos_abandono)})
    jsongraduado = json.dumps({'salary': int(datos_graduado)})
    return render_template("index3.html",data=Persona,catidad_estu=datos_cantidad,abandonos=datos_abandono,graduado=datos_graduado,abandono_in=indice_abandono,nuevos=nuevos,a=jsonabandono,g=jsongraduado,informe=nombre,datoscarrea=Carrera,bandera=1)
   
  
   
    

@Enviar_datos_indi_bleu.route('/Eliminar',methods=['GET', 'POST'])
@login_required
def Eliminar():

    nombre=request.form['eliminar']
    user=request.form['usuario']
    print(user)
    file="Archivo/"+user+"/"+nombre
    print(file)
  

    cursor = db.connection.cursor()
    sql=" DELETE FROM registro WHERE Numero_entrega ="+nombre[0]
    cursor.execute(sql)
    sql=" DELETE FROM registro_encuesta WHERE Numero_entrega ="+nombre[0]
    cursor.execute(sql)
    cursor.connection.commit()
    remove(file)
    return redirect("/Cargar_cvs")