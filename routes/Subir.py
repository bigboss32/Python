from flask import Blueprint, request
import os
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required
import pandas
from flask_mysqldb import MySQL
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
        for col in data:
            print(str(data[col]))
    return "s"
