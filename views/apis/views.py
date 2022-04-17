from flask import Flask, render_template, redirect, url_for, request, abort, session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine
from sqlalchemy.sql import func, text
import os
    # FORMULARIOS
from forms.forms import *
    # APIS REQUERIMETS
from flask import jsonify

app = Flask(__name__)
db = SQLAlchemy(app)

apis = Blueprint('apis', __name__, template_folder='templates', static_folder='static')

@apis.route('/services/vtesta/users', methods=['GET'])
def get_users():
    from models.models import db
    result = db.engine.execute(text("SELECT * FROM usuarios"))
    return jsonify([dict(row) for row in result]) #DATOS EN JSON

@apis.route('/services/vtesta/users/<id>', methods=['GET'])
def get_user_id(id):
    from models.models import db
    result = db.engine.execute(text("SELECT * FROM usuarios WHERE id ="+id))
    return jsonify([dict(row) for row in result]) #DATOS EN JSON

@apis.route('/services/vtesta/terminos_y_condiciones', methods=['GET'])
def get_terminos_y_condiciones():
    from models.models import db
    result = db.engine.execute(text("SELECT * FROM terminos_y_condiciones"))
    return jsonify([dict(row) for row in result]) #DATOS EN JSON

@apis.route('/services/vtesta/politica_de_privacidad', methods=['GET'])
def get_politica_de_privacidad():
    from models.models import db
    result = db.engine.execute(text("SELECT * FROM politica_de_privacidad"))
    return jsonify([dict(row) for row in result]) #DATOS EN JSON
