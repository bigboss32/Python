from flask import Blueprint,request,render_template
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL
resgitro_blue=Blueprint('Registrase',__name__)

db = MySQL()

@resgitro_blue.route('/registro', methods=['GET', 'POST'])
def regsitro():
    if request.method == 'POST':
        if request.form['contra']==request.form['contrados']:
            
            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s)', (request.form['nom'],generate_password_hash(request.form['contra']),request.form['correo']))
            cursor.connection.commit()
            return render_template('inicio.html')
        else:
           
             return render_template("partials/register.html")

    else:
        return render_template("partials/register.html")