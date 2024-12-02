from alunoDAO import AlunoDAO
from aluno import Aluno
from py_con import *
dao = AlunoDAO(conn)
print("=== Testando o AlunoDAO ===")
aluno1 = Aluno(nome="João da Silva", email="joao.silva@example.com")
aluno2 = Aluno(nome="Maria Oliveira", email="maria.oliveira@example.com")
aluno1 = dao.inserir(aluno1)
aluno2 = dao.inserir(aluno2)
alunos = dao.buscar_todos()
print("Alunos no banco de dados:")
for aluno in alunos:
    print(f"ID: {aluno.id}, Nome: {aluno.nome}, Email: {aluno.email}")
dao.atualizar(aluno1.id, novo_nome="João Atualizado", novo_email="joao.novo@example.com")
print(f"Aluno com ID {aluno1.id} atualizado.")
alunos = dao.buscar_todos()
for aluno in alunos:
    print(f"ID: {aluno.id}, Nome: {aluno.nome}, Email: {aluno.email}")
dao.remover(aluno2.id)
print(f"Aluno ID: {aluno2.id} removido.")
alunos = dao.buscar_todos()
for aluno in alunos:
    print(f"ID: {aluno.id}, Nome: {aluno.nome}, Email: {aluno.email}")
conn.close()