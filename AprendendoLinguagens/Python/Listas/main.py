def ex_slide():
    '''
        Faça um programa que leia uma lista de 10 números inteiros e em seguida leia um novo valor (x) e diga qual a posição de x na lista. 
        Caso x não esteja na lista, mostrar a mensagem que o elemento não se encontra na lista. 
        Obs.: Não pode usar o operador in.
    '''
    i = 0
    numeros = []
    print("Digite 10 números inteiros:")
    while i < 10:
        numero = int(input(f"Número {i+1}: "))
        numeros.append(numero)

    # Leitura do número x
    x = int(input("Digite o número para buscar na lista: "))

    # Verificação se x está na lista e sua posição
    find = False
    i = 0
    while i < 10:
        if (numeros[i] == x):
            print(f"O número {x} está na posição {i} da lista.")
            encontrado = True
            break
    if (not encontrado):
        print("O elemento não se encontra na lista.")
def ex1():
    ''''
        Faça um programa em Python que construa uma lista v = [4, 1, 5, 8, 6]. Após, mostre o menor e o maior valor presente na lista.
    '''
    v = [4, 1, 5, 8, 6]
    min = v[0]
    max = v[0]
    i = 0
    while i < len(v):
        if v[i] < min:
            min = v[i]
        i+=1
    i = 0
    while i < len(v):
        if v[i] > max:
            max = v[i]
        i+=1
    print('A sua lista é: ')
    print(v)
    print('O maior valor é: '+ str(max) + '\nO menor valor é: ' + str(min))
def ex2():
    '''
        Faça um programa que construa uma lista com tamanho e elementos informados pelo usuário. Após construída, solicitar que o usuário informe um valor a ser buscado na lista. Se o valor estiver na lista, informar a sua posição; senão, informar que não existe na lista (valor “False”). 
    '''
    size = int(input('Informe o tamanho da sua lista: '))
    i = 0
    lista = []
    while i < size:
        i+=1
        valor = int(input('Informe o ' + str(i) + 'º elemento da sua lista: '))
        lista.append(valor)
    find = int(input('Informe o valor a ser procurado na sua lista: '))
    # i == size aqui
    encontrado = False
    while i >= 0:
        i-=1
        if find == lista[i]:
            encontrado = True
            break
    # if encontrado:
    #     print('O valor ' + str(find) + ' é o ' , str(i) , 'º elemento da lista')
    # else:
    #     print('O valor ' + str(find) + ' não foi encontrado na lista')
    print ( 
        ('O valor ' + str(find) + ' é o ' + str(i) + 'º elemento da lista') 
        if encontrado else 
        ('O valor ' + str(find) + ' não foi encontrado na lista') 
    )
def ex3():
    '''
        Faça um programa que construa uma lista com tamanho e elementos (valores) previamente informados pelo usuário. Após construída, solicitar que o usuário informe um elemento a ser verificado na lista. Se existir, apresentar o total de vezes que o elemento aparece.
    '''
    size = int(input('Informe o tamanho da sua lista: '))
    i = 0
    lista = []
    while i < size:
        i+=1
        valor = int(input('Informe o ' + str(i) + 'º elemento da sua lista: '))
        lista.append(valor)
    find = int(input('Informe o valor a ser procurado na sua lista: '))
    # i == size aqui
    vezes_encontrado = 0
    while i > 0:
        i-=1
        if find == lista[i]:
            vezes_encontrado += 1
    print ('O valor ' + str(find) + ' ocorreu na lista ' + str(vezes_encontrado), end='')
    print(
        ' vez'
        if vezes_encontrado == 1 else
        ' vezes'
    )
def pegar_mes(mes):
    match mes:
        case 1:
            return('Janeiro')
        case 2:
            return('Fevereiro')
        case 3:
            return('Março')
        case 4:
            return('Abril')
        case 5:
            return('Maio')
        case 6:
            return('Junho')
        case 7:
            return('Julho')
        case 8:
            return('Agosto')
        case 9:
            return('Setembro')
        case 10:
            return('Outubro')
        case 11:
            return('Novembro')
        case 12:
            return('Dezembro')
