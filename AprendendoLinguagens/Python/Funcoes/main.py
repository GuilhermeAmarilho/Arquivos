def ex1_simples_uniao(lista1, lista2):
    return list(set(lista1) | set(lista2))
def ex1_simples_uniao_lista(lista1, lista2):
    uniao_resultado = lista1.copy()
    for elemento in lista2:
        if elemento not in uniao_resultado:
            uniao_resultado.append(elemento)
    return uniao_resultado
def ex1_simples():
    '''
        Defina a=[7,4,1,5] e b=[1,8,7,3,6]. Faça uma função chamada união() que recebe duas listas e retorna a união dos elementos das mesmas, sem repetição. 
        1 - Faça primeiro usando conjuntos de Python, ou seja, set() 
        2 - Então faça usando apenas listas (dica: percorra a primeira lista, consultando a segunda)
    '''
    a=[7,4,1,5] 
    b=[1,8,7,3,6]
    print(ex1_simples_uniao(a,b))
    print(ex1_simples_uniao_lista(a,b))
def ex2_simples_anagrama(str1, str2):
    lista1 = sorted(list(str1))
    lista2 = sorted(list(str2))
    return lista1 == lista2
def ex2_simples():
    '''
        Faça uma função chamada é_anagrama(), que receba duas strings e teste se uma é um anagrama da outra. Ou seja, se têm exatamente as mesmas letras mas em ordem diversa.
            - Por que não é conveniente usar conjuntos de Python neste problema?
            - Então faça usando apenas listas (dica: converta a string para uma lista)
    '''
    string1 = str(input('Informe a sua primeira string: '))
    string2 = str(input('Informe a sua segunda string: '))
    if ex2_simples_anagrama(string1, string2):
        print('As strings são anagramas')
    else:
        print('As strings não são anagramas')
# Lista de exercícios
def ex1_imprimir_padrao(n):
        for i in range(1, n + 1):
            linha = (str(i) + " ") * i
            print(linha.strip())
def ex1():
    '''
        Faça um programa para imprimir:
            1
            2   2
            3   3   3
            .....
            n   n   n   n   n   n  ... n
        para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
    '''
    n = int(input("Digite o valor de n: "))
    ex1_imprimir_padrao(n)
def ex2_imprimir_sequencia(n):
    for i in range(1, n + 1):
        linha = " ".join(str(j) for j in range(1, i + 1))
        print(linha)
def ex2():
    '''
        Faça um programa para imprimir:
            1
            1   2
            1   2   3
            .....
            1   2   3   ...  n
        para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
    '''
    n = int(input("Digite o valor de n: "))
    ex2_imprimir_sequencia(n)
def ex3_soma_tres_numeros(a, b, c):
    return a + b + c
def ex3():
    '''
        Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
    '''
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    resultado = ex3_soma_tres_numeros(num1, num2, num3)
    print("A soma dos três números é:", resultado)
def ex4_verifica_positivo_negativo(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'
def ex4():
    '''
        Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
    '''
    numero = float(input("Digite um número: "))
    resultado = ex4_verifica_positivo_negativo(numero)
    print("Resultado:", resultado)
def ex5_somaImposto(taxaImposto, custo):
    custo_com_imposto = custo + (custo * taxaImposto / 100)
    return custo_com_imposto
def ex5():
    '''
        Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
    '''
    taxa = float(input("Digite a taxa de imposto em porcentagem: "))
    custo_item = float(input("Digite o custo do item antes do imposto: "))
    custo_final = ex5_somaImposto(taxa, custo_item)
    print("O custo do item com imposto é:", custo_final)
def ex6_converter_para_12_horas(hora, minuto):
    if hora == 0:
        hora_12 = 12
        periodo = 'A'
    elif hora < 12:
        hora_12 = hora
        periodo = 'A'
    elif hora == 12:
        hora_12 = 12
        periodo = 'P'
    else:
        hora_12 = hora - 12
        periodo = 'P'
    return hora_12, minuto, periodo
def ex6_exibir_hora_12(hora_12, minuto, periodo):
    periodo_str = "A.M." if periodo == 'A' else "P.M."
    print(f"{hora_12}:{minuto:02d} {periodo_str}")
def ex6():
    '''
        Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
    '''
    while True:
        hora_24 = int(input("Digite a hora em formato de 24 horas: "))
        minuto = int(input("Digite os minutos: "))
        hora_12, minuto, periodo = ex6_converter_para_12_horas(hora_24, minuto)
        ex6_exibir_hora_12(hora_12, minuto, periodo)
        repetir = input("Deseja converter outra hora? (s/n): ").strip().lower()
        if repetir != 's':
            break