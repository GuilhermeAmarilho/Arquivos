import math
def ex1():
    # Calcule a área A de um círculo de raio r=2, e apresente a medida na tela.
    # vou fazer c/raio variavel
    raio = int(input('Informe o raio desejado para o circulo: '))
def ex2():
    # Escolha alguma temperatura em graus Celsius e atribua à variável C. Apresente esta convertida em Fahrenheit, usando a fórmula de conversão
    c = float(input('Informe a temperatura em ºC: '))
    f = (9*c/5)+32
    print('A temperatura ',c,'ºC é equivalente a: ',f,'ºF')
def ex3():
    # Faça um programa que calcule um aumento de 12% de um salário. Deve ser lido o valor do salário e mostrado o novo valor.
    salario_antigo = float(input('Informe seu salário atual: '))
    novo_salario = salario_antigo*1.12
    # (salario_antigo * 12 / 100) + salario_antigo
    print('Seu salário de R$ ',salario_antigo,' será reajustado, com um acrescimo de 12%, para R$ ',novo_salario)
def ex4():
    # Leia 3 valores, então calcule e imprima sua média aritmética.
    i = 1
    montante = 0
    while (i <= 3):
        montante+= float(input('Informe o '+str(i)+'º valor a ser calculado: '))
        i+=1
    print('A média aritmética dos numeros informados é: ',(montante/3)) 
def ex5():
    # Leia 3 valores, então calcule e imprima sua média geométrica.
    # medGeometrica = raiz enesima de n termos 
    i = 1
    valor1 = float(input('Informe o 1º valor a ser calculado: '))
    valor2 = float(input('Informe o 2º valor a ser calculado: '))
    valor3 = float(input('Informe o 3º valor a ser calculado: '))
    med_geometrica = math.pow(
        (valor1*valor2*valor3),
        (1/3)
        )
    print('A média geométrica dos numeros informados é: ',str(med_geometrica)) 
def ex6():
    # Faça um programa que leia 3 valores que correspondem ao número de horas, minutos e segundos e depois mostre o equivalente desse tempo em segundos
    horas = int(input('Informe as horas desejadas: '))
    minutos = int(input('Informe os minutos desejados: '))
    segundos = int(input('Informe os segundos desejados: '))
    total_segundos = horas*3600 + minutos*60 + segundos
    print('A conversão de ',horas,' Hr ',minutos,' Min', segundos,' Seg em Segundos é de: ',str(total_segundos))
def ex7():
    # Faça um programa que leia um valor em segundos e mostre o equivalente em horas, minutos e segundos.
    horas = 0
    minutos = 0
    segundos = int(input('Informe os segundos desejados: '))
    print('A conversão de ',segundos, ' Seg para HH MM SS é de: ',end='')
    if(segundos>3600):
        horas = segundos//3600
        print(segundos//3600, ' Hr ',end='')
    segundos = segundos - horas*3600
    # Diminui do total de segundos as horas contabilizadas
    if(segundos>60):
        minutos = segundos//60
        print(segundos//60, ' Min ',end='')
    segundos = segundos - minutos*60
    print(segundos, ' Seg')