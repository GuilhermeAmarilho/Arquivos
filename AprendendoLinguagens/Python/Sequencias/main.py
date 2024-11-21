import random, math
def ex1_slide():
    '''
        Faça um programa que defina v=[1,2,3,4,5,6,7]. Então exiba v em duas metades de comprimento semelhante.
    '''
    v=[1,2,3,4,5,6,7]
    size = len(v)//2
    first_list = ''
    i=0
    while (len(first_list) < size):
        first_list += str(v[i])
        i+=1
    last_list = ''
    while (i < len(v)):
        last_list += str(v[i])
        i+=1
    print('O vetor')
    print(v)
    print('Possui foi dividido em 2 partes, sendo elas: \n'+first_list+'\n'+last_list)
def ex2_slide():
    '''
    Faça um programa que leia uma string s e conte o número de ocorrências da letra 'a'.
    '''
    string = str(input('Informe a string que deseja testar: '))
    ocorrencia = 0
    for char in string:
        if (char == 'a'):
            ocorrencia+=1
    print('Ocorreu '+str(ocorrencia)+' vezes a letra a')
def ex3_slide():
    '''
        Faça um programa que leia um inteiro n e uma string s, criando uma nova string com s repetida n vezes.
    '''
    string = str(input('Informe a string que deseja testar: '))
    n = int(input('Informe quantas vezes deseja repetir a frase: '))
    i = 0 
    result = ''
    while i < n:
        result += string + ' '
        i+=1
    print('A string final é:\n'+result)
def ex1():
    '''
        Faça um programa em Python que gera uma lista aleatória de 10 números inteiros, entre 1 e 100, e calcule a soma dos elementos da lista.
    '''
    numeros = [random.randint(1, 100) for _ in range(10)]
    soma = sum(numeros)
    print("Lista de números:", numeros)
    print("Soma dos elementos:", soma)
def ex2():
    ''' 
        Faça um programa em Python que gera uma lista aleatória de 5 números inteiros, entre 1 e 100, e calcule o produto dos elementos da lista.
    '''
    numeros = [random.randint(1, 100) for _ in range(5)]
    produto = math.prod(numeros)
    print("Lista de números:", numeros)
    print("Produto dos elementos:", produto)
def ex3():
    '''
        Faça um programa em Python que gera uma lista aleatória de 20 números inteiros, entre 1 e 10, e remova os duplicados
    '''
    numeros = [random.randint(1, 10) for _ in range(20)]
    numeros_sem_duplicados = []
    for num in numeros:
        if num not in numeros_sem_duplicados:
            numeros_sem_duplicados.append(num)
    print("Lista original:", numeros)
    print("Lista sem duplicados:", numeros_sem_duplicados)
def ex3_sem_conjuntos():
    '''
        Faça um programa em Python que gera uma lista aleatória de 20 números inteiros, entre 1 e 10, e remova os duplicados
    '''
    numeros = [random.randint(1, 10) for _ in range(20)]
    numeros_sem_duplicados = list(set(numeros))
    print("Lista original:", numeros)
    print("Lista sem duplicados:", numeros_sem_duplicados)
def ex4():
    '''
        Faça um programa em Python que gera duas listas aleatórias de 20 números inteiros, entre 1 e 10, e crie uma nova lista com a união das duas listas, removendo os duplicados
    '''
    lista1 = [random.randint(1, 10) for _ in range(20)]
    lista2 = [random.randint(1, 10) for _ in range(20)]
    uniao_lista = lista1 + lista2
    uniao_sem_duplicados = []
    for num in uniao_lista:
        if num not in uniao_sem_duplicados:
            uniao_sem_duplicados.append(num)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("União sem duplicados:", uniao_sem_duplicados)
def ex5():
    '''
        Faça um programa em Python que gera duas listas aleatórias de 10 números inteiros, entre 1 e 10, e crie uma nova lista com a intersecção das duas listas, removendo os duplicados.
    '''
    lista1 = [random.randint(1, 10) for _ in range(10)]
    lista2 = [random.randint(1, 10) for _ in range(10)]
    interseccao = []
    for num in lista1:
        if num in lista2 and num not in interseccao:
            interseccao.append(num)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Interseção sem duplicados:", interseccao)
def ex6():
    '''
        Faça um programa em Python que gera duas listas aleatórias de 10 números inteiros, entre 1 e 100, e mostre o valor do produto escalar entre as duas listas.
    '''
    lista1 = [random.randint(1, 100) for _ in range(10)]
    lista2 = [random.randint(1, 100) for _ in range(10)]
    produto_escalar = sum(a * b for a, b in zip(lista1, lista2))
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Produto escalar:", produto_escalar)
def ex7():
    '''
        Faça um programa que gera uma lista aleatória de 5 números inteiros e rotaciona a lista de acordo com um valor N informado pelo usuário. Exemplo: [50, 30, 20, 10, 40], N=3 -> [20, 10, 40, 50, 30]
    '''
    lista = [random.randint(1, 100) for _ in range(5)]
    N = int(input("Informe o valor de N para rotacionar a lista: "))
    N = N % len(lista)  
    lista_rotacionada = lista[N:] + lista[:N]
    print("Lista original:", lista)
    print("Lista rotacionada:", lista_rotacionada)
def inserir_ordenado(lista, numero):
    for i in range(len(lista)):
        if numero < lista[i]:
            lista.insert(i, numero)
            return 
    lista.append(numero)
def ex8():
    '''
        Faça um programa em Python que leia 10 números inteiros e apresente uma lista ordenada. A cada elemento inserido deve ser mostrada a lista ordenada. Note que ao adicionar o elemento na lista, ele deve ser inserido na posição que mantenha a lista ordenada. Não pode usar a função sort().
    '''
    lista_ordenada = []
    for _ in range(10):
        numero = int(input("Digite um número inteiro: "))
        inserir_ordenado(lista_ordenada, numero)
        print("Lista ordenada:", lista_ordenada)
    '''
        Faça um programa em Python que leia uma string que representa uma sequência de DNA, composta pelas bases nitrogenadas C (Citosina), G (Guanina), T (Timina), e A (Adenina), e crie uma string que mostre a ligação complementar de cada base nitrogenada na cadeia de DNA. A ligação complementar segue as seguintes regras:
            ● C liga-se com G
            ● G liga-se com C
            ● T liga-se com A
            ● A liga-se com T
        O programa deve mostrar a string de entrada e a de saída, uma embaixo da outra para a devida comparação. Devem ser tratados os erros na entrada, como letras diferentes.
    '''
    string_com_erro = True
    while string_com_erro:
        sequencia_genetica = str(input('Informe o próximo item da base nitrogenada: ')) 
        ligacao_complementar = ''
        for caractere in sequencia_genetica:
            if ( caractere == 'C' or caractere == 'G' or caractere == 'T' or caractere == 'A' ):
                string_com_erro = False
                match caractere:
                    case 'A':
                        ligacao_complementar+='T'
                    case 'T':
                        ligacao_complementar+='A'
                    case 'G':
                        ligacao_complementar+='C'
                    case 'C':
                        ligacao_complementar+='G'
            else:
                string_com_erro = True
                print('Por favor, informe uma string válida!')
                break
    print('A string original é:\t\t'+sequencia_genetica+'\nSua ligação complementar é:\t'+ligacao_complementar)