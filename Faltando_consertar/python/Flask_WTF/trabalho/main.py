from flask import Flask,url_for,session,render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from aluno import Aluno
from dao import AlunoDAO

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "a secret key you won't forget"
app.config["BABEL_DEFAULT_LOCALE"] = "pt"	
babel = Babel(app)

@app.route('/')
def lista():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('lista.html',lista = lista)
@app.route('/deletar/<cod>')
def deletar(cod):
    dao = AlunoDAO()
    pessoa = Aluno(codigo=cod)
    dao.excluir(pessoa)
    return redirect('/')
    
if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True)
