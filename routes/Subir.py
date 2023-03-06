from flask import Blueprint, request,redirect,render_template
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


@Subir_blue.route('/Subir', methods=['POST'])
    
@login_required
def Subir():
    global prediction
    global error
    prediction="Error en el formato de los datos"
    error="No envio ningun archivo valido"
    try:

        file = request.files["subirarchivo"]
 
        filename = secure_filename(file.filename)
        
        if file and allowed_file(filename):
            numero_entrega=pandas.read_sql("select MAX(numero_entrega) from registro ",db.connection)
            max_entrega=numero_entrega.loc[0,'MAX(numero_entrega)']
            if max_entrega==None:
                max_entrega=0
        
            
            
            if max_entrega>=0:
                nombre=str(max_entrega+1)+")"+ filename
                file.save(os.path.join("Archivo",str(max_entrega+1)+")"+ filename))
                filename2 = "Archivo/"+nombre
                data = pandas.read_csv(filename2, header=0)
                data.insert(loc = 0 , column = 'numero_entrega', value = max_entrega+1)
                loaded_model=joblib.load('Modelo\MLPClassifier.pkl')
                cursor = db.connection.cursor()
                b=data.iloc[:, 4:14] 
                print(b)
                for i in range(len(data)):
                    a=data.iloc[i]
                    to_predict = np.array(b.iloc[i]).reshape(1, 10)
                    result = loaded_model.predict(to_predict)
                    final=result[0]
                    
                    cursor.execute('INSERT INTO registro (numero_entrega,Carrera, nombre, cedula,edad_de_ingreso,Actualmente_trabaja,Tipo_de_población_a_la_que_pertenece,ESTADO_CIVIL,Cómo_financia_sus_estudios,CIRCUNSCRIPCION,Dispone_de_un_computador_permanentemente,Posee_conexión_permanente_a_internet,sexo,estrato,FKresultado) VALUES (%s,%s,%s, %s,%s, %s,%s, %s, %s,%s, %s, %s,%s,%s,%s)',
                    (
                    a.numero_entrega,a.Carrera,a.nombre,a.cedula,a.edad_de_ingreso,a.Actualmente_trabaja,a.Tipo_de_población_a_la_que_pertenece,a.ESTADO_CIVIL,a.Cómo_financia_sus_estudios,a.CIRCUNSCRIPCION,a.Dispone_de_un_computador_permanentemente,a.Posee_conexión_permanente_a_internet,a.sexo,a.estrato,final
                    ))
                cursor.connection.commit()
                return redirect("/Historia_cvs")
            else:
                return redirect("/datos")
    except ValueError:
            prediction="Error en el formato de los datos"
    return render_template("500.html", prediction=prediction,error=error)
       