def e4():
    '''
        Faça um programa que leia 12 salários que são os salários equivalente a cada mês de 2023. Apresente em quais meses a pessoa ganhou mais que 5000, e em quais meses houve ganho de salário em relação ao mês anterior.
    '''
    i = 0
    historico_de_salario = []
    meses_com_aumento = []
    meses_superior_a_5000 = []
    while i < 12:
        i += 1
        print('Informe o salário de ' + (pegar_mes(i) + ' : '))
        salario = float( input('R$ '))
        historico_de_salario.append(salario)
        if i != 1:
            if historico_de_salario[i-1] > historico_de_salario[i-2]:
                meses_com_aumento.append( pegar_mes(i) )
        if salario > 5000:
            meses_superior_a_5000.append( pegar_mes(i) )
    print('Os seus salário foram: ')
    i = 0
    while i < 12:
        i += 1
        print(' ' + pegar_mes(i) + ' - R$ ' + str(historico_de_salario[i]))
    print('Você teve um aumento nos seguintes meses: ')
    for valor in meses_com_aumento:
        print(' ' + str(valor) , end = ' ')
    print('Você teve um salário superior a 5000 nos seguintes meses: ')
    for valor in meses_superior_a_5000:
        print(' ' + str(valor) , end = ' ')
def e5():
    '''
        Faça um programa que construa uma lista com elementos (valores) positivos informados pelo usuário. Para encerrar, o usuário deverá digitar 0 (zero). Após construída, gerar a lista reversa da lista informada pelo usuário.
    '''
    lista = []
    print("Digite números positivos para adicionar à lista. Digite 0 para encerrar.")
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0
        elif numero > 0:
            lista.append(numero)  # Adiciona o número positivo à lista
        else:
            print("Por favor, digite apenas números positivos ou 0 para encerrar.")
    lista_reversa = lista[::-1]
    print("Lista original:", lista)
    print("Lista reversa:", lista_reversa)
def e6():
    '''
        Faça um programa que leia um inteiro n, e que então construa uma lista com todos os divisores desse número (testando entre 1 e n, inclusive). Ao final, imprima os divisores na tela, em ordem decrescente
    '''
    n = int(input("Digite um número inteiro: "))
    divisores = []
    i = 0
    while i < n :
        i+=1
        if n % i == 0:  # Verifica se i é um divisor de n
            divisores.append(i)
    
    print("Divisores de", n, "em ordem decrescente: ")
    while len(divisores):
        print(divisores.pop()) 
def exercicio_extra1():
    '''
        Faça a conversão de base dos seguintes sistemas
            Decimal
            Octal
            Binário
            Hexadecimal
    '''
    menu_conversor = int( input('Informe o tipo que valor que você deseja converter.\n1 - Decimal\n2 - Binário\n3 - Octal\n4 - Hexadecimal\nSua resposta: ') )
    match menu_conversor:
        case 1:
            valor_a_converter = int('Informe o valor na base decimal que você deseja converter: ')
            menu_convertido = int( input('Informe o tipo que valor que você deseja receber convertido.\n1 - Decimal\n2 - Binário\n3 - Octal\n4 - Hexadecimal\nSua resposta: ') )
            match menu_convertido:
                case 1:
                    print('o ' + valor_a_converter + ' convertido para decimal é: ',valor_a_converter)
                case 2:
                    valor_convertido = decimal_para_binario(valor_a_converter)
                    print('o ' + valor_a_converter + ' convertido para binário é: ',valor_convertido)
                case 3:
                    valor_convertido = decimal_para_octal(valor_a_converter)
                    print('o ' + valor_a_converter + ' convertido para octal é: ',valor_convertido)
                case 4:
                    valor_convertido = decimal_para_hexadecimal(valor_a_converter)
                    print('o ' + valor_a_converter + ' convertido para binário é: ',valor_convertido)
        case 2:
            valor_a_converter = str('Informe o valor na base binária que você deseja converter: ')
            menu_convertido = int( input('Informe o tipo que valor que você deseja receber convertido.\n1 - Decimal\n2 - Binário\n3 - Octal\n4 - Hexadecimal\nSua resposta: ') )
            match menu_convertido:
                case 2:
                    print('o ' + valor_a_converter + ' convertido para binario é: ',valor_a_converter)
                case 1:
                    valor_convertido = binario_para_decimal(int(valor_a_converter))
                    print('o ' + valor_a_converter + ' convertido para decimal é: ',valor_convertido)
                case 3:
                    valor_convertido = decimal_para_octal(int(binario_para_decimal(valor_a_converter)))
                    print('o ' + valor_a_converter + ' convertido para octal é: ',valor_convertido)
                case 4:
                    valor_convertido = decimal_para_hexadecimal(int(binario_para_decimal(valor_a_converter)))
                    print('o ' + valor_a_converter + ' convertido para hexadecimal é: ',valor_convertido)
        case 3:
            valor_a_converter = str('Informe o valor na base octal que você deseja converter: ')
            menu_convertido = int( input('Informe o tipo que valor que você deseja receber convertido.\n1 - Decimal\n2 - Binário\n3 - Octal\n4 - Hexadecimal\nSua resposta: ') )
            match menu_convertido:
                case 3:
                    print('o ' + valor_a_converter + ' convertido para octal é: ',valor_a_converter)
                case 1:
                    valor_convertido = octal_para_decimal(valor_a_converter)
                    print('o ' + valor_a_converter + ' convertido para decimal é: ',valor_convertido)
                case 3:
                    valor_convertido = decimal_para_octal(int(binario_para_decimal(valor_a_converter)))
                    print('o ' + valor_a_converter + ' convertido para octal é: ',valor_convertido)
                case 4:
                    valor_convertido = decimal_para_hexadecimal(int(binario_para_decimal(valor_a_converter)))
                    print('o ' + valor_a_converter + ' convertido para hexadecimal é: ',valor_convertido)
