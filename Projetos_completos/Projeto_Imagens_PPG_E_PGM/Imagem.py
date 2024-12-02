import os, sys
# -*- coding: utf-8 -*-
class Imagem: 
    
    def __init__(self,arqEntrada):
        # Recebe o nome do arquivo de entrada
        # e cria o atributo arqEntrada
        self.arqEntrada = arqEntrada #Não alterar essa linha
        # Pode editar a partir daqui para criar outros atributos, se desejar.
        self.caminho = self.definir_Caminho()
        if self.validar_Arquivo():
            self.largura =  int(self.definir_Largura())
            self.altura = int(self.definir_Altura())
            self.maxValue = int(self.definir_Max_Value())
            self.tipo = self.definir_Tipo()
            self.pixeis = self.definir_Pixeis()
    
    # Pode editar para criar outros métodos se desejar.
    
    def definir_Caminho(self):
        tipo = self.arqEntrada.split('.')[1]
        if tipo == 'pgm' or tipo == 'PGM':
            return '\\TonsDeCinza\\'
        if tipo == 'ppm' or tipo == 'PPM':
            return '\\Coloridas\\'
    
    def validar_Arquivo(self):
        try:
            file = open(self.pegar_Path_Inicial(), 'r')
            file.close()
            return True
        except:
            return False
    
    def pegar_Path_Base(self):
        file_path = os.path.abspath(__file__).lower().split('\\')
        file_path.pop()
        return '\\'.join(file_path) 
    
    def pegar_Path_Inicial(self):
        return self.pegar_Path_Base() + '\\Imagens\\' + self.definir_Caminho() + self.arqEntrada
    
    def minificar(self):
        file = open(self.pegar_Path_Inicial(), 'r')
        content = []
        for line in file.readlines():
            if line != '\n':
                line = (line.replace('\n', '')).split(' ')
                for item in line:
                    content.append(item)
        file.close()
        return content
    
    def definir_Tipo(self):
        return self.minificar()[0]
    
    def definir_Largura(self):
        return self.minificar()[1]
    
    def definir_Altura(self):
        return self.minificar()[2]
    
    def definir_Max_Value(self):
        return self.minificar()[3]
    
    def definir_Pixeis(self):
        content = []
        for pixel in self.minificar()[4:]:
            if pixel != '':
                content.append(str(pixel))
        return content
    
    def criar_Arquivo_Saida(self, arqSaida):
        try:
            file = open(self.pegar_Path_Base()+'\\'+arqSaida, 'x')
            file.close()
        except:
            pass
    
    def gerar_Cabecalho(self, largura, altura):
        content = self.tipo + '\n' + str(largura) + ' ' + str(altura) + '\n' + str(self.maxValue) + '\n'
        return content

# Classe ImagemPGM herda a classe Imagem
class ImagemPGM(Imagem):

    def __init__(self,arqEntrada):
        # Recebe o nome do arquivo de entrada
        # e cria o atributo arqEntrada chamando o construtora
        # da classe imagem.
        super().__init__(arqEntrada) #Não alterar essa linha
        # Pode editar a partira daqui para criar outros atributos, se desejar.

    ################################################
    ####### ----  EDITAR A PARTIR DAQUI  ---- ######
    ################################################

    # Método que altera o brilho de uma imagem PGM
    # Seu método deve abrir o arquivo de entrada
    # e criar o arquivo de saída.
    # Caso o arquivo de entrada não exista ou seja inválido,
    # retornar False.
    def brilho(self,arqSaida,valor):
        ok=True
        ## Escreva seu código aqui.
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.largura, self.altura))
            content = []
            for pixel in self.pixeis:
                if ((int(pixel) + valor < self.maxValue) and (int(pixel) + valor > 0)):
                    new_Pixel = int(pixel) + valor
                else:
                    if int(pixel) + valor < 0:
                        new_Pixel = 0
                    if int(pixel) + valor >= self.maxValue:
                        new_Pixel = self.maxValue
                content.append(str(new_Pixel))
            content = self.formatar_PGM(content)
            file.write(content)
            file.close()
        else:
            ok = False
        return ok

    # Método que espelha uma imagem PGM
    # Seu método deve abrir o arquivo de entrada
    # e criar o arquivo de saída.
    # Caso o arquivo de entrada não exista ou seja inválido,
    # retornar False.
    def espelha(self,arqSaida):
        ok=True
        ## Escreva seu código aqui.
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.largura, self.altura))
            content = []
            pixeis = self.formatar_PGM(self.pixeis).split('\n')
            for line in pixeis:
                if line != '':
                    line = line.split(' ')
                    i = len(line)
                    while i > 0:
                        i -= 1
                        content.append(line[i])
            file.write(self.formatar_PGM(content))
            file.close()
        else:
            ok = False
        return ok

    ## Podem ser criados outros métodos
    def rotaciona90(self,arqSaida):
        ok=True
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.altura, self.largura))
            matriz = []
            for line in self.formatar_PGM(self.pixeis).split('\n'):
                if line != '':
                    line = line.split(' ')
                    matriz.append(line)
            content = []
            i = 0
            while i < self.largura:
                j = 0
                while j < self.altura:
                    content.append(matriz[j][i])
                    j += 1
                i += 1
            file.write(self.formatar_PGM_90graus(content))
            file.close()
        else:
            ok = False
        return ok
    
    def formatar_PGM(self, saida):
        i = 0
        content = ''
        while i < len(saida):
            if i % self.largura == 0 and i != 0:
                content += '\n'
            if i % self.largura == self.largura - 1:
                content += saida[i]
            else:
                content += saida[i] + ' '
            i += 1
        return content
    
    def formatar_PGM_90graus(self, saida):
        i = 0
        content = ''
        while i < len(saida):
            if i % self.altura == 0 and i != 0:
                content += '\n'
            if i % self.altura == self.altura - 1:
                content += saida[i]
            else:
                content += saida[i] + ' '
            i += 1
        return content

