from flask import Blueprint,request,render_template


sesion_blue=Blueprint('Inicio_de_sesion',__name__)


@sesion_blue.route('/Inicio_de_sesion')
def sesion():
 return render_template("partials/login-v2.html")

@sesion_blue.route('/registro')
def regsitro():
 return render_template("partials/register.html")

@sesion_blue.route('/recuperacion')
def recuperacion():
 return render_template("partials/recuperacion.html")