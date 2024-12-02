from pessoa import Pessoa
from psycopg2 import connect
from server import DAO

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__()
    def excluir(self, pessoa):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM pessoa WHERE codigo = %s",[pessoa.codigo])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def buscar(self, cod):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM Pessoa WHERE codigo = %s', [cod])
                row = cur.fetchone()
                pessoa = Pessoa(codigo=row[0],nome=row[1],salario=row[2],sexo=row[3],num_filhos=row[4],biografia=row[5],senha=row[6],login=row[7])
                cur.close()
                return pessoa
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e     
    def listar(self):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM pessoa')
                for row in cur.fetchall():
                    vet.append(Pessoa(codigo=row[0],nome=row[1],salario=row[2],sexo=row[3],num_filhos=row[4],biografia=row[5],senha=row[6],login=row[7]))
                cur.close()
        except BaseException as e:
            print ("Problema no listar -- exception seguindo para ser tratada")
            raise e    
        return vet
    def inserir(self, pessoa):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("insert into pessoa(nome,salario,sexo,num_filhos,biografia,senha,login) values (%s, %s, %s, %s, %s, %s, %s)",[pessoa.nome,pessoa.salario,pessoa.sexo,pessoa.num_filhos,pessoa.biografia,pessoa.senha,pessoa.login])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def alterar(self, pessoa):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("UPDATE pessoa SET nome=%s, salario=%s, sexo=%s, num_filhos=%s, biografia=%s, senha=%s, login=%s WHERE codigo = %s", [pessoa.nome,pessoa.salario,pessoa.sexo,pessoa.num_filhos,pessoa.biografia,pessoa.senha,pessoa.login,pessoa.codigo])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no alterar -- exception seguindo para ser tratada")
            raise e
    def salvar(self, pessoa):
        if pessoa.persistido():
            self.alterar(pessoa)
        else:
            self.inserir(pessoa)