# Classe ImagemPPM herda a classe Imagem
class ImagemPPM(Imagem):

    def __init__(self,arqEntrada):
        # Recebe o nome do arquivo de entrada
        # e cria o atributo arqEntrada chamando o construtora
        # da classe imagem.
        super().__init__(arqEntrada) #Não alterar essa linha
        # Pode editar a partira daqui para criar outros atributos, se desejar.

    ################################################
    ####### ----  EDITAR A PARTIR DAQUI  ---- ######
    ################################################

    # Método que espelha uma imagem PPM
    # Seu método deve abrir o arquivo de entrada
    # e criar o arquivo de saída.
    # Caso o arquivo de entrada não exista ou seja inválido,
    # retornar False.
    def espelha(self,arqSaida):
        ok=True
        ## Escreva seu código aqui
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.largura, self.altura))
            pixeis = self.formatar_PPM(self.pixeis)
            while len(pixeis) > 0:
                line = pixeis[0:self.largura]
                pixeis = pixeis[self.largura:]
                line = line[::-1]
                file.write(self.stringficar_Linha(line))
            file.close()
        else:
            ok = False
        return ok

    # Método que rotaciona 90o uma imagem PPM
    # Seu método deve abrir o arquivo de entrada
    # e criar o arquivo de saída.
    # Caso o arquivo de entrada não exista ou seja inválido,
    # retornar False.

    def rotaciona90(self,arqSaida):
        ok=True
        ## Escreva seu código aqui.
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.altura, self.largura))
            pixeis = self.formatar_PPM(self.pixeis)
            eixo_X = 0
            while eixo_X < self.largura:
                eixo_Y = 0
                linha = []
                while eixo_Y < self.altura:
                    linha.append(pixeis[(eixo_Y * self.largura) + eixo_X])
                    eixo_Y += 1
                file.write(self.stringficar_Linha(linha))
                eixo_X += 1
            file.close()
        else:
            ok=False
        return ok

    ## Podem ser criados outros métodos

    def brilha(self,arqSaida, valor):
        ok=True
        if self.validar_Arquivo():
            self.criar_Arquivo_Saida(arqSaida)
            file = open(self.pegar_Path_Base() + '\\' + arqSaida, 'w')
            file.write(self.gerar_Cabecalho(self.largura, self.altura))
            content = []
            pixeis = self.formatar_PPM(self.pixeis)
            for pixel in pixeis:
                new_pixel = []
                for subPixel in pixel:
                    if ((int(subPixel) + valor < 0) or (int(subPixel) + valor >= self.maxValue)):
                        if int(subPixel) + valor < 0:
                            new_pixel.append('0')
                        if int(subPixel) + valor >= self.maxValue:
                            new_pixel.append(self.maxValue)
                    else:
                        new_pixel.append(str(int(subPixel)+valor))
                content.append(new_pixel)
            file.write(self.stringficar(content))
            file.close()
        else:
            ok = False
        return ok

    def formatar_PPM(self, saida):
        i = 0
        content = []
        while len(saida) > 0:
            content.append(saida[0:3])
            saida = saida[3:]
        return content
    
    def stringficar_Linha(self, saida):
        content = ''
        for pixel in saida:
            for subpixel in pixel:
                content += str(subpixel) + ' '
        content += '\n'
        return content

    def stringficar(self, saida):
        content = ''
        while len(saida) > 0:
            line = saida[0:self.largura]
            saida = saida[self.largura:]
            for pixel in line:
                for subpixel in pixel:
                    content += str(subpixel) + ' '
            content += '\n'
        return content