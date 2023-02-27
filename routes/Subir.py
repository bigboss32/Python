from flask import Blueprint, request
import os
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required
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
    file = request.files["subirarchivo"]
    print(file)
    filename = secure_filename(file.filename)
    print(filename)
    if file and allowed_file(filename):
        print("permitido")
        file.save(os.path.join("Archivo", filename))
        filename2 = "Archivo/"+filename
        data = pandas.read_csv(filename2, header=0)
        print(data.head(10))
        print(data.shape)
        loaded_model=joblib.load('Modelo\MLPClassifier.pkl')
        cursor = db.connection.cursor()
        for i in range(len(data)):
            a=data.iloc[i]
    
            to_predict = np.array(a).reshape(1, 10)
            result = loaded_model.predict(to_predict)

            if int(result)==0:
                    prediction=0
                    print("abando")
            elif int(result)==1:
                    prediction=1
                    print("gardu")
            else:
                prediction=-1
                print("no se")
             
    
            
            
         #   cursor.execute('INSERT INTO registro (numero_entrega, nombre, cedula,edad_de_ingreso,Actualmente_trabaja,Tipo_de_población_a_la_que_pertenece,ESTADO_CIVIL,Cómo_financia_sus_estudios,CIRCUNSCRIPCION,Dispone_de_un_computador_permanentemente,Posee_conexión_permanente_a_internet,GRADUADO,sexo,estrato) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)',
         #    (
         #     a.numero_entrega,a.nombre,a.cedula,a.edad_de_ingreso,a.Actualmente_trabaja,a.Tipo_de_población_a_la_que_pertenece,a.ESTADO_CIVIL,a.Cómo_financia_sus_estudios,#a.CIRCUNSCRIPCION,a.Dispone_de_un_computador_permanentemente,a.Posee_conexión_permanente_a_internet,a.GRADUADO,a.sexo,a.estrato
          #  ))
           # cursor.connection.commit()
      
    return "a"
