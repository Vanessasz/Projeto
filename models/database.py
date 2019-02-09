from Projeto import app, db
from flask_login import UserMixin


'''
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

class loja(db.Model):
	__tablename__= "lojas"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String, nullable=False)
	telefone = db.Column(db.String, nullable=False)
	cnpj = db.Column(db.String, nullable=False)
	email = db.Column(db.String, unique=True)
	senha = db.Column(db.String, nullable=False)
	

	def __init__(self, nome, telefone, cnpj, email, senha):
		self.nome = nome
		self.telefone = telefone
		self.cnpj = cnpj
		self.email = email
		self.senha = senha

'''
class desc(db.Model):
	__tablename__= "descricoes"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	descricao = db.Column(db.String, nullable=False)
	quantidade = db.Column(db.Integer, nullable=False)
	valor = db.Column(db.Float, nullable=False)
	dia = db.Column(db.Date, nullable=False) 
	nomeloja = db.Column(db.String, nullable=False)
	#lojas_id = db.Column(db.Integer, db.ForeignKey('descricoes.id'), nullable=False)


	def __repr__(self):
		return f"desc('{self.descricao}', '{self.quantidade}', '{self.valor}',  '{self.dia}',  '{self.nomeloja}')"
