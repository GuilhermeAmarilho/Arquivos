import os, csv
from time import strftime, gmtime
def pegar_path():
    file_path = os.path.abspath(__file__).lower().split('\\')
    file_path.pop()
    return '\\'.join(file_path)
def ex1_inicializar_Arquivo(nome_Do_Arquivo, metodo):
    try:
        open(nome_Do_Arquivo, 'x')
    except:
        pass
    return open(nome_Do_Arquivo, metodo)
def ex1():
    '''
        Crie um programa que leia um arquivo de texto chamado texto.txt, e conte quantas linhas e palavras ele possui. Mostre o total de linhas e de palavras ao usuário
    '''
    nome = pegar_path()+'\\'+'texto.txt'
    arquivo = ex1_inicializar_Arquivo(nome, 'r').readlines()
    total_Linhas = len(arquivo)
    total_Palavras = len('\n'.join(arquivo).split(' '))
    if total_Palavras == 0:
        print(f'O arquivo {nome} ainda não possui nada escrito')
    print(f'O arquivo {nome} possui {total_Linhas} linhas e {total_Palavras} palavras')
def ex2_crud_Diario(type, nome_Arquivo, content = '', line = -1, visual = False):
    file_path = os.path.abspath(__file__).lower().split('\\')
    local = '\\'.join(file_path[:file_path.index('alg_ed1') + 1]) + '\\' + nome_Arquivo
    try: 
        file = open(local, 'x')
        file.close()
    except:
        pass
    match type:
        case 0:
            file = open(local, 'a')
            data = strftime("%d/%m/%Y %H:%M:%S", gmtime()) + ' -> ' + content + '\n'
            file.write(data)
            file.close()
        case 1:
            file = open(local, 'r')
            if line == -1:
                string = ''.join(file.readlines())
                file.close()
                return string
            else:
                try:
                    string = file.readlines()[line].split(' -> ')[1]
                    file.close()
                    return string
                except:
                    return '\nLinha não encontrada'
        case 2:
            try:                
                file = open(local, 'r')
                diario = file.readlines()
                diario[line] = strftime("%d/%m/%Y %H:%M:%S", gmtime()) + ' -> ' + content + '\n'
                file = open(local, 'w', encoding='utf-8')
                file.writelines(diario)
                file.close()
                return string
            except:
                return '\nLinha não encontrada'
        case 3:
            if line == -1:
                file = open(local, 'w')
                file.write('')
                file.close()
                return '\nTodas as linhas foram excluidas excluido!'
            else:
                try:
                    file = open(local, 'r')
                    diario = file.readlines()
                    diario[line] = ''
                    file.close()
                    file = open(local, 'w', encoding='utf-8')
                    file.writelines(diario)
                    file.close()
                    return f'\nA linha {line} do diário foi excluida com sucesso!'
                except:
                    return '\nLinha não encontrada'
        case 4:
            return
def ex2_Listar_Insercoes(nome_Arquivo):
    file_path = os.path.abspath(__file__).lower().split('\\')
    local = '\\'.join(file_path[:file_path.index('alg_ed1') + 1]) + '\\' + nome_Arquivo
    file = open(local, 'r')
    list = []
    for content in file.readlines():
        list.append(
            content.split(' -> ')[0]
        )
    return list
def ex2_menu_inicial():
    nome = str(input('Informe seu nome: '))
    path = pegar_path()+'\\'+'diario.txt'
    while True:
        os.system('cls')
        value = int(
            input(
                f'Olá, bem vindon ao diário d@ {nome}.'
                +'\n0 - Escrever no diário.'
                +'\n1 - Ler diário.'
                +'\n2 - Atualizar linha do diário.'
                +'\n3 - Excluir registros do diário.'
                +'\n4  - Sair'
                +'\nSua resposta: '
            )
        )
        match value:
            case 0:
                content = str(input('Informe o que deseja anotar no diário.\nSua anotação: '))
                ex2_crud_Diario(0, path, content)
            case 1:
                lines = ex2_Listar_Insercoes(path)
                if len(lines) == 0:
                    print('Não há registros no seu diário')
                else:
                    type = int(
                        input(
                            'Você quer ler uma linha especifica ou todo o diário?'
                            +'\n1 - Todo o diário'
                            +'\n2 - Apenas uma linha'
                            +'\nSua resposta: '
                        )
                    )
                    if type == 1:
                        linha = -1
                    if type == 2:
                        os.system('cls')
                        print('Informe a linha que deseja ler', end='')
                        i = 0
                        for line in lines:
                            print(f'\n{i} - {line}', end='')
                            i+=1
                        linha = int(input('\nInforme sua resposta: '))
                    string = ex2_crud_Diario(1, path, '', linha)
                    print(string)
            case 2:
                lines = ex2_Listar_Insercoes(path)
                if(len(lines) != 0):
                    print('Informe a linha que deseja alterar', end='')
                    i = 0
                    for line in lines:
                        print(f'\n{i} - {line}', end='')
                        i+=1
                    linha = int(input('\nInforme sua resposta: '))
                    try:
                        string = ex2_crud_Diario(1, path, '', linha)
                        new_String = str(input(f'Linha antiga: {string}'+'Nova linha: '))
                        ex2_crud_Diario(2, path, new_String, linha)
                    except:
                        print("Erro ao atualizar linha!")
                else:
                    print('ainda não há o que alterar')
            case 3: 
                lines = ex2_Listar_Insercoes(path)
                if len(lines) == 0:
                    print('Não há registros no seu diário')
                else:
                    type = int(
                        input(
                            'Você quer excluir uma linha especifica ou todo o diário?'
                            +'\n1 - Todo o diário'
                            +'\n2 - Apenas uma linha'
                            +'\nSua resposta: '
                        )
                    )
                    if type == 1:
                        linha = -1
                    if type == 2:
                        print('Informe a linha que deseja excluir', end='')
                        lines = ex2_Listar_Insercoes(path)
                        i = 0
                        for line in lines:
                            print(f'\n{i} - {line}', end='')
                            i+=1
                        linha = int(input('\nInforme sua resposta: '))
                    ex2_crud_Diario(3, path, '', linha)
            case 4:
                return
        input('Pressione Enter para continuar!')
