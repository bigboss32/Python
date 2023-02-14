
from .entities.user import User
class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            print()
            sql="""SELECT idUsuario,Nombre,contrase,correo FROM usuario where correo='{}'""".format(user.correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], User.contrase), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        