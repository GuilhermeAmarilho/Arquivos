from datetime import datetime
class Cachorro:
    def __init__(self, nome, raca):
        self._nome = nome
        self._raca = raca
        self._id = ""
    def _set_nome(self,nome):
        self._nome = nome
    def _get_nome(self):
        return str(self._nome)
    nome = property(_get_nome,_set_nome)
    def _set_raca(self,raca):
        self._raca = raca
    def _get_raca(self):
        return str(self._raca)
    raca = property(_get_raca,_set_raca)
    def _set_id(self, id):
        self._id = id
    def _get_id(self):
        return str(self._id)
    id = property(_get_id,_set_id)
    def __str__(self):
        return f'{self.id};{self.nome};{self.raca};'