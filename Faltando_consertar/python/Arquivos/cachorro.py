from datetime import datetime
class Cachorro:
    def __init__(self, nome, raca, nascimento):
        self._nome = nome
        self._raca = raca
        self._nascimento = format(datetime.strptime(str(nascimento),'%d-%m-%Y'), '%d-%m-%Y')
        self._id = ""
    def _set_nome(self,nome):
        self._nome = nome
    def _get_nome(self):
        return self._nome
    nome = property(_get_nome,_set_nome)
    def _set_raca(self,raca):
        self._raca = raca
    def _get_raca(self):
        return self._raca
    raca = property(_get_raca,_set_raca)
    def _set_id(self,id):
        self._id = id
    def _get_id(self):
        return self._id
    id = property(_get_id,_set_id)
    def _set_nascimento(self,nascimento):
        self._nascimento = nascimento
    def _get_nascimento(self):
        return self._nascimento
    nascimento = property(_get_nascimento,_set_nascimento)
    def __str__(self):
        return "{},{},{}".format(self._nome,self._raca,self._nascimento)