# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import redirect, url_for, render_template
from app.models.dao.usuariodao import UsuarioDAO

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/')
def index():
    a = UsuarioDAO()
    b = a.listar()
    return render_template('index.html', lista = b)
@usuario_bp.route('/outro')
def bye():
    a = Usuario(nome='guilherme',login='amarilho',altura=1.82,idade=18,email='guiamarilho1@outlook.com',senha='amarilho')
    return a.login