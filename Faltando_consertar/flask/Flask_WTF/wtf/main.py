from flask import Flask,url_for,flash,session,render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from form import formulario
from pessoa import Pessoa
from dao import PessoaDAO
app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "a secret key you won't forget"
app.config["BABEL_DEFAULT_LOCALE"] = "pt"	
babel = Babel(app)

@app.route('/')
def lista():
    dao = PessoaDAO()
    lista = dao.listar()
    return render_template('lista.html',lista = lista)
@app.route('/deletar/<cod>')
def deletar(cod):
    dao = PessoaDAO()
    pessoa = Pessoa(codigo=cod)
    dao.excluir(pessoa)
    return redirect(url_for('lista'))

@app.route('/alterar',methods=['GET','POST'])
def alterar():
    if request.method == "POST":
        cod = request.form['cod']
    else:
        cod = request.args['cod']
    form = formulario()
    if cod == 'None':
        pessoa = None
        cod = None
    else:
        dao = PessoaDAO()
        pessoa = dao.buscar(cod)
        form.sexo.data = pessoa.sexo
        form.biografia.data = pessoa.biografia
        cod = int(cod)
    if form.validate_on_submit():
        dao = PessoaDAO()
        pessoa = Pessoa(codigo=cod,nome=request.form['nome'],salario=request.form['salario'],sexo=request.form['sexo'],num_filhos=request.form['num_filhos'],biografia=request.form['biografia'],senha=request.form['senha'],login=request.form['login'])
        dao.salvar(pessoa)
        return redirect(url_for('lista'))

    else:
        return render_template('formulario.html',form=form,pessoa=pessoa)

    return redirect(url_for('lista'))
if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True)
