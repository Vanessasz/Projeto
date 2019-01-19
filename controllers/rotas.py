from Projeto import app
from Projeto.models import bd
from flask import render_template,request, url_for, redirect #Fiz import do render_template 
from Projeto.controllers.form import FormSistema, FormRegistro
from flask_sqlalchemy import SQLAlchemy


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')



@app.route("/sistema", methods=['GET', 'POST']) #Aqui definimos uma rota ṕara a página
def sistema(): #Defini uma função para essa página.
	
    form = FormSistema()
    
    if form.validate_on_submit():
    	valores = desc(descricao=form.descricao.data,quantidade=form.quantidade.data,
    					valor=form.valor.data, dia=form.dia.data,nomedaloja=form.nomedaloja.data)  
    	db.session.add(valores)
    	db.session.commit()
   
    return render_template('sistema.html', form=form)


@app.route("/registro", methods=['GET', 'POST'])
def registro(): 

	form = FormRegistro()



	return render_template('registro.html', form=form)