def ex2():
    '''
        Escreva um programa que permita ao usuário inserir uma entrada de diário em um arquivo chamado diario.txt. Cada vez que o programa é executado, ele deve adicionar uma nova entrada ao final do arquivo (use o modo “a”). Pergunte ao usuário o que ele gostaria de escrever, e adicione (leia) a data e a hora no início da entrada, no arquivo.
    '''
    ex2_menu_inicial()
def ex3():
    '''
        Escreva um programa que leia o conteúdo de um arquivo, sendo o seu nome informado pelo usuário. Substitua todas as ocorrências de uma palavra específica por outra palavra, sendo ambas fornecidas pelo usuário. Salve o conteúdo alterado em um novo arquivo, sendo que o seu nome também seja informadopelo usuário.
    '''
    try:
        nome = str(input('Informe seu nome: '))
        path = pegar_path()+'\\'+'Arquivo.txt'
        palavra_Chave = str(input(f'Informe a palavra que deseja alterar por {nome}: '))
        arquivo = open(path, 'r')
        conteudo = arquivo.readlines()
        arquivo = open(path, 'w')
        novo_Texto = []
        for linhas in conteudo:
            lista_De_Palavras = linhas.split(' ')
            nova_Linha = []
            for palavra in lista_De_Palavras:
                if(palavra == '\n'):
                    pass
                else:
                    if palavra == palavra_Chave:
                        nova_Linha.append(nome)
                    else:
                        nova_Linha.append(palavra)
            nova_Linha = ' '.join(nova_Linha)
            novo_Texto.append(nova_Linha)
        novo_Texto = ''.join(novo_Texto)
        arquivo.write(novo_Texto)
    except:
        arquivo = open('Arquivo.txt', 'x')
        print("O arquivo não havia sido criado ainda.")
def ex4():
    '''
        Escreva um programa que leia números armazenados em um arquivo, sendo o nome deste arquivo informado pelo usuário. Neste arquivo, cada linha contém um número. Some todos os números, e apresente o resultado. Caso o arquivo esteja vazio, informe para o usuário.
    '''
    # file_Name = str(input('Informe o nome do arquivo: '))
    file_Name = 'Itens'
    file_Path = pegar_path() + '\\' + file_Name + '.txt'
    try:
        arquivo = open(file_Path, 'r')
        linhas = arquivo.readlines()
        somatorio = 0
        if len(linhas) == 0:
            return 'Nao ha numeros registrados ainda!'
        else:
            for linha_Atual in linhas:
                linha_Atual = linha_Atual.replace('\n',"")   
                if linha_Atual.isnumeric():
                    somatorio += int(linha_Atual)
            return f'O valor total é: {somatorio}'
    except:
        print("O arquivo não existe.")
        value = int(input('Deseja criar o arquivo?\n1 - Sim\n2 - Não\nSua resposta:'))
        if value == 1:
            try:
                arquivo = open(file_Path, 'x')
                print('Arquivo criado!')
            except:
                print('Não foi possivel criar o arquivo')
        else:
            print('Entendido!')
def ler_csv(nome_arquivo):
    nomes = []
    idades = []
    with open(nome_arquivo, mode='r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            nomes.append(linha['nome'])
            idades.append(int(linha['idade']))
    return nomes, idades
def calcular_media(idades):
    if len(idades) > 0:
        return sum(idades) / len(idades) 
    else:
        return 0
def exibir_dados(nomes, media_idades):
    print("Nomes:")
    for nome in nomes:
        print(f"- {nome}")
    print(f"\nMédia das idades: {media_idades:.2f} anos")
def ex5():
    '''
        Crie um programa que leia um arquivo CSV chamado dados.csv, contendo uma lista de nomes e de idades. Exiba todos os nomes e a média das idades.
    '''
    path = pegar_path() + '\\' + 'dados.csv'
    nomes, idades = ler_csv(path)
    media_idades = calcular_media(idades)
    exibir_dados(nomes, media_idades)