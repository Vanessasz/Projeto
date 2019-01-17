from Projeto import app
from Projeto.models import bd
from flask import render_template,request, url_for, redirect #Fiz import do render_template 
from Projeto.controllers.form import FormHome
from flask_sqlalchemy import SQLAlchemy

@app.route("/", methods=['GET', 'POST']) #Aqui definimos uma rota ṕara a página
def home(): #Defini uma função para essa página.
	
    form = FormHome()
    
    if form.validate_on_submit():
    	valores = desc(descricao=form.descricao.data,quantidade=form.quantidade.data,
    					valor=form.valor.data, dia=form.dia.data,nomedaloja=form.nomedaloja.data)  
    	db.session.add(valores)
    	db.session.commit()
   
    return render_template('estrutura.html', form=form)


