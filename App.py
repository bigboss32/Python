#importing libraries
import os
import numpy as np
import flask
from flask import Flask, render_template, request
import joblib
from werkzeug.utils import secure_filename

#creating instance of the class
app=Flask(__name__)
app.config['UPLOAD_FOLDER']="Archivo"
ALLOWED_EXTENSIONS=set(['csv'])


#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def allowed_file(file):
    file=file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False
@app.route('/Subir',methods = ['POST'])
def Subir():
    file=request.files["subirarchivo"]
    print(file,file.filename)
    filename=secure_filename(file.filename)
    if file and allowed_file(filename):
        print("permitido")
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
    return "s"

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 9)
    loaded_model=joblib.load('Modelo\modelo_entrenado.pkl')
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        try:
            to_predict_list = list(map(float, to_predict_list))
            result = ValuePredictor(to_predict_list)
            if int(result)==0:
                prediction='abandono'
            elif int(result)==1:
                prediction='graduado'
            else:
                prediction=f'{int(result)} No-definida'
        except ValueError:
            prediction='Error en el formato de los datos'

        return render_template("result.html", prediction=prediction)



if __name__=="__main__":

    app.run(port=5001)