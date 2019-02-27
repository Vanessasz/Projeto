from Projeto import app, db #Aqui estou fazendo o importe da instância que eu criei.

from Projeto.models import database
from Projeto.models.database import desc, loja

from flask import render_template, url_for, flash, redirect, request, abort, send_file, Markup
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_user, login_manager

from Projeto.controllers.form import FormSistema, FormRegistro, FormLogin

@app.route("/")
@app.route("/home")
def home():
	""" Essa função renderiza a página principal """
	return render_template('home.html')



@app.route("/sistema", methods=['GET', 'POST']) 
	#Aqui definimos uma rota ṕara a página
def sistema(): 
	#Defini uma função para essa página
	
	form = FormSistema()
	""" Instanciei meu formulário para poder usar """
	valores = 0

	query = desc.query.filter_by(_id=2).first()

	print('VALORES',valores)

	if form.validate_on_submit():
		print('NO IF')
		valores = desc(descricao=form.descricao.data, quantidade=form.quantidade.data, valor=form.valor.data, 
							dia=form.dia.data, nomeloja=form.nomeloja.data)  

		db.session.add(valores)
		#session usando os atributos
		db.session.commit()
		#salvando os dados definitivo no banco de dados
		
		
		print(valores)

		return redirect(url_for('sistema'))

	return render_template('sistema.html', form=form, query=query)

  


@app.route("/registro", methods=['GET', 'POST'])
def registro(): 

	form = FormRegistro()

	
	if form.validate_on_submit():
		valores = loja(nome=form.nome.data, telefone=form.telefone.data, cnpj=form.cnpj.data, 
			email=form.email.data, senha=form.senha.data)

		db.session.add(valores)

		db.session.commit()

	return render_template('registro.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():

	form = FormLogin()
	
	if form.validate_on_submit():
		query = loja.query.filter_by(email=form.email.data).first()
		if query and query.senha == form.senha.data:
			login_user(query)
			flash("Login efetuado com sucesso.")
	
			return redirect(url_for('sistema'))
		else:
			flash("Login inválido.")
			
	else: 
		print(form.errors)

	return render_template('login.html', form=form)



