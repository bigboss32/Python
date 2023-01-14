from flask import Blueprint,request
import os
from werkzeug.utils import secure_filename

Subir_blue=Blueprint('Subir',__name__)


ALLOWED_EXTENSIONS=set(['csv'])

def allowed_file(file):
    file=file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False
@Subir_blue.route('/Subir',methods = ['POST'])
def Subir():
    file=request.files["subirarchivo"]
    print(file,file.filename)
    filename=secure_filename(file.filename)
    if file and allowed_file(filename):
        print("permitido")
        file.save(os.path.join("Archivo",filename))
    return "s"