import random, os, json, math
def pegar_path():
    file_path = os.path.abspath(__file__).lower().split('\\')
    file_path.pop()
    return '\\'.join(file_path)
class Pessoa:
    def __init__(self, nome, genero, classe, ataque, vida, defesa, vivo = True):
        self.nome = nome
        self.genero = genero
        self.classe = classe
        self.ataque = ataque
        self.vida = vida
        self.defesa = defesa
        self.vivo = vivo
    def get_nome(self):
        return self.nome
    def get_vida(self):
        return self.vida
    def set_vida(self, vida):
        self.vida = float("{:.2f}".format(vida))
    def get_ataque(self):
        return self.ataque
    def get_defesa(self):
        return self.defesa
    def atacar(self, defensor):
        dano = float("{:.2f}".format(random.randrange(101)/100 * self.get_ataque()))
        if (defensor.get_vida() - dano) > 0:
            defensor.set_vida(defensor.get_vida() - dano)
            print(f'{self.get_nome()} atacou {defensor.get_nome()}, causando {dano} de dano e deixando-o com {defensor.get_vida()} de vida')
        else:
            defensor.set_vida(0)
            print(f'{self.get_nome()} executou {defensor.get_nome()}')
    def defender(self, atacante):
        dano = (random.randrange(101)/100) * atacante.get_ataque()
        if (self.vida - dano) > 0:
            self.set_vida(self.vida - dano)
            print(f'{self.nome} foi atacado por {atacante.get_nome()}, recebendo {dano} de dano!')
        else:
            print(f'{self.nome} foi executado por {atacante.get_nome()}')
    def __str__(self):
        if self.vivo:
            return f"Nome: {self.nome}, Classe: {self.classe}, Ataque: {self.ataque}, Vida: {self.vida}, Defesa: {self.defesa}"
        else:
            string = ''
            if self.genero == 'f':
                string+='A '
            else:
                string+='O '
                string+= f"{self.nome} está morto!"
def ex1():
    '''
        Faça um programa que simule um jogo de RPG utilizando orientação a objetos (OO), onde teremos um personagem com atributos como vida, ataque e defesa, e eles poderão batalhar entre si.
        Classe:
        1. Classe Personagem: Representa o personagem no jogo, com atributos de vida, ataque e defesa.
    '''
    p1 = Pessoa('Guilherme', 'm', 'Guerreiro', 15, 50, 1)
    p2 = Pessoa('Pereira', 'm', 'Bardo', 7.5, 100, 4)
    i = 0
    while True:
        if p1.get_vida() > 0 and p2.get_vida() > 0:
            p1.atacar(p2)
            p2.atacar(p1)
            print()
            i+=1
        else:
            break
class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def get_nome(self):
        return self.nome
    def get_preco(self):
        return self.preco
    def __str__(self):
        return f"{self.get_nome()}"
class Estoque():
    def __init__(self, descricao):
        self.descricao = descricao
        self.produtos = []
    def get_descricao(self):
        return self.descricao
    def add_produto(self, produto, quantidade):
        estoque_Do_Produto = {
            'Produto': produto,
            'Quantidade': quantidade
        }
        if len(self.get_produtos()) == 0:
            self.produtos.append(estoque_Do_Produto)
            return True
        else:
            for produto_Em_Estoque in self.produtos:
                if produto_Em_Estoque['Produto'] == produto:
                    produto_Em_Estoque['Quantidade'] += quantidade
                    return True
            self.produtos.append(estoque_Do_Produto)
    def rem_produto(self, produto, quantidade):
        for produto_Em_Estoque in self.produtos:
            if produto_Em_Estoque['Produto'] == produto:
                if produto_Em_Estoque['Quantidade'] - quantidade >= 0:
                    produto_Em_Estoque['Quantidade'] -= quantidade
                    return True
                else:
                    return False
        return False
    def get_produtos(self):
        return self.produtos
    def __str__(self):
        string = f'Estoque: {self.get_descricao()}'
        if len(self.get_produtos()) != 0:
            string += '\n############## Produtos ##############'
            for produto in self.get_produtos():
                string+= f'\nProduto: {produto['Produto'].get_nome()} - Quantidadde: {produto['Quantidade']}'
        else:
            string += '\nAinda sem produtos no estoque!'
        return string
