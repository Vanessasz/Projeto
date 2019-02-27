from Projeto import app, db, login_manager
from flask_login import UserMixin

from flask_login import login_user

@login_manager.user_loader
def load_user(_id):
	return loja.query.get(int(_id))

class Administrador(db.Model):
	__tablename__ = "admin"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String, nullable=False)
	email = db.Column(db.String, unique=True)
	senha = db.Column(db.String, nullable=False)


	def __init__(self, nome, email, senha):
		self.nome = nome
		self.email = email
		self.senha = senha

class loja(db.Model, UserMixin):
	__tablename__= "lojas"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String, nullable=False)
	telefone = db.Column(db.String, nullable=False)
	cnpj = db.Column(db.String, nullable=False)
	email = db.Column(db.String, unique=True)
	senha = db.Column(db.String, nullable=False)
	
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False 

	def get_id(self):
		return str(self._id)
	
	
		self.nome = nome
		self.telefone = telefone
		self.cnpj = cnpj
		self.email = email
		self.senha = senha


class desc(db.Model):
	__tablename__= "descricoes"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	descricao = db.Column(db.String, nullable=False)
	quantidade = db.Column(db.Integer, nullable=False)
	valor = db.Column(db.Float, nullable=False)
	dia = db.Column(db.Date, nullable=False) 
	nomeloja = db.Column(db.String, nullable=False)
	descricoes_id = db.Column(db.Integer, db.ForeignKey('lojas._id'), nullable=False)


	def __repr__(self):
		return f"desc('{self.descricao}', '{self.quantidade}', '{self.valor}',  '{self.dia}',  '{self.nomeloja}' ,  '{self.descricoes_id}')"
