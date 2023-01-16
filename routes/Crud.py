from flask import Blueprint,render_template,request,redirect,flash
from models.Tablas import persona
from utils.db import db
Crud_blue=Blueprint('Crud',__name__)

@Crud_blue.route("/Crud")
def Crud_html():
    personas=persona.query.all()
    return render_template("Crud.html",personas=personas)

@Crud_blue.route("/nuevapersona", methods=['POST'])
def nueva_persona():
    name=request.form['name']
    email=request.form['email']
    telefono=request.form['telefono']
    new_persona=persona(name,email,telefono)
    db.session.add(new_persona)
    db.session.commit()
    print(new_persona)
    flash("contacto creado exelente")
    return redirect("/Crud")

@Crud_blue.route("/eliminarpersona/<id>")
def eliminar_persona(id):
    personaeliminada=persona.query.get(id)
    db.session.delete(personaeliminada)
    db.session.commit()
    return redirect("/Crud")

@Crud_blue.route("/actualizarpersona/<id>",methods=['POST','GET'])
def actualizar_persona(id):
    actualizaiconpersona=persona.query.get(id)
    if request.method =='POST':
     
        actualizaiconpersona.name=request.form['name']
        actualizaiconpersona.email=request.form['email']
        actualizaiconpersona.telefono=request.form['telefono']
        db.session.commit()
        return redirect("/Crud")
  

   
    return render_template("Actualizacion.html",actualizaiconpersona=actualizaiconpersona)