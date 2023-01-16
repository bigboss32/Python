from utils.db import db

class persona(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    email=db.Column(db.String(80))
    telefono=db.Column(db.String(80))
    def __init__(self,name,email,telefono):
        self.name=name
        self.email=email
        self.telefono=telefono