class CachorroDAO:
    def inserir(self,obj):
        valor = (obj.__str__()).split(',')
        lista = ((open('arquivo.txt', 'r', encoding="utf8")).read())
        li = lista.split('\n')
        x = 0
        if (len(lista.split('\n'))<2):
            obj.id = 1
            lista+=("{},{},{},{}\n".format(obj.nome,obj.raca,obj.nascimento,obj.id))
            postar = open('arquivo.txt', 'w', encoding="utf8")
            postar.writelines(lista)
            postar.close()
            print('Cachorro adicionado com sucesso')
        else:
            for n in li:
                a = n.split(',')
                if(a != ''):
                    if(a[0] == valor[0] and a[1] == valor[1] and a[2] == valor[2]):
                        x = 1  
            if(x==0):
                obj.id = int(li[len(li)-2].split(',')[3]) + 1
                lista+=("{},{},{},{}\n".format(obj.nome,obj.raca,obj.nascimento,obj.id))
                postar = open('arquivo.txt', 'w', encoding="utf8")
                postar.writelines(lista)
                postar.close()
                print('Cachorro adicionado com sucesso')
            else:
                print('Cachorro ja cadastrado')
    def deletar(self,id):
        lista = ((open('arquivo.txt', 'r', encoding="utf8")).read()).split('\n')
        b = 0 
        c = 0
        for n in lista: 
            if(n!=''):
                a = n.split(',')[3]
                if(int(id) == int(a)):
                    c = 1
                    break
                b+=1
        if(c==1):
            lista.pop(b)
            lista = '\n'.join(lista)
            postar = open('arquivo.txt', 'w', encoding="utf8")
            postar.writelines(lista)
            postar.close()
            print ('Cachorro eliminado com sucesso')
        else:
            print ('Id invalido')
    def buscar(self,id):
        lista = ((open('arquivo.txt', 'r', encoding="utf8")).read()).split('\n')
        b = 0 
        c = 0
        for n in lista: 
            if(n!=''):
                a = n.split(',')[3]
                if(int(id) == int(a)):
                    c = 1
                    break
                b+=1
        if(c==1):
            a = lista[b].split(',')
            print ("Nome do cachorro: {}, raça: {}, data de nascimento: {}, id:{}".format(a[0],a[1],a[2],a[3]))
        else:
            print ('Id invalido')
    def alterar(self,obj):
        lista = ((open('arquivo.txt', 'r', encoding="utf8")).read())
        li = lista.split('\n')
        b = 0 
        c = 0
        x = 0
        if (id == ''):
            print("Informe o id!")
        else:
            for n in li: 
                if(n!=''):
                    a = n.split(',')[3]
                    if(int(obj.id) == int(a)):
                        c = 1
                        break
                    b+=1
            if(c==1):    
                for n in li:
                    if(n!=''):
                        a = n.split(',')
                        d = obj.__str__().split(',')
                        if(a[0] == d[0] and a[1] == d[1] and a[2] == d[2]):
                            x = 1
                if(x==0):
                    li[b] = ("{},{},{},{}".format(obj.nome,obj.raca,obj.nascimento,obj.id))
                    lista = '\n'.join(li)
                    postar = open('arquivo.txt', 'w', encoding="utf8")
                    postar.writelines(lista)
                    postar.close()
                    print('Alteração feita com sucesso')
                else:
                    print('Esta combinação de nome e raça já está cadastrado')
            else:
                print ('Id invalido')
    def listar(self):
        lista = ((open('arquivo.txt', 'r', encoding="utf8")).read()).split('\n')
        print("Nome, Raça, Data de nascimento, ID:")
        for n in lista: 
            if(n!=""):
                a = n.split(',')
                print("{}, {}, {}, {}".format(a[0],a[1],a[2],a[3]))