from usuariodao import UsuarioDao
from usuario import Usuario
from ideiadao import IdeiaDao
from ideia import Ideia
from flask import Flask, request, url_for, redirect, render_template, session
app = Flask(__name__)
@app.route('/')
def index():
    try:
        aaaa = session['senha']
        return redirect('/lista')
    except:
        return render_template('login.html')
@app.route('/login',methods = ['POST', 'GET'])
def login():
    dao = UsuarioDao() 
    login = request.form["login"]
    senha = request.form["senha"]
    user = Usuario(login=login,senha=senha)
    u = dao.buscar(user)
    if(u == None):
        return render_template('login.html')
    else:
        session['nome'] = u[1]
        session['login'] = u[2]
        session['cod'] = u[0]
        session['senha'] = u[3]
        return redirect('lista')
@app.route('/logout')
def logout():
    session.pop('nome')
    session.pop('senha')
    session.pop('login')
    return render_template('login.html')
@app.route('/lista')
def lista():
    try: 
        aaaa = session['senha']
        dao = IdeiaDao()
        lis = dao.listar(100,0)
        return render_template('lista.html',ideia = lis)
    except:
        return redirect('/')
@app.route('/inserir')
def forminserir():
    try: 
        aaaa = session['senha']
        return render_template('inserir.html')
    except:
        return redirect('/')
@app.route('/inserir',methods = ['POST', 'GET'])
def inserir():
    try: 
        aaaa = session['senha']
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        user = Usuario(cod=session['cod'])
        ideia = Ideia(titulo=titulo,descricao=descricao,usuario=user)
        dao = IdeiaDao()
        dao.inserir(ideia)
        return redirect('lista')
    except:
        return redirect('/')
@app.route('/sobre/<cod>')
def sobre(cod):
    try: 
        aaaa = session['senha']
        dao = IdeiaDao()
        lis = dao.buscar(int(cod))
        return render_template('sobre.html',lis = lis)
    except:
        return redirect('/')
@app.route('/deletar/<cod>')
def deletar(cod):
    try: 
        aaaa = session['senha']
        dao = IdeiaDao()
        lis = dao.buscar(int(cod))
        dao.excluir(lis)
        return redirect('/lista')
    except:
        return redirect('/')
@app.route('/alterar/<cod>')
def alterar(cod):
    try: 
        aaaa = session['senha']
        dao = IdeiaDao()
        lis = dao.buscar(int(cod))
        return render_template('alterar.html', lis = lis)
    except:
        return redirect('/')
@app.route('/update',methods = ['POST', 'GET'])
def update():
    try: 
        aaaa = session['senha']
        cod = request.form["cod"]
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        dao = IdeiaDao()
        ideia = dao.buscar(cod)
        ideia.titulo = titulo
        ideia.descricao = descricao
        dao.alterar(ideia)
        return redirect('/lista')
    except:
        return redirect('/')
def main():
    app.secret_key = 'string'
    app.env = 'development'
    app.run(debug=True, port=4000)
if __name__ == "__main__":
    main()