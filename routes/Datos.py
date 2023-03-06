from flask import Blueprint,render_template
from flask_login import login_required
from flask_mysqldb import MySQL
import pandas
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
datos_blue=Blueprint('Datos',__name__)
db = MySQL()


@datos_blue.route('/datos', methods=['GET', 'POST'])
@login_required
def datos():

    Persona=[]
    Carrera=[]
    cantidad=pandas.read_sql("select count(*) from registro ",db.connection)
    Datafreresultado =pandas.read_sql("SELECT  FKresultado FROM registro ",db.connection)
    abandono=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 0 ",db.connection)
    graduado=pandas.read_sql("select count(*) FROM registro WHERE FKresultado = 1 ",db.connection)
    carreradatoorginal=pandas.read_sql("select Carrera FROM registro ",db.connection)
    carreradato=carreradatoorginal.drop_duplicates()
    
    cuenta_carrera = carreradatoorginal['Carrera'].value_counts()
   
    for i in range(len(carreradato)):
     Carrera.append(carrera(i+1,carreradato.loc[i,'Carrera'],cuenta_carrera[i]))
   
   
     
    
    estudiantes_nuevos=pandas.read_sql("select count(*) FROM registro ",db.connection)
    Datafremenombre =pandas.read_sql("SELECT nombre FROM registro ",db.connection)

    datos_estudiantes_nuevos=estudiantes_nuevos.loc[0, 'count(*)']
    datos_cantidad=cantidad.loc[0, 'count(*)']
    Datafreresultadodos =pandas.read_sql("SELECT  Carrera FROM registro",db.connection)
    datos_abandono=abandono.loc[0,'count(*)']
    indice_abandono=(datos_cantidad/datos_abandono)/100
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
    return render_template("index3.html",data=Persona,catidad_estu=datos_cantidad,abandonos=datos_abandono,abandono_in=indice_abandono,nuevos=nuevos,a=jsonabandono,g=jsongraduado,datoscarrea=Carrera)