from flask import Blueprint,request,render_template
import os
import time
historial_blue=Blueprint('Historia_cvs',__name__)


@historial_blue.route('/Historia_cvs')
def historial():
        a=0
        ejemplo_dir = 'Archivo'
        contenido = os.listdir(ejemplo_dir)
        archivos = []
        tiempo = []
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.csv'):
                archivos.append(fichero)
                print(fichero)
                ti_c = os.path.getctime(ejemplo_dir+"/"+fichero)
                c_ti = time.ctime(ti_c)
                tiempo.append(c_ti)
      
        
        print(archivos)
        print(tiempo)
        return render_template("simple.html",archivos=archivos,fecha=tiempo)

   