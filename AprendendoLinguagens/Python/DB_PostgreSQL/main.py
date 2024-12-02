import psycopg2

dados = "dbname=postgres host=localhost user=postgres password=1234 port=5432"
con = psycopg2.connect(dados)

cursor = con.cursor()

# cursor.execute("SELECT * FROM aluno;")
# resultados = cursor.fetchall()
# for linha in resultados:
#     print(linha)

# Selecione todos os alunos que estejam matriculados em cursos técnicos de nível médio e sejam maiores de idade
# SELECT aluno.nome as nome, aluno.email as email, aluno.cpf as cpf, tipocurso.nome as modalidade FROM aluno, tipocurso WHERE tipocurso.nome = 'técnicos de nível médio' AND EXTRACT(YEAR FROM AGE(aluno.data_nascimento)) > 17;

query = "SELECT aluno.nome as nome, aluno.email as email, aluno.cpf as cpf, tipocurso.nome as modalidade FROM aluno, tipocurso WHERE tipocurso.nome = %s AND EXTRACT(YEAR FROM AGE(aluno.data_nascimento)) > %s;"
params = ('técnicos de nível médio', 17)

# Executar a consulta
cursor.execute(query, params)

# Recuperar os resultados
resultados = cursor.fetchall()

# Exibir os resultados
print("Resultados encontrados:")
for row in resultados:
    print(f"Nome: {row[0]}, Email: {row[1]}, Data de Nascimento: {row[2]}, CPF: {row[3]}")

# Fechar o cursor e a conexão
cursor.close()
con.close()