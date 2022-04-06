from dao import CachorroDAO
from cachorro import Cachorro
from repeticao import r
def roda():
    dao = CachorroDAO()
    a = ""
    while(a!="6"):
        r(0.5)
        print("Controle de animais do guilherme\n1 - adicionar novo cachorro\n2 - excluir cachorro\n3 - alterar cachorro\n4 - listar cachorro\n5 - buscar cachorro\n6 - fechar o programa")
        a = input("informe a requisição: ")
        if (a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6"):
            if(a=="1"):
                r(0.5)
                print("Adicionar novo cachorro\nformato da classe\nnome,raça,data de nascimento(dd-mm-yyyy)")   
                print("\n\n")
                nome = input("Informe o nome do animal: ")
                raca = input("Informe a raça do animal: ")
                data = input("Informe o nascimento do animal(dd-mm-yyyy): ")
                dao.inserir(Cachorro(nome,raca,data))
                r(0.5)
            if(a=="2"):
                r(0.5)
                print("Excluir cachorro")
                print("\n\n")
                id = input("Informe o ID do cachorro a apagar: ")
                dao.deletar(id)
                r(0.5)
            if(a=="3"):
                r(0.5)
                print("Alterar cachorro")
                print("\n\n")
                id = input("Informe o ID do cachorro a alterar: ")
                nome = input("Informe o novo nome do animal: ")
                raca = input("Informe a nova raça do animal: ")
                data = input("Informe o novo nascimento do animal(dd-mm-yyyy): ")
                animal = Cachorro(nome,raca,data)
                animal.id = id
                dao.alterar(animal)
                print("Cachorro alterado com sucesso!")
                r(0.5)
            if(a=="4"):
                r(0.5)
                print("Lista de todos os cachorros")
                print("\n\n")
                dao.listar()
                print("\n")
                a = input("Pressione enter para continuar")
            if(a=="5"):
                r(0.5)
                print("Buscar cachorro")
                print("\n\n")
                id = input("Informe o ID do cachorro buscado: ")
                dao.buscar(id)
                a = input("Pressione enter para continuar")
            if(a=="6"):
                r(0.5)
                print("Obrigado por utilizar o programa")
                r(2)
        else:
            r(0.5)    
            print("valor invalido")
            r(1.5)    
