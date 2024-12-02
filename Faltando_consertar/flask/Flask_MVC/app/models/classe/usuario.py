class Usuario:
    def __init__(self,**kwargs):
        if(kwargs.get("nome")): self._nome = kwargs["nome"]
        if(kwargs.get("login")): self._login = kwargs["login"]
        if(kwargs.get("altura")): self._altura = kwargs["altura"]
        if(kwargs.get("idade")): self._idade = kwargs["idade"]
        if(kwargs.get("email")): self._email = kwargs["email"]
        if(kwargs.get("senha")): self._senha = kwargs["senha"]
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self,altura):
        self._altura = altura
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,idade):
        self._idade = idade
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self,login):
        self._login = login
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email = email
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha
    def __str__(self):
        return "nome: {}, login: {}, altura: {}, idade: {}, email: {}, senha: {}".format(self._nome,self._login,self._altura,self._idade,self._email,self._senha)
