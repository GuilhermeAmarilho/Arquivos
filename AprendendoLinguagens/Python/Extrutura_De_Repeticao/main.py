import time, os
def clear():
    time.sleep(2)
    os.system('cls')
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
def ex5():
    '''
        Dado um número positivo, desenvolva um algoritmo que escreva todos os números positivos menores que esse número
    '''
    ordem = int(input('Informe a ordem escolhida\n1 - Crescente\n2 - Decrescente\nSua resposta: '))
    value = int(input('Informe o valor limite da lista: '))
    if(ordem == 1):
        i = 1
        while(i<=value):
            time.sleep(0.1)
            print(i)
            i+=1
    else:
        while(value>0):
            print(value)
            time.sleep(0.1)
            value-=1
def ex6():
    '''
        Construa um algoritmo que calcula e mostra a tabela de depreciação para “n” anos de um determinado equipamento, a partir das informações fornecidas pelo usuário do valor da compra do equipamento e da taxa de depreciação por ano. Por exemplo, uma máquina comprada por R$28.000,00 se deprecia a uma taxa de R$4.000,00, por ano. A tabela de depreciação seria de sete anos, apresentando os seguintes valores:
        Verifique que o equipamento não pode ter valor negativo e, neste caso, será necessário que o usuário informe um valor maior que zero. No último ano, a depreciação pode ser maior que o valor residual do equipamento, mas o valor residual não pode ser negativo.
    '''
    nomeProduto = str(input('Informe o nome do produto que iremos análizar: '))
    taxaDepreciacao = float(input('Informe a taxa de depreciacao d@ '+nomeProduto+' por ano: '))
    custo = float(input('Informe o custo para comprar @ '+nomeProduto+': '))
    ano = 1
    clear()
    while(ano*taxaDepreciacao <= custo):
        print('No ',str(ano),'º ano, @ ',nomeProduto,' desvalorizou R$ ',(taxaDepreciacao*ano),
              '\n E atualmente, possúi um valor residual de R$ ',str(custo-taxaDepreciacao*ano))
        time.sleep(0.1)
        ano+=1
    if(ano*taxaDepreciacao > custo):
        ano+=1
        print('No ',str(ano),'º ano, @ ',nomeProduto,' desvalorizou R$ ',(taxaDepreciacao*ano),
              '\n E atualmente, possúi um valor residual de R$ 00,00')
def ex7():
    '''
        Supondo que você está na fila para pagar o total consumido em uma lancheria, a partir da tabela abaixo escreva um algoritmo que leia o código de cada item e a quantidade consumida (ou seja, o total deste item). A seguir, calcule e mostre o valor total da conta a pagar. A leitura será encerrada com um código diferente daqueles utilizados na tabela.
    '''
    valorFinal = 0
    while(True):
        print('Cardápio da lancheria\n1 - Hot Dog - Valor: R$ 4,00\n2 - X Salada - Valor: R$ 4,50\n3 - X Bacon - Valor: R$ 5,00\n4 - Torrada - Valor: R$ 2,00\n5 - Refrigerante - Valor: R$ 1,50')
        x = int(input('Informe o codigo do produtos que você consumiu: '))
        if(x>0 and x<6):
            if(x == 1):
                print('Você selecionou o Hot Dog')
                y = int(input('Informe a quantidade do produto que você consumiu: '))
                valorFinal+= y * 4.00
            else:
                if(x == 2):
                    print('Você selecionou o X Salada ')
                    y = int(input('Informe a quantidade do produto que você consumiu: '))
                    valorFinal+= y * 4.50
                else:
                    if(x == 3):
                        print('Você selecionou o X Bacon ')
                        y = int(input('Informe a quantidade do produto que você consumiu: '))
                        valorFinal+= y * 5
                    else:
                        if(x == 4):
                            print('Você selecionou a Torrada ')
                            y = int(input('Informe a quantidade do produto que você consumiu: '))
                            valorFinal+= y * 2
                        else:
                            if(x == 5):
                                print('Você selecionou o Refrigerante ')
                                y = int(input('Informe a quantidade do produto que você consumiu: '))
                                valorFinal+= y * 1.5
        else:
            print('Muito obrigado por informar seus itens!')
            break
        clear()
    print('Seu valor da compra ficou em ',str(valorFinal),' reais')
