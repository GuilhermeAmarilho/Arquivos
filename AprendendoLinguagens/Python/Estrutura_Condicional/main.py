import math
def ex1():
    '''
        Leia um número inteiro i e indique se ele está dentro do intervalo fechado [1, 10]
    '''
    num = int(input('Informe o número desejado: '))
    if(num>=0 and num<=10):
        print('O número ',num, ' está contido entre 0 e 10')
    else:
        print('O número ',num, ' não está contido entre 0 e 10')
def ex2():
    '''
        Leia um número inteiro i e indique se ele está dentro do intervalo aberto (1, 10)
    '''
    num = int(input('Informe o número desejado: '))
    if(num>0 and num<10):
        print('O número ',num, ' está contido entre 0 e 10')
    else:
        print('O número ',num, ' não está contido entre 0 e 10')
def ex3():
    '''
        Leia um número inteiro i e indique se ele está fora do intervalo fechado [1, 10]
    '''
    num = int(input('Informe o número desejado: '))
    if(num<0 and num>10):
        print('O número ',num, ' está fora do intervalo fechado [0 a 10]')
    else:
        print('O número ',num, ' está dentro do intervalo fechado [0 a 10]')
def ex4():
    '''
        Leia um inteiro n. Imprima uma mensagem para os casos em que for negativo, zero ou positivo.
    '''
    num = int(input('Informe o número desejado: '))
    if ( num > 0 ):
        print('O número ' , num , ' é positivo.')
    else:
        if ( num < 0 ):
            print('O número ' , num , ' é negativo.')
        else:
            print('O número ' , num , ' não é positivo nem negativo.')
def ex5():
    '''
        Leia um inteiro indicando uma quantidade de horas. Se a quantidade for menor ou igual a 23, simplesmente imprima o número de horas. Caso contrário, calcule e imprima a quantidade de dias completos e de horas remanescentes.
    '''
    hora = int(input('Informe a hora desejada: '))
    if(hora>=0):
        if(hora<=23):
            print('O total de horas é: ',hora,' horas')
        else:
            dias = hora//24
            hora-= dias*24
            print('Com o total de horas informado, temos ',dias,' dias e ',hora,' horas')
    else:
        print('Você informou um valor negativo para a hora. Esse valor não é permitido')
def ex6():
    '''
        Escreva um programa que leia um valor inteiro i e diga se este é par ou ímpar.
    '''
    valor = int(input('Informe o valor desejado: '))
    if(valor%2 == 0):
        print('O número ',valor,' é par')
    else:
        print('O número ',valor,' é impar')
def ex7():
    '''
        Defina dois valores a e b, escrevendo um programa que apresente os mesmos em ordem crescente, ou indicando que são iguais.
    '''
    valor1 = int(input('Informe o 1º valor: '))
    valor2 = int(input('Informe o 2º valor: '))
    if(valor1 > valor2):
        print('O valor ',valor1,' é maior que o valor ',valor2)
    else:
        if(valor1 < valor2):
            print('O valor ',valor2,' é maior que o valor ',valor1)
        else:
            print('Os valores ',valor1,' e ',valor2,' são iguais.')
def ex8():
    '''
        Defina um cardápio contendo três itens com código e preço unitário. O programa deve solicitar um código e a respectiva quantidade, calculando e imprimindo o valor a ser pago.
    '''
    print('Cardápio digital:\n',
            '1 - Salada\t\t\t ---- Valor: R$ 2,00\n',
            '2 - Torrada\t\t\t ---- Valor: R$ 3,00\n',
            '3 - Suco de fruta\t\t ---- Valor: R$ 4,00\n',
            '4 - Cachorro quente\t\t ---- Valor: R$ 5,00\n'
        )
    codigo = int(input('Informe o código do produto consumido: '))
    quantidade = int(input('Informe a quantidade do produto consumido: '))
    match codigo:
        case 1:
            print('Você consumiu ',quantidade,'x de Salada. O valor final foi: R$ ',str(quantidade*2),',00')
        case 2:
            print('Você consumiu ',quantidade,'x de Torrada. O valor final foi: R$ ',str(quantidade*3),',00')
        case 3:
            print('Você consumiu ',quantidade,'x de Suco de frutas. O valor final foi: R$ ',str(quantidade*4),',00')
        case 4:
            print('Você consumiu ',quantidade,'x de Cachorro quente. O valor final foi: R$ ',str(quantidade*5),',00')
        case _:
            print('Você informou o código referente a um item inexistente')
def ex9():
    '''
        Leia os valores reais a, b e c, representando os coeficientes de uma equação de segundo grau. Primeiro, calcule o discriminante da equação, dado por Δ = b2 - 4ac. Então trate as três situações possíveis e indique as eventuais raízes da equação:
    '''
    # sem raízes / uma única raiz / duas raízes distintas
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
    print('A equação informada é ', end='')
    if(a != 0):
        print('(',a,')x² ', end='')
    if(b != 0):
        print('+ (',b,')x ', end='')
    if(c != 0):
        print('+ (',c,')')
    delta = b*b - 4*a*c
    if(delta > 0):
        x = ( -b + math.pow(delta , (1/2)) )/ (2*a)
        # pode usar math.sqrt que já é a formula de raiz, mas pow eleva. x elevado 1/2 é igual a raiz quadrada de x
        print('Há duas raizes distintas para satisfazer a equação. São elas: ')
        print('x\' = ',str(x))
        x = ( -b - math.pow(delta , (1/2)) )/ (2*a)
        print('x\'\' = ',str(x))
    else:
        if(delta==0):
            x = - b / (2*a)
            print('Há apenas uma raiz possível para a equação: ',str(x))
        else:
            print('Não há raizes reais possíveis para a equação!')