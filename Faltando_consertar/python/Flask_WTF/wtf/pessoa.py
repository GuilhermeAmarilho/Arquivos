import hashlib
class Pessoa:
    def __init__(self,**kwargs):
        if(kwargs.get("codigo")): self._codigo = kwargs["codigo"]
        if(kwargs.get("nome")): self._nome = kwargs["nome"]
        if(kwargs.get("salario")): self._salario = kwargs["salario"]
        if(kwargs.get("sexo")): self._sexo = kwargs["sexo"]
        if(kwargs.get("num_filhos")): self._num_filhos = kwargs["num_filhos"]
        if(kwargs.get("biografia")): self._biografia = kwargs["biografia"]
        if(kwargs.get("senha")): self._senha = hashlib.md5((kwargs["senha"]).encode()).hexdigest()
        if(kwargs.get("login")): self._login = kwargs["login"] 
    def __str__(self):
        return "Código: {}, Nome: {}, Salario: {}, Sexo: {}, Nº de filhos: {}, Biografia: {}, Senha: {}, Login: {}".format(self._codigo,self._nome,self._salario,self._sexo,self._num_filhos,self._biografia,self._senha,self._login)
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,codigo):
        self._codigo = codigo
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,salario):
        self._salario = salario
    @property
    def sexo(self):
        return self._sexo
    @sexo.setter
    def sexo(self,sexo):
        self._sexo = sexo
    @property
    def num_filhos(self):
        return self._num_filhos
    @num_filhos.setter
    def num_filhos(self,num_filhos):
        self._num_filhos = num_filhos
    @property
    def biografia(self):
        return self._biografia
    @biografia.setter
    def biografia(self,biografia):
        self._biografia = biografia
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self,login):
        self._login = login
    def persistido(self):
        return hasattr(self,"_codigo") and self.codigo!=None 