import psycopg2

dados = "dbname=postgres host=localhost user=postgres password=1234 port=5432"
con = psycopg2.connect(dados)
cursor = con.cursor()

cursor.execute("SELECT * FROM aluno;")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

cursor.close()
con.close()