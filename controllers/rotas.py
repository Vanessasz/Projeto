
from Projeto import app, db #Aqui estou fazendo o importe da instância que eu criei.

#from Projeto.models import database
from Projeto.models.database import Desc, Administrador, Role, UserRoles

from flask import render_template, url_for, flash, redirect, request, abort, send_file, Markup
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import func

from flask_user import current_user, login_required, roles_required, UserManager

from Projeto.controllers.form import FormSistema, FormRegistro, FormLogin, LoginAdmin, SistemaBusca

from flask_login import login_user, login_manager, logout_user

from collections import namedtuple


@app.route("/")

@app.route("/home")
def home():
    """ Essa função renderiza a página principal """
    

    return render_template('home.html')

#Rota para o admin
@app.route("/sistema_admin", methods=['GET', 'POST']) 
    #Aqui definimos uma rota ṕara a página
@roles_required('admin')
    # Aqui o usuário só terá acesso ao sistema se estiver feito login
def sistema_admin():
    

    lista_teste = []

    for u in db.session.query(Administrador).all():
       
       lista_teste.append(str(u._id) + '  ' + u.nome)


    ##########################################################
    '''
    lojas_cadastradas = db.session.query(Administrador.nome).all()
    
    lista_loja = []

    lista_loja = [x[0] for x in lojas_cadastradas]

    print('LISTA LOJA',lista_loja)
    '''
    ##########################################################3

    form = FormSistema()
    
    if form.validate_on_submit():

        campos = request.form.get('seletor_loja')

        lista_extaida = []

        lista_extaida = campos.split('  ')
        
        valores = Desc(descricao=form.descricao.data, quantidade=form.quantidade.data, valor=form.valor.data, 
                        dia=form.dia.data, nomeloja=lista_extaida[1], descricoes_id=int(lista_extaida[0]))  

        db.session.add(valores)
        #session usando os atributos
        db.session.commit()
        #salvando os dados definitivo no banco de dados
        
        flash(f'Adicionado com sucesso!', 'success')
        print(valores)

        return redirect(url_for('sistema_admin'))   

    #lojas_cadastradas = db.session.query(Role.name=='user')
    #lojas_cadastradas = db.session.query(Administrador).filter_by(nomeloja)

    #Defini uma função para essa página

    """ Instanciei meu formulário para poder usar """
    #form_busca = SistemaBusca()
    #busca

    #Query para as somas
    soma_itens = db.session.query(func.sum(Desc.quantidade)).first()
    soma_valores = db.session.query(func.sum(Desc.valor)).first()

    soma_total = db.session.query(func.sum(Desc.valor * Desc.quantidade)).first()#filter_by(descricoes_id=current_user._id)
    
    valores = 0

    query = db.session.query(Desc).all()
    #query = Desc.query.filter_by(descricoes_id=current_user._id)

    #nomeloja = current_user._id

    return render_template('sistema_admin.html',form=form, query=query, soma_itens=soma_itens[0], soma_valores=soma_valores[0],
                             soma_total=soma_total[0], lista_teste=lista_teste) 


#Rota para as lojas
@app.route("/sistema", methods=['GET', 'POST']) 
    #Aqui definimos uma rota ṕara a página
@login_required
    # Aqui o usuário só terá acesso ao sistema se estiver feito login
def sistema(): 
    #Defini uma função para essa página
    form = FormSistema()
    """ Instanciei meu formulário para poder usar """
    #form_busca = SistemaBusca()
    #busca

    #Query para as somas
    soma_itens = db.session.query(func.sum(Desc.quantidade)).filter_by(descricoes_id=current_user._id)
    soma_itens_conversor = str(soma_itens[0])
    soma_itens_conversor = soma_itens_conversor[1:-2]
    soma_itens_final = int(soma_itens_conversor)



    soma_valores = db.session.query(func.sum(Desc.valor)).filter_by(descricoes_id=current_user._id)

    soma_total = db.session.query(func.sum(Desc.valor * Desc.quantidade)).filter_by(descricoes_id=current_user._id)#filter_by(descricoes_id=current_user._id)   
    soma_total_conversor  = str(soma_total[0])
    soma_total_conversor = soma_total_conversor[1:-2]
    soma_total_final = float(soma_total_conversor)

    valores = 0

    query = Desc.query.filter_by(descricoes_id=current_user._id)


    return render_template('sistema.html', form=form, query=query, soma_itens_final=soma_itens_final, 
                                            soma_valores=soma_valores[0], soma_total_final=soma_total_final) 


