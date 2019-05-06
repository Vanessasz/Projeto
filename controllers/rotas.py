from Projeto import app, db #Aqui estou fazendo o importe da instância que eu criei.

from Projeto.models import database
from Projeto.models.database import desc, loja, administrador

from flask import render_template, url_for, flash, redirect, request, abort, send_file, Markup
from flask_sqlalchemy import SQLAlchemy

from flask_login import login_user, login_manager, current_user, logout_user, login_required

from Projeto.controllers.form import FormSistema, FormRegistro, FormLogin, LoginAdmin, SistemaBusca

db.create_all()
db.session.commit()


@app.route("/")
@app.route("/home")
def home():
	""" Essa função renderiza a página principal """
	return render_template('home.html')



@app.route("/sistema", methods=['GET', 'POST']) 
	#Aqui definimos uma rota ṕara a página
@login_required 
	# Aqui o usuário só terá acesso ao sistema se estiver feito login

	
def sistema(): 
	#Defini uma função para essa página
	formulario = FormSistema()
	""" Instanciei meu formulário para poder usar """
	#form_busca = SistemaBusca()
	#busca

	valores = 0

	query = desc.query.filter_by(descricoes_id=current_user._id)
	print('ID',query)

	nomeloja = current_user._id
	print(current_user._id)

	if formulario.validate_on_submit():
		print('NO IF')
		valores = desc(descricao=formulario.descricao.data, quantidade=formulario.quantidade.data, valor=formulario.valor.data, 
							dia=formulario.dia.data, nomeloja=formulario.nomeloja.data, descricoes_id=current_user._id)  

		db.session.add(valores)
		#session usando os atributos
		db.session.commit()
		#salvando os dados definitivo no banco de dados
		
		flash(f'Adicionado com sucesso!', 'success')
		print(valores)

		return redirect(url_for('sistema'))

	return render_template('sistema.html', formulario=formulario, query=query)


@app.route("/registro", methods=['GET', 'POST'])
def registro(): 

	form = FormRegistro()

	
	if form.validate_on_submit():
		valores = loja(nome=form.nome.data, telefone=form.telefone.data, cnpj=form.cnpj.data, 
			email=form.email.data, senha=form.senha.data)

		db.session.add(valores)

		db.session.commit()
		flash(f'Cadastro efetuado com sucesso. Você pode agora se logar {form.nome.data}!', 'success')
		return redirect(url_for('login'))

	return render_template('registro.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    form = FormLogin()
    
    if current_user.is_authenticated: 
        
        return redirect(url_for('sistema'))

    if form.validate_on_submit():
        query = loja.query.filter_by(email=form.email.data).first()
        if query and query.senha == form.senha.data:
            login_user(query)
            #flash(f'Login efetuado com sucesso.', 'success')
            return redirect(url_for('sistema'))
        else:
            print(form.errors)          
            flash('Login inválido.', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/loginadmin", methods=['GET', 'POST'])
def loginadmin():

    form = LoginAdmin()

    if current_user.is_authenticated:
        
        return redirect(url_for('sistema'))
    
    if form.validate_on_submit():
        query = administrador.query.filter_by(email=form.email.data).first()
        if query and query.senha == form.senha.data:
            login_user(query)
            flash("Login efetuado com sucesso.")
            return redirect(url_for('sistema'))
        else:
            print(form.errors)          
            flash("Login inválido.", "text-danger")
    return render_template('loginadmin.html', title='login', form=form)




@app.route("/visualizar/<ver_item>", methods=['GET', 'POST'])
def visualizar(ver_item):

	query = desc.query.get_or_404(ver_item)
	
	return render_template('visualizar.html', query=query)

@app.route("/sistema/<item_id>/editar", methods=['GET', 'POST'])
def editar(item_id):
	
	query_editar = desc.query.get_or_404(item_id)

	print('TIPO NOMELOJA',type(query_editar.nomeloja))
	print('TIPO DESC',type(query_editar.descricao))
	
	formulario = FormSistema()
	
	if formulario.validate_on_submit():

		query_editar.descricao = formulario.descricao.data
		query_editar.quantidade = formulario.quantidade.data
		query_editar.valor = formulario.valor.data
		query_editar.dia = formulario.dia.data
		query_editar.nomeloja = formulario.nomeloja.data


		db.session.commit()
		flash(f'Editado com sucesso!', 'success')
		
		return redirect(url_for('sistema', item_id=query_editar._id))

	elif request.method == 'GET':

		formulario.descricao.data = query_editar.descricao
		formulario.quantidade.data = query_editar.quantidade
		formulario.valor.data = query_editar.valor
		formulario.dia.data = query_editar.dia
		formulario.nomeloja.data = query_editar.nomeloja

		return render_template('editar.html', formulario=formulario, query_editar=query_editar)


@app.route("/sistema/<excluir_id>/excluir", methods=['POST'])
@login_required
def excluir(excluir_id):

	query_excluir = desc.query.get_or_404(excluir_id)
	
	db.session.delete(query_excluir)
	db.session.commit()
	flash('Apagado com sucesso!', 'success')
	return redirect(url_for('sistema', query_excluir = query_excluir))
	

@app.route("/minhaconta", methods=['GET', 'POST'])
@login_required
def minhaconta():

	form = FormRegistro()
	
	if form.validate_on_submit():
		current_user.nome = form.nome.data
		current_user.telefone = form.telefone.data
		current_user.cnpj = form.cnpj.data
		current_user.email = form.email.data
		current_user.senha = form.senha.data
		current_user.confirma_senha = form.confirma_senha.data
		db.session.commit()
		flash('Sua conta foi atualizada com sucesso.', 'success')
		return redirect(url_for('sistema'))

	elif request.method == 'GET':
		form.nome.data = current_user.nome
		form.telefone.data = current_user.telefone
		form.cnpj.data = current_user.cnpj
		form.email.data = current_user.email
		form.senha.data = current_user.senha
		

	return render_template('minhaconta.html', title='Minha Conta', form=form)



@app.route("/sair")
def sair():
    logout_user()
    return redirect(url_for('home'))
