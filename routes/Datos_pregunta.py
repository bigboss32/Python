from flask import Blueprint, request,render_template,redirect
from os import remove
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
Datos_pregunta_bleu = Blueprint('Datos_pregunta', __name__)
db = MySQL()

@Datos_pregunta_bleu.route('/Datos_pregunta',methods=['GET', 'POST'])
@login_required
def datos_pregunta():
    return render_template("data.html")