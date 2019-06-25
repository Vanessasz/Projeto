from datetime import datetime


from Projeto import app, db, login_manager

from flask_user import UserMixin

from flask_login import login_user

from flask_user import login_required, roles_required, UserManager, SQLAlchemyAdapter


@login_manager.user_loader
def load_user(descricoes_id):
	return Administrador.query.get(int(descricoes_id))

class Administrador(db.Model, UserMixin):
	__tablename__ = "admin"

	def get_id(self):
		return (self._id)

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(45), unique=True, nullable=False)
	senha = db.Column(db.String(45), nullable=False)
	roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))


	def __repr__(self):
		return f"admin('{self.nome}', '{self.email}', '{self.email}')"

    # Relationships
    
#Classes que registram as regras para os usuarios
#Administrador ou Usuário comum
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=False)

# Define the UserRoles data model
class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('admin._id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

db_adapter = SQLAlchemyAdapter(db,  Administrador)
user_manager = UserManager(db_adapter, app)


class Desc(db.Model):
	__tablename__= "descricoes"

	def get_id(self):
		return (self._id)

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	descricao = db.Column(db.String, nullable=False)
	quantidade = db.Column(db.Integer, nullable=False)
	valor = db.Column(db.Float, nullable=False)
	dia = db.Column(db.String, nullable=False) 
	nomeloja = db.Column(db.String, nullable=True)
	
	descricoes_id = db.Column(db.Integer, db.ForeignKey('admin._id'), nullable=False) # Chave estrangeira
	
	def __repr__(self):
		return f"descricoes('{self.descricao}', '{self.quantidade}','{self.valor}','{self.dia}','{self.nomeloja}')"