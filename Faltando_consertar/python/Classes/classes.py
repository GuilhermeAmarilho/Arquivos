class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    def _getnome(self):
        return self._nome
    def _setnome(self, nome):
        self._nome = nome
    nome = property(_getnome,_setnome)
    def __str__(self):
        return "O seu nome é %s" %(self._nome)
    
class Matricula:
    def __init__(self, matricula):
        self._matricula = matricula
    def _getmatricula(self):
        return self._matricula
    def _setmatricula(self, matricula):
        self._matricula = matricula
    matricula = property(_getmatricula,_setmatricula)


a = Aluno('gui',1234)

#def sao as funções
#self é como o this ($this->nome())

#ex completo

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    nome = property(_get_nome,_set_nome)

class Arma:
    def __init__(self, nome):
        self._tipo = nome
    def _getarma(self):
        return self._tipo
    def _setarma(self,tipo):
        self._tipo = tipo
    arma = property(_getarma,_setarma)

class Soldado(Pessoa, Arma):
    def __ini(self):
        Pessoa.__init__(self,nome)
        Arma.__init__(Self,nome,preco)