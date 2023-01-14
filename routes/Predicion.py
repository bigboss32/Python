from flask import Blueprint,request,render_template
import joblib
import numpy as np
Predicion_blue=Blueprint('Predicion',__name__)

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 9)
    loaded_model=joblib.load('Modelo\modelo_entrenado.pkl')
    result = loaded_model.predict(to_predict)
    return result[0]

@Predicion_blue.route('/result',methods = ['POST'])
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