from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import TextField, StringField, BooleanField, PasswordField, SubmitField, FloatField, DateField, IntegerField, SelectField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import validators

from flask_login import current_user, AnonymousUserMixin


class FormSistema(FlaskForm):
	descricao = StringField('Descrição',validators=[DataRequired()])
	quantidade = IntegerField('Quantidade', validators=[DataRequired()])
	valor = FloatField('Quantidade', validators=[DataRequired()])
	dia = StringField('Data', validators=[DataRequired()])
	nomeloja = StringField()
	enviar = SubmitField('Adicionar')


class FormRegistro(FlaskForm):
	nome = StringField('Digite o nome da sua loja',validators=[DataRequired()])
	email = StringField('Digite o email',validators=[DataRequired(),Email()])
	senha = PasswordField('Digite sua senha',validators=[DataRequired()])
	confirma_senha = PasswordField('Confirme a senha',validators=[DataRequired(),EqualTo('senha')])
	enviar = SubmitField('Salvar')


class FormLogin(FlaskForm):
	email = StringField('Digite o email',validators=[DataRequired(),Email()])
	senha = PasswordField('Digite sua senha',validators=[DataRequired()])
	lembrar_me = BooleanField('Lembrar-me')	
	enviar = SubmitField('Salvar')


class LoginAdmin(FlaskForm):
	email = StringField('Digite seu email',validators=[DataRequired(),Email()])
	senha = PasswordField('Digite sua senha',validators=[DataRequired()])
	lembrar_me = BooleanField('Lembrar-me')	
	enviar = SubmitField('Acessar')
	

class SistemaBusca(Form):
	itens = [('descricao', 'quantidade', 'valor')]
	select = SelectField('Pesquisar itens', itens=itens)
	search = StringField('Faça sua Busca aqui')
	enviar = SubmitField('Buscar')

class FormVenda(FlaskForm):
	quantidade = IntegerField('Quantidade', validators=[DataRequired()])
	enviar = SubmitField('Vender')