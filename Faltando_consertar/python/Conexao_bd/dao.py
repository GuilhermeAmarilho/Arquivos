class DepartamentoDao:
    def __init__(self):
        self._dados_con = "dbname=python host=localhost user=postgres password=postgres port=5432"
    def listar(self):
        vet = []
        try:
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM departamento")
                #cur.execute("SELECT * FROM departamento where coddepartamento = %s", [4]) #faz o select
                #cur.execute("SELECT * FROM departamento where coddepartamento = %(coddepartmaento)s", {'coddepartamento':4})
                #cur.mogrify("select * from departamento where coddepartamento = %s", [5]) retorna string do select
                #for linha in cur.fetchall():
                #    print (linha.__repr__())
                #    vet.append(departamento(cod=int(linha[0]), nome = linha[1]))
                cur.close()
        except BaseException:
            print("treta")
        return vet

a= DepartamentoDao()
a.listar()
