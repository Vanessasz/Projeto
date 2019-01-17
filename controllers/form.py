from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user, AnonymousUserMixin
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class FormHome(FlaskForm):
    descricao = StringField('Descrição',validators=[DataRequired()])
    quantidade = FloatField('Quantidade', validators=[DataRequired()])
    valor = FloatField('Quantidade', validators=[DataRequired()])
    dia = DateField('Data', validators=[DataRequired()])
    nomeloja = StringField('Nome da Loja', validators=[DataRequired()])
    enviar = SubmitField('Adicionar')