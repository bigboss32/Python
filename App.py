

import flask
from flask import Flask, render_template, request
from routes.Subir import Subir_blue
from routes.Predicion import Predicion_blue
from flask_sqlalchemy import SQLAlchemy

# creating instance of the class
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/ predicion'

SQLAlchemy(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

app.register_blueprint(Subir_blue)
app.register_blueprint(Predicion_blue)









