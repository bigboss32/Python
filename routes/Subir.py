from flask import Blueprint, request, redirect, render_template,url_for
import os
from werkzeug.utils import secure_filename
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import joblib
import numpy as np
Subir_blue = Blueprint('Subir', __name__)
db = MySQL()


ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False


def comprobar(user):

    if os.path.isdir("Archivo") == False:
         os.mkdir("Archivo")
    if os.path.isdir("Archivo"+"/"+user) == False:
        os.mkdir("Archivo"+"/"+user)


@Subir_blue.route('/Subir', methods=['POST'])
@login_required
def Subir():
            global prediction
            global error
            prediction = "Error en el formato de los datos"
            error = "No envio ningun archivo valido"
            try:
                   
                    cursor = db.connection.cursor()
                    file = request.files["subirarchivo"]
                    user=request.form["usuario"]
                   
                    comprobar(user)
                  
                    

                        
                        


                    filename = secure_filename(file.filename)


                
                        
                        
                    if file and allowed_file(filename):
                        numero_entrega=pandas.read_sql("select MAX(numero_entrega) from registro ",db.connection)
                        max_entrega=numero_entrega.loc[0,'MAX(numero_entrega)']
                        if max_entrega==None:
                            max_entrega=0
                        nombre=str(max_entrega+1)+")"+ filename
                        file.save(os.path.join("Archivo"+"/"+user,str(max_entrega+1)+")"+ filename))
                        filename2 = "Archivo/"+user+"/"+nombre
                      

                        dfFiltro = pandas.read_csv(filename2, sep=';')
                        data_final=dfFiltro.loc[:, ['nombre','cedula','PROGRAMA','EDAD_DE_INGRESO','Actualmente_trabaja','Tipo_de_población_a_la_que_pertenece','ESTADO_CIVIL'
                                                            ,'¿Cómo_financia_sus_estudios?','CIRCUNSCRIPCION','¿Dispone_de_un_computador_permanentemente?','¿Posee_conexión_permanente_a_internet?'
                                                            ,'SEXO','ESTRATO']]
                        data_final.insert(loc = 0 , column = 'numero_entrega', value = max_entrega+1)

                    
                            
                        





                        dfFiltro['EDAD_DE_INGRESO']=dfFiltro['EDAD_DE_INGRESO'].astype(int) 
                        dfFiltro['EDAD_DE_INGRESO']=pandas.cut(dfFiltro['EDAD_DE_INGRESO'],[0,18,24,34,44,54],labels=[0,1,2,3,4])
                        dfFiltro['EDAD_DE_INGRESO']=dfFiltro['EDAD_DE_INGRESO'].astype(int) 
                                #Columna de Sexo 
                        dfFiltro.SEXO.replace(['M', 'F'],[1,0], inplace=True)

                        dfFiltro.Actualmente_trabaja.replace(['Sí', 'No'],[1,0], inplace=True)
                        dfFiltro.Tipo_de_población_a_la_que_pertenece.replace(["Urbana","Rural"],[1,0], inplace=True)

                        dfFiltro["ESTADO_CIVIL"].replace(['Soltero', 'Unión Libre', 'Madre soltera', 'Casado', 'Religioso','Divorciado'],[0,1,2,3,4,5], inplace=True)

                        dfFiltro['¿Cómo_financia_sus_estudios?'].replace(['Familia', 'Crédito', 'Recursos Propios', 'Beca'],[0,1,2,3], inplace=True)

                        dfFiltro['CIRCUNSCRIPCION'].replace(['REGULAR PREGRADO', 'DESPLAZADO', 'PUEBLO INDIGENA',
                                                                    'COMUNIDAD NEGRA', 'VICTIMA DEL CONFLICTO ARMADO INTERNO'],
                                                                    [0,1,2,3,4], inplace=True)

                                # Columna de Estrato 

                        dfFiltro['¿Dispone_de_un_computador_permanentemente?'].replace(['Sí', 'No'],[1,0], inplace=True)

                        dfFiltro['¿Posee_conexión_permanente_a_internet?'].replace(['Sí', 'No'],[1,0], inplace=True)

                    


                      
                        data=dfFiltro.loc[:, ['nombre','cedula','PROGRAMA','EDAD_DE_INGRESO','Actualmente_trabaja','Tipo_de_población_a_la_que_pertenece','ESTADO_CIVIL'
                                                            ,'¿Cómo_financia_sus_estudios?','CIRCUNSCRIPCION','¿Dispone_de_un_computador_permanentemente?','¿Posee_conexión_permanente_a_internet?'
                                                            ,'SEXO','ESTRATO']]


                      
                    
                        data.insert(loc = 0 , column = 'numero_entrega', value = max_entrega+1)
                            
                        loaded_model=joblib.load('Modelo\MLPClassifier.pkl')
                        
                        b=data.iloc[:, 4:14] 
                
                        for i in range(len(data)):
                                    a=data.iloc[i]
                                    to_predict = np.array(b.iloc[i]).reshape(1, 10)
                                    result = loaded_model.predict(to_predict)
                                    final=result[0]
                                    
                                    cursor.execute('INSERT INTO registro (numero_entrega,Carrera, nombre, cedula,edad_de_ingreso,Actualmente_trabaja,Tipo_de_población_a_la_que_pertenece,ESTADO_CIVIL,Cómo_financia_sus_estudios,CIRCUNSCRIPCION,Dispone_de_un_computador_permanentemente,Posee_conexión_permanente_a_internet,sexo,estrato,FKresultado,usuario) VALUES (%s,%s,%s, %s,%s, %s,%s, %s, %s,%s, %s, %s,%s,%s,%s,%s)',
                                    (
                                    a.numero_entrega,a.PROGRAMA,a.nombre,a.cedula,a.EDAD_DE_INGRESO,a.Actualmente_trabaja,a.Tipo_de_población_a_la_que_pertenece,a.ESTADO_CIVIL,a['¿Cómo_financia_sus_estudios?'],a.CIRCUNSCRIPCION,a['¿Dispone_de_un_computador_permanentemente?'],a['¿Posee_conexión_permanente_a_internet?'],a.SEXO,a.ESTRATO,final,user
                                    ))

                                    a=data_final.iloc[i]
                                
                                    cursor.execute('INSERT INTO registro_encuesta (numero_entrega,Carrera, nombre, cedula,edad_de_ingreso,Actualmente_trabaja,Tipo_de_población_a_la_que_pertenece,ESTADO_CIVIL,Cómo_financia_sus_estudios,CIRCUNSCRIPCION,Dispone_de_un_computador_permanentemente,Posee_conexión_permanente_a_internet,sexo,estrato,FKresultado,usuario) VALUES (%s,%s,%s, %s,%s, %s,%s, %s, %s,%s, %s, %s,%s,%s,%s,%s)',
                                        (
                                        a.numero_entrega,a.PROGRAMA,a.nombre,a.cedula,a.EDAD_DE_INGRESO,a.Actualmente_trabaja,a.Tipo_de_población_a_la_que_pertenece,a.ESTADO_CIVIL,a['¿Cómo_financia_sus_estudios?'],a.CIRCUNSCRIPCION,a['¿Dispone_de_un_computador_permanentemente?'],a['¿Posee_conexión_permanente_a_internet?'],a.SEXO,a.ESTRATO,final,user
                                        ))
                        cursor.connection.commit()
                        return  redirect(url_for('Datos.datos',question_id=user))
            
            except ValueError:
                prediction="Error en el formato de los datos"
            return render_template("500.html", prediction=prediction,error=error)       