def ex8():
    '''
        Escreva um algoritmo que leia informações sobre um grupo de 10 pessoas, e calcule alguns dados estatísticos. Para cada pessoa do grupo, deve-se ler o nome da pessoa, a altura, o peso e o sexo (“F” para feminino e “M” para masculino). Calcular e escrever:
        A quantidade total de homens e mulheres e o percentual de cada
        Média de peso das pessoas por sexo (somatório dos pesos de todas as pessoas pela quantidade de pessoas)
    '''
    x = 0
    sexoMasculino = 0
    sexoFeminino = 0
    totalPeso = 0
    totalAltura = 0
    while(x  != 10):
        print('Olá, bem vindo ao questionário do IBGE')
        nome = str(input('Primeiramente, informe seu nome: '))
        sexo = int(input('Agora, informe seu sexo\n1 - Homem\n2 - Mulher\nSua resposta: '))
        if(sexo == 1):
            sexoMasculino+=1
        else:
            sexoFeminino+=1
        peso = float(input('Informe seu peso: '))
        totalPeso+=peso
        altura = float(input('Informe sua altura: '))
        totalAltura+=altura
        print('Muito obrigado Sr/Sra ',nome,' por participar do questionário')
        x+=1
        clear()
    print('O total de pessoas intrevistadas é de: ',str(sexoMasculino+sexoFeminino),
          '\n O número de homens é de: ',str(sexoMasculino),
          ' e seu percentual é de: ',str(sexoMasculino/(sexoMasculino+sexoFeminino)*100),'%',
          '\n O número de mulheres é de: ',str(sexoFeminino),
          ' e seu percentual é de: ',str(sexoFeminino/(sexoMasculino+sexoFeminino)*100),'%')
    print('A média de peso entre as pessoas é de: ',str(totalPeso/(sexoFeminino+sexoMasculino)))
    print('A média de altura entre as pessoas é de: ',str(totalAltura/(sexoFeminino+sexoMasculino)))
def ex9():
    '''
        Um cubo de gelo, exposto a uma determinada temperatura, perde metade de sua massa a cada 50 segundos. Dada a massa inicial, em gramas, proponha um algoritmo que determine o tempo necessário para que a massa do cubo seja menor que 0,5 grama. Ao final, escreva o tempo calculado em horas, minutos e segundos. Considere que a massa inicial deverá ser um valor maior ou igual a 0,5 grama.
    '''
    peso = float(input('Informe a massa, em gramas, do cubo de gelo que deseja calcular: '))
    tempo = 0
    while (peso >= 0.5):
        tempo+=50
        peso = peso/2
    if(tempo>0):
        if (tempo>=60):
            print ('Esse cúbo de gelo levará ', (tempo//60), ' minutos e ', (tempo%60), ' segundos para derreter.')
        else:
            print ('Esse cúbo de gelo levará ',(tempo%60), ' segundos para derreter.')
    else:
        print('Você informou um valor inválido para essa operação.')
def ex10():
    '''
        Escreva um algoritmo que leia a quilometragem e o consumo em litros em cada abastecimento, e calcule o consumo médio por quilômetro de cada segmento da viagem. O consumo médio é obtido com a diferença de quilometragem entre dois abastecimentos, dividindo-a pelo número de litros do último abastecimento.
        Também deve calcular e mostrar o consumo médio cumulativo ao final de cada trecho (a cada abastecimento). O consumo médio cumulativo é calculado através da diferença entre a quilometragem de um abastecimento e a quilometragem do início da viagem, dividindo-a pela soma dos litros de todos os abastecimentos até então.
        consumo_medio_cumulativo_final = ( km_final - km_inicial ) / total_litros_abastecido
        Perceba que o usuário não deve informar uma quilometragem menor que a anterior. Para encerrar a leitura da quilometragem, o usuário deve informar a quilometragem zero.
    '''
    km_inicial = int(input('Informe a kilometragem inicial marcada no carro: '))
    combustivel_inicial = float(input('Informe quanto de combustivel há em seu carro: '))
    km_final = 1
    while(km_final != 0):
        print('Você fez uma parada para abastecer.')
        km_final = int(input('Qual kilometragem está marcando no seu carro? '))
        if(km_final != 0):
            combustivel_final = float(input('Informe quanto de combustivel você abasteceu em seu carro: '))
            km_andada = km_final - km_inicial
            combustivel_gasto = combustivel_inicial - combustivel_final
            print('Você fez ',(km_andada/combustivel_gasto),' km/L desde o início de sua viágem até agora')
            km_inicial = km_final
            combustivel_inicial = combustivel_final