def  ex2():
    '''
        Faça um programa para gerenciar um estoque de produtos. Cada produto possui informações como nome, preço e quantidade. 
        A classe Estoque será responsável por gerenciar as operações CRUD (Criar, Ler, Atualizar, Deletar) sobre os produtos. 
        Utilize arquivos. 
        Seu programa deve ter pelo menos as seguintes classes: 
            1. Classe Produto: Representa um produto com os atributos e métodos necessários. 
            2. Classe Estoque: Gerencia os produtos e realiza as operações CRUD
    '''
    os.system('cls')
    maca = Produto('Maçã argentina', 5.99)
    mamao = Produto('Mamão papaya', 4.99)
    pera = Produto('Banana prata', 2.99)
    abacaxi = Produto('Abacaxi', 6.99)
    estoque = Estoque('Hortifruti')
    estoque.add_produto(maca, 5)
    estoque.add_produto(mamao, 4)
    estoque.add_produto(pera, 9)
    estoque.add_produto(maca, 2) # 7 
    estoque.rem_produto(abacaxi, 4) # erro
    estoque.add_produto(abacaxi, 3) 
    estoque.rem_produto(maca, 4) # 3
    estoque.rem_produto(mamao, 6) # erro
    estoque.rem_produto(maca, 3)
    print(estoque)
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    def sacar(self, valor):
        if ((valor <= self.saldo) and (valor > 0)):
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R$ {self.saldo:.2f}")
        return self.saldo
class Banco:
    def __init__(self, arquivo_banco=(pegar_path()+'\\'+'contas.json')):
        self.arquivo_banco = arquivo_banco
        self.contas = self.carregar_contas()
    def carregar_contas(self):
        if os.path.exists(self.arquivo_banco):
            with open(self.arquivo_banco, 'r') as file:
                return json.load(file)
        return {}
    def salvar_contas(self):
        with open(self.arquivo_banco, 'w') as file:
            json.dump(self.contas, file, indent=4)
    def criar_conta(self, titular, saldo_inicial=0):
        if titular in self.contas:
            print("Conta já existente para esse titular.")
        else:
            self.contas[titular] = {'saldo': saldo_inicial}
            self.salvar_contas()
            print(f"Conta criada para {titular} com saldo inicial de R$ {saldo_inicial:.2f}.")
    def depositar(self, titular, valor):
        if titular in self.contas:
            conta = ContaBancaria(titular, self.contas[titular]['saldo'])
            conta.depositar(valor)
            self.contas[titular]['saldo'] = conta.saldo
            self.salvar_contas()
        else:
            print(f"Conta não encontrada para {titular}.")
    def sacar(self, titular, valor):
        if titular in self.contas:
            conta = ContaBancaria(titular, self.contas[titular]['saldo'])
            conta.sacar(valor)
            self.contas[titular]['saldo'] = conta.saldo
            self.salvar_contas()
        else:
            print(f"Conta não encontrada para {titular}.")
    def consultar_saldo(self, titular):
        if titular in self.contas:
            conta = ContaBancaria(titular, self.contas[titular]['saldo'])
            conta.consultar_saldo()
        else:
            print(f"Conta não encontrada para {titular}.")
def ex3():
    '''
    Faça um programa para gerenciar as contas bancárias de um Banco. A ideia é ter um sistema básico para criar contas, depositar e sacar dinheiro, além de consultar o saldo. Use arquivos.
    Classe ContaBancaria: Representa uma conta bancária com, pelo menos, titular (nome do dono da conta) e saldo (quantia de dinheiro na conta).
    Classe Banco: Contém várias contas.
    Operações CRUD:
        Criar conta.
        Depositar: Adiciona um valor ao saldo.
        Sacar: Subtrai um valor do saldo.
        Consultar saldo: Exibe o saldo da conta.
    '''
    banco = Banco()
    while True:
        os.system('cls')
        opcao = input('===== Menu do Banco =====\n1 - Criar Conta\n2 - Depositar\n3 - Sacar\n4 - Consultar Saldo\n5 - Sair\nEscolha uma opção: ')
        if opcao == '1':
            nome = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial: "))
            banco.criar_conta(nome, saldo_inicial)
            input('Pressione enter para continuar! ')
        elif opcao == '2':
            nome = input("Nome do titular: ")
            valor = float(input("Valor a depositar: "))
            banco.depositar(nome, valor)
            input('Pressione enter para continuar! ')
        elif opcao == '3':
            nome = input("Nome do titular: ")
            valor = float(input("Valor a sacar: "))
            banco.sacar(nome, valor)
            input('Pressione enter para continuar! ')
        elif opcao == '4':
            nome = input("Nome do titular: ")
            banco.consultar_saldo(nome)
            input('Pressione enter para continuar! ')
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
class Tempo:
    def __init__(self, hora=0, minuto=0):
        self.hora = hora
        self.minuto = minuto
        self.ajustar_tempo()
    def ajustar_tempo(self):
        if self.minuto >= 60:
            self.hora += self.minuto // 60
            self.minuto = self.minuto % 60
        self.hora = self.hora % 24
    def mostrar(self):
        print(f"{self.hora:02d}:{self.minuto:02d}")
    def adicionar_minutos(self, m):
        self.minuto += m
        self.ajustar_tempo()
