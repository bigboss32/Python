from flask import Blueprint,render_template
from flask_login import login_required
Cargar_cvs_blue=Blueprint('Cargar_cvs',__name__)
@Cargar_cvs_blue.route('/Cargar_cvs')
@login_required
def historial():
 return render_template("Cargar.html")
