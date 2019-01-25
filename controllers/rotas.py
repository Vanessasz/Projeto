from Projeto import app, db #Aqui estou fazendo o importe da instância que eu criei.

from Projeto.models import database
from Projeto.models.database import desc

from flask import render_template, url_for, flash, redirect, request, abort, send_file, Markup
from flask_sqlalchemy import SQLAlchemy

from Projeto.controllers.form import FormSistema, FormRegistro

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')



@app.route("/sistema", methods=['GET', 'POST']) #Aqui definimos uma rota ṕara a página
def sistema(): #Defini uma função para essa página.
	
    form = FormSistema()
    
    if form.validate_on_submit():
    	print('validou')
    	valores = desc(descricao=form.descricao.data, quantidade=form.quantidade.data, valor=form.valor.data, 
    					dia=form.dia.data, nomeloja=form.nomeloja.data)  
    	db.session.add(valores) #session usando os atributos.
    	db.session.commit()

    	return redirect(url_for('sistema'))
   
    return render_template('sistema.html', form=form)


@app.route("/registro", methods=['GET', 'POST'])
def registro(): 

	form = FormRegistro()



	return render_template('registro.html', form=form)