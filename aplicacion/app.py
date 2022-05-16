from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from aplicacion import config
    # FORMS
from forms.forms import *
    # VIEWS
from views.menus.views import menus
from views.dashboard.views import dashboard
from views.apis.views import apis
    # DRIVER
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
import os

from flask_mail import Message, Mail

    # APP
app = Flask(__name__)
    # VIEWS
app.register_blueprint(menus)
app.register_blueprint(dashboard)
app.register_blueprint(apis)
    # SYSTEM
app.config.from_object(config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

    # CORREO ENVIOS
app.config['MAIL_SERVER'] = 'smtp.ionos.mx'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contacto@vtesta.info'
app.config['MAIL_PASSWORD'] = '132Tres132-'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail()
mail.init_app(app)


### ------------------------------------------------------- INICIO  PAGES ----------------------------------------------------------####
@app.route('/login', methods=['get', 'post'])
def login():
    from models.models import Usuarios
    # Control de permisos - cambiar pizarron para redirigir
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard_inicio"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('dashboard.dashboard_inicio'))
        form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('inicio/login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/registro", methods=["get", "post"])
def registro():
    from models.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("menus.inicio"))
    form = FormUsuario()
    if form.validate_on_submit():
        existe_usuario = Usuarios.query.\
            filter_by(username=form.username.data).first()
        if existe_usuario is None:
            user = Usuarios()
            form.populate_obj(user)
            user.admin = False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("menus.menu_inicio"))
        form.username.errors.append("Nombre de usuario ya existe.")
    return render_template("inicio/registro.html", form=form)
### ------------------------------------------------------- FIN INICIO PAGES --------------------------------------------------------####


@login_manager.user_loader
def load_user(user_id):
    from models.models import Usuarios
    return Usuarios.query.get(int(user_id))

@app.errorhandler(404)
#@login_required
def page_not_found(error):
    return render_template("inicio/error.html", error="Página no encontrada..."), 404
