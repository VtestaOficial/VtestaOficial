import os
#import pymysql

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# SQL LITE DE PRUEBAS
# PWD = os.path.abspath(os.curdir)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False


# POSTGREST DE PRODUCTIVO
SQLALCHEMY_DATABASE_URI = "postgresql://ivan:lolo1639.@vtesta.info:5432/vtesta" # CONEXION PRUEBA
#SQLALCHEMY_DATABASE_URI = "postgresql://ivan:lolo1639.@localhost:5432/vtesta" # CONEXION SERVER
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 30
SQLALCHEMY_MAX_OVERFLOW = -1 #CONEXIONES SIMULTANEAS -1
