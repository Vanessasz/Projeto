from Projeto import app, db #Aqui estou fazendo o importe da instância que eu criei.

from Projeto.models import database
from Projeto.models.database import desc

from flask import render_template, url_for, flash, redirect, request, abort, send_file, Markup
from flask_sqlalchemy import SQLAlchemy

from Projeto.controllers.form import FormSistema, FormRegistro

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
	valores = 0s

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



	return render_template('registro.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():

	return render_template('login.html')



