class Config:
    SECRET_KEY="1"

class DevolopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='root'
    MYSQL_DB='proyecto'
   

config={
    'development':DevolopmentConfig
}