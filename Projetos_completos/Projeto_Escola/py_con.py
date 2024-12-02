import psycopg2
try:
    dados = "dbname=postgres host=localhost user=postgres password=1234 port=5432"
    conn = psycopg2.connect(dados)
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE aluno (id SERIAL PRIMARY KEY, nome VARCHAR(300) NOT NULL, email VARCHAR(300) UNIQUE NOT NULL);")
        cursor.close()
        print("A tabela Aluno já existe e está pronta para uso!")
    except:
        print("A tabela Aluno foi criada no banco de dados!")
except:
    print("Nao foi")