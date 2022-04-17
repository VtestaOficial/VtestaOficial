from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField,\
    TextAreaField, SelectField, PasswordField, FloatField, TextField
from wtforms.fields.html5 import EmailField, DateTimeLocalField, DateField, DateTimeField,\
    SearchField
from flask_wtf.file import FileField
from wtforms.widgets import TextArea
from wtforms.validators import Required
from datetime import datetime


class LoginForm(FlaskForm):
    username = StringField('User', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Entrar')

class FormUsuario(FlaskForm):
    username = StringField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    nombre = StringField('Nombre completo')
    email = StringField('Email')
    admin =  SelectField("Admin", choices=[("0", "No"),("1", "Si")], default="No")
    user_fi =  SelectField("FI", choices=[("0", "No"),("1", "Si")], default="No")
    leader_fi =  SelectField("FI", choices=[("0", "No"),("1", "Si")], default="No")
    user_am =  SelectField("AM", choices=[("0", "No"),("1", "Si")], default="No")
    user_auditor =  SelectField("Auditor", choices=[("0", "No"),("1", "Si")], default="No")
    submit = SubmitField('Aceptar')
