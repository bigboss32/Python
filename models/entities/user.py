from werkzeug.security import check_password_hash,generate_password_hash

class User():
    def __init__(self,idUsuario,Nombre,contrase,correo="") -> None:
        self.idUsuario=idUsuario
        self.Nombre=Nombre
        self.contrase=contrase
        self.correo=correo

    @classmethod
    def  check_password(self,hashed_password,contrase):
        return check_password_hash(hashed_password,contrase)

print(generate_password_hash("hola"))