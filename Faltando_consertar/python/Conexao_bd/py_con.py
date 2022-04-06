import psycopg2
try:
    dados = "dbname=python host=localhost user=postgres password=postgres port=5432"
    con = psycopg2.connect(dados)
except:
    print("Nao foi")
