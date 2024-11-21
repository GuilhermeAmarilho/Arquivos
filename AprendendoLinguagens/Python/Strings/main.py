def ex1():
    '''
        Faça um programa em Python que leia uma string, conte e imprima o número de caracteres que elapossui (incluindo espaços).
    '''
    string = input("Digite uma string: ")
    numero_de_caracteres = len(string)
    print(f"A string possui {numero_de_caracteres} caracteres (incluindo espaços).")
def ex2():
    '''
        Faça um programa em Python que leia uma string, conte e imprima o número de palavras que ela possui. Considere que cada palavra é separada por um único espaço
    '''
    string = input("Digite uma string: ")
    palavras = string.split()
    numero_de_palavras = len(palavras)
    print(f"A string possui {numero_de_palavras} palavras.")
def ex3():
    '''
    Faça um programa em Python que leia uma string e diga se ela é palíndromo. Um palíndromo é uma string que é igual quando lida de trás para frente
    '''
    string = input("Digite uma string: ")
    string_inversa = string[::-1]
    print('A sua string é: \n'+string+
          '\nPara ela ser palindroma, lendo de trás para frente devemos encontrar a mesma string, com isso temos:\n'+string_inversa+
          '\nCom isso, sabemos que a string informada ',end='')
    if(string_inversa==string):
        print('é palindroma')
    else:
        print('não é palindroma')
def ex4():
    '''
        Refaça o exercício 3, ignorando espaços e diferenças entre maiúsculas e minúsculas
    '''
    string = input("Digite uma string: ")
    string = string.replace(" ", "").lower()
    string_inversa = string[::-1]
    print('A sua string é: \n'+string+
          '\nPara ela ser palindroma, lendo de trás para frente devemos encontrar a mesma string, com isso temos:\n'+string_inversa+
          '\nCom isso, sabemos que a string informada ',end='')
    if(string_inversa==string):
        print('é palindroma')
    else:
        print('não é palindroma')
def ex5():
    '''
        Faça um programa em Python que leia uma string e remova todos os caracteres duplicados.
    '''
    string = input("Digite uma string: ")
    resultado = []    
    for char in string:
        # Se o caractere ainda não está no resultado, adiciona
        if char not in resultado:
            resultado.append(char)
    nova_string = ''
    for item in resultado:
        nova_string+=item
    print (nova_string)
def ex6():
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