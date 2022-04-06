# from app.models.classe.usuario import usuario
from app.models.classe.usuario import Usuario
from psycopg2 import connect
from datetime import datetime
from app.models.dao.dao import DAO

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()
    def excluir(self, usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM usuario WHERE login=%s",[usuario.login])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema na exclusão -- exception seguindo para ser tratada")
            raise e
    def buscar(self, login):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * from usuario WHERE login=%s', [login])
                row = cur.fetchone()
                u = Usuario(login=row[0],nome=row[1],altura=row[2],idade=row[3],email=row[4],senha=row[5])
                cur.close()
                return u
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e    
    def listar(self):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM usuario')
                for row in cur.fetchall():
                    vet.append(Usuario(login=row[0],nome=row[1],altura=row[2],idade=row[3],email=row[4],senha=row[5]))
                cur.close()
        except BaseException as e:
            print ("Problema no listar -- exception seguindo para ser tratada")
            raise e    
        return vet
    def inserir(self, usuario):
        params =  [usuario.login, usuario.nome, usuario.altura, usuario.idade, usuario.email, usuario.senha]
        query = "INSERT INTO usuario (login,nome,altura,idade,email,senha) VALUES (%s, %s, %s, %s, %s, md5(%s))"
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def alterar(self, usuario):
        params =  [usuario.nome, usuario.altura, usuario.idade, usuario.email, usuario.senha, usuario.login]
        query = "UPDATE usuario SET nome=%s, altura=%s, idade=%s, email=%s, senha=%s WHERE login=%s"
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no alterar -- exception seguindo para ser tratada")
            raise e
