from aluno import Aluno
class AlunoDAO:
    def __init__(self, conn):
        self.conn = conn
    def buscar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, email FROM aluno")
        resultados = cursor.fetchall()
        alunos = [Aluno(id=row[0], nome=row[1], email=row[2]) for row in resultados]
        cursor.close()
        return alunos
    def inserir(self, aluno):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO aluno (nome, email) VALUES (%s, %s) RETURNING id", (aluno.nome, aluno.email))
        aluno.id = cursor.fetchone()[0]
        self.conn.commit()
        cursor.close()
        return aluno
    def remover(self, aluno_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM aluno WHERE id = %s", (aluno_id,))
        self.conn.commit()
        cursor.close()
    def atualizar(self, aluno_id, novo_nome=None, novo_email=None):
        cursor = self.conn.cursor()
        campos = []
        valores = []
        if novo_nome:
            campos.append("nome = %s")
            valores.append(novo_nome)
        if novo_email:
            campos.append("email = %s")
            valores.append(novo_email)
        if campos:
            query = f"UPDATE aluno SET {', '.join(campos)} WHERE id = %s"
            valores.append(aluno_id)
            cursor.execute(query, valores)
            self.conn.commit()
        cursor.close()