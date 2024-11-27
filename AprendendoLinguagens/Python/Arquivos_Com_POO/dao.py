import os
def pegar_path():
    file_path = os.path.abspath(__file__).lower().split('\\')
    file_path.pop()
    return '\\'.join(file_path) + '\\' + 'arquivo.txt'
class CachorroDAO:
    def __init__(self):
        try:
            open(pegar_path(), 'x', encoding="utf8")
        except:
            pass
    def inserir(self, obj):
        obj._set_id(self.pegarUltimoID())
        lista = self.listar()

        lista.append(
            obj.__str__()+'\n'
        )
        if self.gravarDados(lista):
            return True
        else:
            return False
    def deletar(self,id):
        lista = self.listar()
        i = 0
        verify = False
        while i < len(lista):
            if lista[i].split(';')[0] == str(id):
                lista[i] = ''
                verify = True
            i += 1
            self.gravarDados(lista)
        return verify
    def buscar(self,id):
        lista = self.listar()
        for item in lista: 
            if item.split(';')[0] == str(id):
                return item
        return ''
    def alterar(self,obj):
        lista = self.listar()
        i = 0
        verify = False
        while i < len(lista):
            if lista[i].split(';')[0] == obj._get_id():
                lista[i] = obj.__str__()+'\n'
                verify = True
            i += 1
            self.gravarDados(lista)
        return verify
    def pegarUltimoID(self):
        try:
            atual = self.listar().pop().split(';')[0]
            return int(atual) + 1
        except:
            return 1
    def listar(self):
        arquivo = open(pegar_path(), 'r', encoding="utf8")
        lista = arquivo.readlines()
        arquivo.close()
        return lista
    def gravarDados(self, lista):
        postar = open(pegar_path(), 'w', encoding="utf8")
        for item in lista:
            postar.write(item)
        postar.close()