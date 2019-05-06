from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user, AnonymousUserMixin, LoginManager, login_user
from wtforms import StringField, BooleanField, PasswordField, SubmitField, FloatField, DateField, IntegerField, SelectField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import validators


class FormSistema(FlaskForm):
	descricao = StringField('Descrição',validators=[DataRequired()])
	quantidade = IntegerField('Quantidade', validators=[DataRequired()])
	valor = FloatField('Quantidade', validators=[DataRequired()])
	dia = DateField('Data', validators=[DataRequired()],  format='%d-%m-%Y')
	nomeloja = StringField('Nome da Loja', [validators.DataRequired()])
	enviar = SubmitField('Adicionar')


class FormRegistro(FlaskForm):
	nome = StringField('Digite o nome da sua loja',validators=[DataRequired()])
	telefone = StringField('Digite o telefone',validators=[DataRequired()])
	cnpj = StringField('Digite o CNPJ',validators=[DataRequired()])
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
	choices = [('descricao', 'valor', 'nomeloja')]
	select = SelectField('Pesquisar itens', choices=choices)
	search = StringField('')
	enviar = SubmitField('Buscar')