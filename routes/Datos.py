from flask import Blueprint,request,render_template, redirect, url_for, flash
from flask_mysqldb import MySQL

datos_blue=Blueprint('Datos',__name__)
db = MySQL()


@datos_blue.route('/datos', methods=['GET', 'POST'])
def datos():
      cursor = db.connection.cursor()
      sql ="select * from registro"
      
      print(cursor.execute(sql))
      row = cursor.fetchone()
      print(row)
      print(row[1])
      print(row[2])
      print(row[3])
      print(row[4])
      return "a"