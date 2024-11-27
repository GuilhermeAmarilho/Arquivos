from dao import CachorroDAO
from cachorro import Cachorro
from time import sleep
import os
def clear():
    os.system('cls')

clear()
def main():
    dao = CachorroDAO()
    a = ''
    roll = True
    while roll:
        clear()
        print(
            'Controle de animais do guilherme\n'+
            '1 - adicionar novo cachorro\n'+
            '2 - excluir cachorro\n3 - alterar cachorro\n'+
            '4 - listar cachorro\n5 - buscar cachorro\n'+
            '6 - fechar o programa'
        )
        option = int(input('informe a requisição: '))
        match option:
            case 1:
                clear()
                print('Adicionar novo cachorro!')
                nome = input('Informe o nome do animal: ')
                raca = input('Informe a raça do animal: ')
                if dao.inserir(Cachorro(nome,raca)):
                    print(f'O cachorrro {nome} foi adicionado com sucesso!')
                else:
                    print('Não foi possível adicionar o cachorro!')
                input('Pressione enter para prosseguir!')
            case 2:
                clear()
                print('Excluir cachorro')
                id = str(input('Informe o ID do cachorro a apagar: '))
                if dao.deletar(id):
                    print('Cachorro excluido com sucesso!')
                else:
                    print('Não foi possivel excluir o cachorro!')
                input('Pressione enter para prosseguir!')
            case 3:
                clear()
                print('Alterar cachorro')
                id = str(input('Informe o ID do cachorro a alterar: '))
                nome = input('Informe o novo nome do animal: ')
                raca = input('Informe a nova raça do animal: ')
                animal = Cachorro(nome, raca)
                animal._set_id(id)
                if dao.alterar(animal):
                    print('Cachorro alterado com sucesso!')
                else:
                    print('Não foi possivel alterar o cachorro!')
                input('Pressione enter para prosseguir!')
            case 4:
                clear()
                print('Lista de todos os cachorros')
                lista = dao.listar()
                if(len(lista) == 0):
                    print('Ainda não há cachorros registrados!')
                else:
                    for dog in lista:
                        print(dog)
                a = input('\nPressione enter para continuar')
            case 5:
                clear()
                print('Buscar cachorro')
                id = str(input('Informe o ID do cachorro buscado: '))
                if dao.buscar(id) != '':
                    print(dao.buscar(id))
                else:
                    print('Cachorro não encontrado!')
                input('Pressione enter para continuar')
            case 6:
                roll = False
            case __:
                print('valor invalido')
main()