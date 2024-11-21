def ex1_funcao_linha(n):
    cont = 0
    string = ""
    while cont < n:
        string += "#"
        cont+=1
    return string
def ex1():
    '''
        Faça um procedimento chamado linha() que recebe um parâmetro inteiro n, indicando que deve ser mostrada na tela uma sequência de n caracteres '#', em uma mesma linha
    '''
    string = ex1_funcao_linha(3)
    print(string)
def ex2_funcao_linha(l, h):
    string = ""
    i = 0
    while h > i:
        j = 0
        while l > j:
            string += '#'
            j += 1 
        string +='\n'
        i += 1
    return string
def ex2():
    '''
        Usando o procedimento linha(), faça um procedimento chamado retangulo() que recebe os parâmetros inteiros a e b, indicando os lados de um retângulo a ser impresso, e também composto por caracteres '#'. Teste várias vezes, usando valores diferentes.
    '''
    retangulo = ex2_funcao_linha(14,6)
    return retangulo
def ex3_funcao_linha(l):
    cont = 0
    string = ''
    while cont < l:
        subcont = 0
        while subcont < l:
            string += '#'
            subcont += 1
        string += '\n'
        cont += 1
    return string
def ex3():
    '''
        Usando o procedimento retangulo(), faça um procedimento chamado quadrado(), que recebe um parâmetro inteiro n indicando o lado do quadrado a ser impresso. Teste este procedimento, chamando-o com vários valores.
    '''
    print(ex3_funcao_linha(6))