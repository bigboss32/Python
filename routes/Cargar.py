from flask import Blueprint,request,render_template
import os
from werkzeug.utils import secure_filename

Cargar_cvs_blue=Blueprint('Cargar_cvs',__name__)


@Cargar_cvs_blue.route('/Cargar_cvs')
def historial():
 return render_template("Cargar.html")
