from flask import Blueprint,request,render_template
import os
from werkzeug.utils import secure_filename

historial_blue=Blueprint('Historia_cvs',__name__)


@historial_blue.route('/Historia_cvs')
def historial():
 return render_template("simple.html")

   