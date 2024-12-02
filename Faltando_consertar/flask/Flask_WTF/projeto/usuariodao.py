from usuario import Usuario
from psycopg2 import connect
from dao import DAO
import hashlib
class UsuarioDao(DAO):
    def __init__(self):
        super().__init__()
    def excluir(self, usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM usuario WHERE cod=%s",[usuario.cod])
                conn.commit()
                cur.close()
                usuario.cod = None
        except BaseException as e:
            print ("Problema na exclusão -- exception seguindo para ser tratada")
            raise e
    def inserir(self, usuario):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                usuario.senha = hashlib.md5(usuario.senha.encode()).hexdigest()
                cur.execute('INSERT INTO usuario (nome, login, senha) VALUES (%s,%s,%s)',[usuario.nome,usuario.login,usuario.senha])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no insert -- exception seguindo para ser tratada")
            raise e
    def buscar(self, usuario):
        # try:
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            usuario.senha = hashlib.md5(usuario.senha.encode()).hexdigest()
            cur.execute('SELECT * FROM usuario where login = %s and senha = %s',[usuario.login,usuario.senha])
            return cur.fetchone()
            cur.close()