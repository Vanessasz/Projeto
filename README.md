# Jóia Lar 

### Pensando em resolver um problema do cotidiano, o qual será meu TCC do curso de Análise e Desenvolvimento de Sistemas.

O software está sendo desenvolvido usando a linguagem de programação **Python** e o framework web _Flask_. Foi criado uma pasta com o nome de Estudo e lá dentro que se encontra o código do software ao qual foi dado o nome de _Projeto_, essa é outra pasta. Para organizar todo esse conteúdo foi usado uma máquina virtual com o nome de venv para usar essa máquina virtual temos que dar esse comando se o virtualenv ainda não tiver sido instalado **pip install virtualenv** e depois a versão do python que eu quero usar por exemplo **virtualenv -p python3.6 venv** terminado essa instalação é hora de ativarmos a nossa máquina virtual e darmos o nome para ela, nesse caso eu dei o nome de venv que é um padrão, mas poderia ter sido qualquer nome. **virtualenv venv** pronto está dado um nome a ela e com isso essa pasta venv foi criada. ![alternate text](./venv.png "venv") Toda vez que eu for trabalhar nesse projeto eu preciso ativar essa máquina virtual. Para isso eu abro um terminal entro dentro da pasta Estudo depois Projeto, venv e dou esse comando source bin/activate digito cd .. para sair da pasta venv e voltar para a pasta Projeto, a onde se encontra todo o código do meu software. Feito isso digito no terminal python run.py e abrirá uma página home. 

```

@app.route("/") #Aqui definimos uma rota para a página
@app.route("/home") #Tanto / como /home será direcionado para home
def home(): 
	return render_template('home.html') #Essa página irá retornar o que estiver dentro do meu aquivo home.html

```

