import psycopg2

dados = "dbname=python host=localhost user=postgres password=postgres port=5432"
con = psycopg2.connect(dados)
cur = con.cursor()


cur.execute("insert into departamento (nome) values (%s)",["lucas gordo ruim"])

cur.execute("update departamento set nome = %s where id = %s",["guguguugug",3])

cur.execute("delete from departamento where id = %s",[13])

cur.execute("select * from departamento where id = %s",[1])
a = cur.fetchone()
print(a)
con.commit() # posta as alterações


cur.execute("select * from departamento")
for lista in cur.fetchall():
    print(lista)


cur.close()