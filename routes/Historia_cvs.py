from flask import Blueprint,request,render_template
import os
import time
from models.entities.Archivo import Tree
historial_blue=Blueprint('Historia_cvs',__name__)


@historial_blue.route('/Historia_cvs')
def historial():
        a=0
        ejemplo_dir = 'Archivo'
        contenido = os.listdir(ejemplo_dir)
        archivos = []
        
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.csv'):
                ti_c = os.path.getctime(ejemplo_dir+"/"+fichero)
                c_ti = time.ctime(ti_c)
                historial_temp=Tree(fichero,c_ti)
                print(historial_temp.nombre)
                print(historial_temp.fecha)
                archivos.append(historial_temp)

               
        

        return render_template("simple.html",archivos=archivos,)

   