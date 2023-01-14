# importing libraries
import os
import numpy as np
import flask
from flask import Flask, render_template, request
import joblib
from werkzeug.utils import secure_filename
from routes.Subir import Subir_blue
from routes.Predicion import Predicion_blue

# creating instance of the class
app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

app.register_blueprint(Subir_blue)
app.register_blueprint(Predicion_blue)









