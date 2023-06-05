from flask import Blueprint, request,render_template,redirect
from os import remove
from flask_login import login_required
import pandas
from flask_mysqldb import MySQL
import json
from models.entities.Persona import persona
from models.entities.Carrera import carrera
from models.entities.Encuestas import encuesta
from models.entities.Descargar_csv import obj
Total_estudiantes_use_bleu = Blueprint('Total_estudiantes_use', __name__)
db = MySQL()
@Total_estudiantes_use_bleu.route('/total_estudiantes_use',methods=['GET', 'POST'])
@login_required
def total():
        
 
        
    
            
 return "hola"