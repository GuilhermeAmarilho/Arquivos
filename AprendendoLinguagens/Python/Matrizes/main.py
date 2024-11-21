import numpy
def ex1_mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))
def ex1_somar_matrizes(m1, m2):
    array = []
    col = 0
    while col < len(m1):
        lin = 0
        array.append([])
        while lin < len(m1[col]):
            array[col].append(m1[col][lin] + m2[col][lin])
            lin += 1
        col += 1
    return array
def ex1():
    '''
        Faça um programa que defina uma matriz identidade 3x3 e exiba a soma dela com a matriz [ [1,2,3], [4,5,6], [7,8,9] ]. Dica: Crie um procedimento para mostrar uma matriz.
    '''
    matriz = [ [1,2,3], [4,5,6], [7,8,9] ]

    matriz_identidade = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

    # matriz_soma = [[matriz_identidade[i][j] + matriz[i][j] for j in range(3)] for i in range(3) ]
    print(ex1_somar_matrizes(matriz_identidade, matriz))
def ex2_gerar_array(i, j):
    array = []
    col = 0
    while col < j:
        lin = 0
        array.append([])
        while lin < i:
            array[col].append(
                lin*lin + col
            )
            lin += 1
        col += 1
    return array
def ex2_mostrar_matriz(matriz):
    col = 0
    while col < len(matriz):
        lin = 0
        while lin < len(matriz[col]):
            if col == lin:
                print(matriz[col][lin], end=' ')
            lin += 1
        col += 1
def ex2():
    '''
        Faça um programa que leia dois inteiros linhas e colunas, e que então crie uma matriz deste tamanho com valores reais. Cada elemento deve ser inicializado com a fórmula i²+j, onde i é o índice da linha e j o índice da coluna. Exiba a diagonal desta matriz. Não use numpy.
    '''
    array = ex2_gerar_array(6,6)
    print(array)
    ex2_mostrar_matriz(array)
def ex3():
    '''
        Faça um programa que defina uma matriz identidade 3x3 e exiba a soma dela com a matriz [ [1,2,3], [4,5,6], [7,8,9] ]. Dica: Crie um procedimento para mostrar uma matriz. Use numpy
    '''
    identidade = numpy.eye(3)
    matriz = [ [1,2,3], [4,5,6], [7,8,9] ]
    soma = identidade + matriz
    ex1_mostrar_matriz(soma)
def ex4():
    '''
        Faça um programa que leia dois inteiros linhas e colunas, e que então crie uma matriz deste tamanho com valores reais. Cada elemento deve ser inicializado com a fórmula i² +j, onde i é o índice da linha e j o índice da coluna. Exiba a diagonal desta matriz. Use numpy
    '''
    
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    matriz = numpy.zeros((linhas, colunas), dtype=float)
    for i in range(linhas):
        for j in range(colunas):
            matriz[i, j] = i**2 + j
    diagonal = numpy.diagonal(matriz)
    print(f'A matriz é: \n{matriz}\nSua diagonal é: {diagonal}')