def ex4():
    '''
        Implemente uma classe Tempo que contém os atributos hora e minuto (valores inteiros). Crie o método mostrar() que exibe o tempo no formato hh:mm.
        Implemente e teste um método adicionar_minutos(m), que acrescenta um valor inteiro de minutos e mantém o tempo consistente.
    '''
    tempo = Tempo(14, 30)
    tempo.mostrar()
    tempo.adicionar_minutos(40)
    tempo.mostrar()
    tempo.adicionar_minutos(120)
    tempo.mostrar()
    tempo.adicionar_minutos(180)
    tempo.mostrar()
class Ponto:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y
    def definir_x(self, x):
        self._x = x
    def obter_x(self):
        return self._x
    def definir_y(self, y):
        self._y = y
    def obter_y(self):
        return self._y
    def distancia(self, p):
        return math.sqrt((self._x - p.obter_x())**2 + (self._y - p.obter_y())**2)
def ex5():
    '''
        Crie uma classe Ponto que representa um ponto no plano bidimensional, de coordenadas x e y reais.
        Crie métodos públicos definir_x(), obter_x(), definir_y() e obter_y() para consulta e alteração.
        Adicione um método distância(p) para calcular a distância Euclidiana entre o objeto desta classe e um outro ponto p.
    '''
    ponto1 = Ponto(1, 2)
    ponto2 = Ponto(4, 6)
    print("Ponto 1:", ponto1.obter_x(), ponto1.obter_y())
    print("Ponto 2:", ponto2.obter_x(), ponto2.obter_y())
    dist = ponto1.distancia(ponto2)
    print(f"Distância entre Ponto 1 e Ponto 2: {dist:.2f}")
class Personagem:
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
    def definir_x(self, x):
        self._x = x
    def obter_x(self):
        return self._x
    def definir_y(self, y):
        self._y = y
    def obter_y(self):
        return self._y
    def definir_vx(self, vx):
        self._vx = vx
    def obter_vx(self):
        return self._vx
    def definir_vy(self, vy):
        self._vy = vy
    def obter_vy(self):
        return self._vy
    def mover_Em_Linha_Reta(self, i, j):
        self._x += i
        self._y += j
        print(f"Movido para a nova posição: ({self._x}, {self._y})")
    def mover_Com_Velocidade(self):
        self._x += self._vx
        self._y += self._vy
        print(f"Movido para a nova posição: ({self._x}, {self._y})")
    def detectar_colisao(self, outro_personagem):
        if self._x == outro_personagem.obter_x() and self._y == outro_personagem.obter_y():
            print("Colisão detectada!")
        else:
            print("Sem colisão.")
def ex6():
    '''
        Crie uma classe Personagem que representa a posição de um personagem em um plano bidimensional, de coordenadas x e y reais.
        Crie métodos públicos definir_x(), obter_x(), definir_y() e obter_y() para consulta e alteração.
        Adicione um método move(i,j) que muda a posição do personagem em x e y, respectivamente.
    '''
    personagem = Personagem(2, 3)
    print(f"Posição inicial: ({personagem.obter_x()}, {personagem.obter_y()})")
    personagem.mover_Em_Linha_Reta(3, 4)
    personagem.mover_Em_Linha_Reta(-2, -1)
    print(f"Posição final: ({personagem.obter_x()}, {personagem.obter_y()})")
def ex7():
    '''
        Modifique a classe Personagem implementada anteriormente, criando mais dois atributos, vx para definir a velocidade em x e vy para definir a velocidade em y.
        Crie métodos públicos definir_vx(), obter_vx(), definir_vy() e obter_vy() para consulta e alteração.
        Adicione um método move() que muda a posição do personagem em x e y, de acordo com sua velocidade, ou seja, x = x + vx e y = y+vy
    '''
    personagem = Personagem(2, 3, 1, 2)
    print(f"Posição inicial: ({personagem.obter_x()}, {personagem.obter_y()})")
    print(f"Velocidade em x {personagem.obter_vx()} e em y {personagem.obter_vy()}")
    personagem.mover_Com_Velocidade()
    personagem.mover_Com_Velocidade()
    print(f"Posição final: ({personagem.obter_x()}, {personagem.obter_y()})")
def ex8():
    '''
        Modifique a classe Personagem implementada anteriormente, criando um método para detectar colisão com um outro personagem
    '''
    personagem1 = Personagem(2, 3, 1, 2)
    personagem2 = Personagem(4, 5, -1, -2)
    print(f"Posição inicial do personagem 1: ({personagem1.obter_x()}, {personagem1.obter_y()})")
    print(f"Posição inicial do personagem 2: ({personagem2.obter_x()}, {personagem2.obter_y()})")
    personagem1.mover_Com_Velocidade()
    personagem2.mover_Com_Velocidade()
    personagem1.detectar_colisao(personagem2)
    personagem1.mover_Com_Velocidade()
    personagem2.mover_Com_Velocidade()
    personagem1.detectar_colisao(personagem2) # Sem colisão
    personagem2.mover_Em_Linha_Reta(2, 6)
    personagem1.detectar_colisao(personagem2) # Colisão