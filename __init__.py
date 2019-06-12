import smtplib
from flask import Flask # Estou importando o framework Flask para poder utiliza-ló em meu projeto.
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__) # Todo Flask está contido aqui dentro.

app.config['SECRET_KEY'] = '833d1a8d188e94730cb6af5b9fcc9786'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodedados.db'

#if __name__ == "__main__":
	#app.run() # O usuario está executando o arquivo principal? se sim 
	# o flask só dá o run se esse for o arquivo principal de execução. 
	# já estamos com uma instância do flask pronta.

db = SQLAlchemy(app) # Uma instância do SQLALchemy, ou seja uma classe.
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' #usa a classe do bootstrap para exibir mensagem de "login necessario'"


 



from Projeto.controllers import rotas #Preciso especificar o caminho todo para o Flask entender.


