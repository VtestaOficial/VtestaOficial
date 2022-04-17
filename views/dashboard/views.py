from flask import Flask, render_template, redirect, url_for, request, abort,session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine
from sqlalchemy.sql import func, text
import os
    # CORREOS
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid

    # FORMULARIOS
from forms.forms import *

app = Flask(__name__)
db = SQLAlchemy(app)
msg = EmailMessage()

dashboard = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard.route('/dashboard/home')
@login_required
def dashboard_inicio():
    return render_template("Dashboard/Inicio/inicio.html")

