from Projeto import app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from Projeto import db

class Administrador(db.Model):
	__tablename__ = "admin"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), unique=True)
	senha = db.Column(db.String(30), nullable=False)


	def __init__(self, nome, email, senha):
		self.nome = nome
		self.email = email
		self.senha = senha

class loja(db.Model):
	__tablename__= "lojas"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(50), nullable=False)
	telefone = db.Column(db.String(30), nullable=False)
	cnpj = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(50), unique=True)
	senha = db.Column(db.String(30), nullable=False)
	

	def __init__(self, nome, telefone, cnpj, email, senha):
		self.nome = nome
		self.telefone = telefone
		self.cnpj = cnpj
		self.email = email
		self.senha = senha


class desc(db.Model):
	__tablename__= "descricoes"

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	descricao = db.Column(db.String(50), nullable=False)
	quantidade = db.Column(db.Integer, nullable=False)
	valor = db.Column(db.Float, nullable=False)
	dia = db.Column(db.Date, nullable=False) 
	nomedaloja = db.Column(db.String(30), nullable=False)
	lojas_id = db.Column(db.Integer, db.ForeignKey('descricoes.id'), nullable=False)

	def __init__(self, descricao, quantidade, valor, dia, nomedaloja):
		self.descricao = descricao
		self.quantidade = quantidade
		self. valor = valor
		self.dia = data
		self.nomedaloja = nomedaloja

