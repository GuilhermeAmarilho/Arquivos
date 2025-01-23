from flask import Flask, render_template, request

app = Flask(__name__)

# Caso queira adicionar arquivos estáticos
# url_for('static', filename='style.css')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/loginForm')
def loginForm():
    return render_template('login.html')

@app.route('/cadastroLogin')
def cadastroLogin():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        return render_template('show_data.html', username=username, email=email, password=password)
    # Renderiza o formulário caso seja uma requisição GET
    return render_template('cadastro.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)