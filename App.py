from flask import Flask, render_template
from flask_mysqldb import MySQL
from routes.Subir import Subir_blue
from routes.Datos import datos_blue
from routes.Registrarse import resgitro_blue
from routes.Historia_cvs import historial_blue
from routes.Historial_usuarios import historial_usuarios_blue
from routes.Cargar import Cargar_cvs_blue
from routes.Inicio_de_sesion import sesion_blue
from routes.Enviar_datos_indivi import Enviar_datos_indi_bleu
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    print("hola")
    return render_template("inicio.html")

app.register_blueprint(Enviar_datos_indi_bleu)
app.register_blueprint(Subir_blue)
app.register_blueprint(datos_blue)
app.register_blueprint(resgitro_blue)
app.register_blueprint(historial_blue)
app.register_blueprint(Cargar_cvs_blue)
app.register_blueprint(sesion_blue)
app.register_blueprint(historial_usuarios_blue)







