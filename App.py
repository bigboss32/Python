

import flask
from flask import Flask, render_template, request
from routes.Subir import Subir_blue
from routes.Predicion import Predicion_blue
from routes.Crud import Crud_blue
from routes.Historia_cvs import historial_blue
from routes.Cargar import Cargar_cvs_blue
from flask_sqlalchemy import SQLAlchemy

# creating instance of the class
app = Flask(__name__)
app.secret_key="1"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/predicion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

SQLAlchemy(app)

@app.route('/')
def index():
    return flask.render_template('index3.html')

@app.route('/a')
def a():
    return flask.render_template('simple.html')

app.register_blueprint(Subir_blue)
app.register_blueprint(Predicion_blue)
app.register_blueprint(Crud_blue)
app.register_blueprint(historial_blue)
app.register_blueprint(Cargar_cvs_blue)







