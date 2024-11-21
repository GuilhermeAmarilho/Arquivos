def ex1():
    '''
        Faça um programa que leia dois valores inteiros x e y. Se x for menor ou igual a y, então imprima os valores inteiros que começam em x e vão até y, incluindo ambos, um em cada linha
    '''
    x = int(input('Informe o 1º valor escolhido: '))
    y = int(input('Informe o 2º valor escolhido: '))
    if(x <= y):
        inicial = x
        final = y
    else:
        inicial = y
        final = x
    print("A sequência que vai de ", inicial, " a ", final," é: ")
    while(inicial <= final):
        print(inicial, end=' ')
        inicial+=1
def ex2():
    '''
        Faça um programa que leia um inteiro n. Então leia mais n valores reais digitados pelo usuário e calcule sua soma. Ao final, mostre esta soma e também a média aritmética.
    '''
    valor = 1
    contador = 1
    acumulador = 0
    while (valor!=0):
        valor = int(input('Informe o '+str(contador)+' valor escolhido: \nPressione 0 para sair.\nQual resultado você deseja? '))
        acumulador+=valor
        contador+=1
    print('Você informou ',contador,' números!\nA soma desses números é: ',acumulador,'\nA média aritimética deles é: ',(acumulador/(contador-1)))
def ex3():
    '''
        Faça um programa que fique em repetição, sempre solicitando um valor inteiro e positivo v. Caso o usuário entre com um valor zero ou negativo, repita a pergunta e leia um novo valor. A repetição só deve terminar para uma entrada positiva.
    '''
    valor = -1
    while(valor <= 0):
        valor = int(input('Informe um valor inteiro e positivo: '))
def ex4():
    '''
        Faça um programa que defina um saldo inicial zero. O programa deve solicitar repetidamente por um valor real (negativo se débito, positivo se crédito), que atualiza o saldo. Quando for entrado 0, o programa deve terminar e mostrar o saldo restante.
    '''
    saldo = 0
    valor = 1
    while (valor!=0):
        valor = int(input('Informe o valor para a transação\nPositivo para a créditar na conta\nNegativo para debitar da conta\nSua resposta: '))
        saldo+= valor
    print('Seu saldo final é de: R$',saldo,',00')