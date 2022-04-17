from flask import Flask, render_template, redirect, url_for, request, abort,session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine
from sqlalchemy.sql import func, text
import os
    # CORREOS
import smtplib
from flask_mail import Message, Mail
    # FORMULARIOS
from forms.forms import *

mail = Mail()
app = Flask(__name__)
db = SQLAlchemy(app)
mail.init_app(app)

menus = Blueprint('menus', __name__, template_folder='templates', static_folder='static')

@menus.route('/')
def menu_inicio():
    return render_template("Inicio/inicio.html")

@menus.route('/contactanos', methods=['GET', 'POST'])
def menu_inicio_contactanos():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Correo = request.form['Correo']
        Mensaje = request.form['Mensaje']
        #ENVIO DE CORREO A NOTIFICACIONES
        msg = Message(Nombre, sender='contacto@vtesta.info', recipients=['ivannaje15@gmail.com'])
        msg.html = """
              <h2>
              El Cliente: %s </br>
              Con el Correo: %s </br>
              Nos manda el Mensaje: %s </br>
              </h2>
              """ % (Nombre, Correo, Mensaje)
        try:
             mail.send(msg)
        except Exception as e:
            # Print any error messages to stdout
            #print(e)
            print('Se envio')
        return redirect(url_for('menus.menu_inicio_contactanos_envio'))
    return render_template("Contacto/inicio.html")

@menus.route('/contactanos/envio_exitoso')
def menu_inicio_contactanos_envio():
    return render_template("Contacto/respuesta.html")

@menus.route('/centro_de_ayuda', methods=['GET', 'POST'])
def menu_inicio_centro_de_ayuda():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Correo = request.form['Correo']
        Mensaje = request.form['Mensaje']
        #ENVIO DE CORREO A NOTIFICACIONES
        msg = Message(Nombre, sender='contacto@vtesta.info', recipients=['ivannaje15@gmail.com'])
        msg.html = """
              <h2>
              El Cliente: %s </br>
              Con el Correo: %s </br>
              Nos manda el Mensaje: %s </br>
              </h2>
              """ % (Nombre, Correo, Mensaje)
        try:
             mail.send(msg)
        except Exception as e:
            # Print any error messages to stdout
            #print(e)
            print('Se envio')
        return redirect(url_for('menus.menu_inicio_contactanos_envio'))
    return render_template("Centro_ayuda/inicio.html")

@menus.route('/desarrollo_personalizado', methods=['GET', 'POST'])
def menu_inicio_desarrollo_personalizado():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Correo = request.form['Correo']
        Mensaje = request.form['Mensaje']
        #ENVIO DE CORREO A NOTIFICACIONES
        msg = Message(Nombre, sender='contacto@vtesta.info', recipients=['ivannaje15@gmail.com'])
        msg.html = """
              <h2>
              El Cliente: %s </br>
              Con el Correo: %s </br>
              Nos manda el Mensaje: %s </br>
              </h2>
              """ % (Nombre, Correo, Mensaje)
        try:
             mail.send(msg)
        except Exception as e:
            # Print any error messages to stdout
            #print(e)
            print('Se envio')
        return redirect(url_for('menus.menu_inicio_contactanos_envio'))
    return render_template("Desarrollo/inicio.html")

@menus.route('/terminos_y_condiciones')
def menu_inicio_terminos_y_condiciones():
    from models.models import db
    resultados = db.engine.execute(text("SELECT * FROM terminos_y_condiciones"))
    return render_template("Terminos/inicio.html", resultados=resultados)

@menus.route('/politica_de_privacidad')
def menu_inicio_politica_de_privacidad():
    from models.models import db
    resultados = db.engine.execute(text("SELECT * FROM politica_de_privacidad"))
    return render_template("Condiciones/inicio.html", resultados=resultados)