def decimal_para_binario(decimal):
    bin_vector = []
    while (decimal > 0):
        bin_vector.insert(0,str(decimal%2))
        decimal = decimal//2
    bin_textual = ''
    for caracter in bin_vector:
        bin_textual += caracter
    return bin_textual
def binario_para_decimal(binario):
    pow = len(binario)-1
    decimal = 0
    for caractere in binario:
        decimal += int(caractere)*(2**pow)
        pow-=1
    return decimal
def decimal_para_octal(decimal):
    octal_vetor = []
    while (decimal > 0):
        octal_vetor.insert(0,str(decimal%8))
        decimal = decimal//8
    octal_textual = ''
    for caracter in octal_vetor:
        octal_textual += caracter
    return octal_textual
def octal_para_decimal(octal):
    pow = len(octal)-1
    decimal = 0
    for caractere in octal:
        decimal += int(caractere)*(8**pow)
        pow-=1
    return decimal
def decimal_para_hexadecimal(decimal):
    hexadecimal_vetor = []
    while (decimal > 0):
        hexadecimal_vetor.insert(0,str(decimal%16))
        decimal = decimal//16
    hexadecimal_textual = ''
    for caracter in hexadecimal_vetor:
        if (int(caracter) > 9):
            match caracter:
                case '10': hexadecimal_textual += 'A'
                case '11': hexadecimal_textual += 'B'
                case '12': hexadecimal_textual += 'C'
                case '13': hexadecimal_textual += 'D'
                case '14': hexadecimal_textual += 'E'
                case '15': hexadecimal_textual += 'F'
        else:
            hexadecimal_textual += caracter
    return hexadecimal_textual
def hexadecimal_para_decimal(hexadecimal):
    pow = len(hexadecimal)-1
    decimal = 0
    for caracter in hexadecimal:
        match caracter:
            case 'A': 
                decimal += 10*(16**pow)
            case 'B': 
                decimal += 11*(16**pow)
            case 'C': 
                decimal += 12*(16**pow)
            case 'D': 
                decimal += 13*(16**pow)
            case 'E': 
                decimal += 14*(16**pow)
            case 'F': 
                decimal += 15*(16**pow)
            case _: 
                decimal += int(caracter)*(16**pow)
        pow-=1
    return decimal
def exercicio_extra2(vetor):
    '''
        Implementar o método bubble sort
    '''
    tamanho_vetor = len(vetor)
    for i in range(tamanho_vetor):
        swapped = False
        for j in range(0, tamanho_vetor-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                swapped = True
        if not swapped:
            break
    return vetor
def desafio_lucas():
    '''
        Verificar o tamanho de uma string sem try catch, len, e for. Usando apenas while
    '''
    string = '\0Essa é a string utilizada'
    print ('O tamanho da string é: ' + str(len(string)))
    i = 0
    texto = ''
    print('Prova real!')
    while (True):
        if(string == ''):
            print('Tamanho da string é 0')
        else:
            i+=1
            texto = string[-i] + texto
            print('i atual: '+str(i))
            print('texto atual é: '+texto)
            if(texto == string):
                print('Tamanho da string é: '+str(i))
                break