@app.route("/registro", methods=['GET', 'POST'])
def registro():     

    form = FormRegistro()

    
    if form.validate_on_submit():
        valores = Administrador(nome=form.nome.data, email=form.email.data, senha=form.senha.data)

        db.session.add(valores)
        regra = Role(name='user')
        #regra = UserRoles(role_id=2)
        valores.roles.append(regra)

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
        query = Administrador.query.filter_by(email=form.email.data).first()
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
        
        return redirect(url_for('sistema_admin'))
    
    if form.validate_on_submit():
        query = Administrador.query.filter_by(email=form.email.data).first()
        
        if query and query.senha == form.senha.data:
            login_user(query)
            flash("Login efetuado com sucesso.", 'success')
            return redirect(url_for('sistema_admin'))
        else:
            print(form.errors)          
            flash("Login inválido.", "text-danger")

    return render_template('loginadmin.html', title='login', form=form)


@app.route("/visualizar/<ver_item>", methods=['GET', 'POST'])
def visualizar(ver_item):

    #query = desc.query.get_or_404(ver_item).filter_by(lojas.descricoes_id)

    query = db.session.query(ver_item).filter_by(Desc.descricoes_id)

    soma_itens = db.session.query(func.sum(Desc.quantidade)).first()


    loja = db.session.query(func.sum(Desc.valor)).filter_by(Desc.nomeloja)
    #filter_by(descricoes_id=current_user._id)

    #loja = des.query.filter_by(desc.nomeloja).first()
    
    return render_template('visualizar.html', query=query, loja=loja)


@app.route("/sistema/<item_id>/editar", methods=['GET', 'POST'])
def editar(item_id):
    
    query_editar = Desc.query.get_or_404(item_id)

    form = FormSistema()
    
    if form.validate_on_submit():

        query_editar.descricao = form.descricao.data
        query_editar.quantidade = form.quantidade.data
        query_editar.valor = form.valor.data
        query_editar.dia = form.dia.data
        query_editar.nomeloja = form.nomeloja.data


        db.session.commit()
        flash(f'Editado com sucesso!', 'success')
        
        return redirect(url_for('sistema', item_id=query_editar._id))

    elif request.method == 'GET':

        form.descricao.data = query_editar.descricao
        form.quantidade.data = query_editar.quantidade
        form.valor.data = query_editar.valor
        form.dia.data = query_editar.dia
        form.nomeloja.data = query_editar.nomeloja

        return render_template('editar.html', form=form, query_editar=query_editar)


@app.route("/sistema/<excluir_id>/excluir", methods=['POST'])
@login_required
def excluir(excluir_id):

    query_excluir = Desc.query.get_or_404(excluir_id)
    
    db.session.delete(query_excluir)
    db.session.commit()
    flash('Apagado com sucesso!', 'success')
    return redirect(url_for('sistema', query_excluir = query_excluir))

@app.route("/sistema/<vender_id>/venda", methods=['GET', 'POST'])
@login_required
def vender(vender_id):

    form = FormSistema()

    query_venda = Desc.query.get_or_404(vender_id)

    #query_venda = Desc.query.get_or_404(vender_id)

    if form.validate_on_submit():
        valor = 0
        
        valor = int(form.quantidade.data)

        valor_a = int(query_venda.quantidade)

        query_venda.quantidade =  valor_a - valor
        

        db.session.commit()
        
        flash('Vendido com sucesso!', 'success')
        
        return redirect(url_for('sistema')) 

    elif request.method == 'GET':

        form.descricao.data = query_venda.descricao
        #form.quantidade.data = query_editar.quantidade
        form.valor.data = query_venda.valor
        form.dia.data = query_venda.dia
        form.nomeloja.data = query_venda.nomeloja


    return render_template('venda.html', form=form, query_venda=query_venda)

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

'''
  {% if current_user.has_roles('admin') %}
                 <li class="nav-item active">
                    
            <a class="nav-link" href="{{ url_for('sistema_admin') }}">Sistema</a>
                </li> 
                    {% elif current_user.has_roles('user')  %}
                <li class="nav-item active">

            <a class="nav-link" href="{{ url_for('sistema') }}">Sistema</a>
                </li>
                {% else %}

                {% endif %}




'''