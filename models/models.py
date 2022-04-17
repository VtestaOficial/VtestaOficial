from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class TerminosyCondicones(db.Model):
    __tablename__ = 'terminos_y_condiciones'
    id = Column(Integer, primary_key=True)
    texto = Column(String(100), nullable=False)
    tipo = Column(String(128), nullable=False)
    tipo = Column(String(200), nullable=False)
    secuencia = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class PoliticaPrivacidad(db.Model):
    __tablename__ = 'politica_de_privacidad'
    id = Column(Integer, primary_key=True)
    texto = Column(String(100), nullable=False)
    tipo = Column(String(128), nullable=False)
    tipo = Column(String(200), nullable=False)
    secuencia = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Usuarios(db.Model):
    """Usuarios"""
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password_hash = Column(String(128), nullable=False)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    admin = Column(Integer)
    user_fi = Column(Integer)
    leader_fi = Column(Integer)
    user_am = Column(Integer)
    user_auditor = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Flask-Login integracion
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        return self.admin

    def is_user_auditor(self):
        return self.user_auditor

    def is_user_fi(self):
        return self.user_fi

    def is_leader_fi(self):
        return self.leader_fi
    
    def is_user_am(self):
        return self.user_am
