import pyxel, random
from tkinter import messagebox
def ex1():
    '''
        Desenhe um círculo.
    '''
    pyxel.init(120, 120)  # Inicializa uma janela de 120x120 pixels
    pyxel.cls(0)  # Limpa a tela com a cor preta
    pyxel.circ(60, 60, 45, 5)  # Desenha um círculo na posição (60, 60), com raio 30, cor 5 azul
    pyxel.show()
def ex2():
    '''
        Faça um círculo animado andar para a direita.
        Essa função inicializa e roda o jogo apenas quando chamada.
    '''
    pyxel.init(120, 120)
    global ex2_x, ex2_y, ex2_aceleracao
    ex2_x = 0
    ex2_y = 60
    ex2_aceleracao = 2
    pyxel.run(ex2_Update, ex2_Draw)
def ex2_Update():
    global ex2_x, ex2_aceleracao
    ex2_x += ex2_aceleracao
    if ex2_x > pyxel.width:
        ex2_x = -15 
def ex2_Draw():
    global ex2_x, ex2_y
    pyxel.cls(7)  # Limpa a tela com a cor branca
    pyxel.circ(ex2_x, ex2_y, 15, 0)
def ex3():
    '''
        Faça um círculo animado andar para a direita e à esquerda (bate na  janela e volta).
    '''
    pyxel.init(120, 120)
    global ex3_x, ex3_y, ex3_aceleracao_x, ex3_aceleracao_y
    ex3_x = 60
    ex3_y = 20
    ex3_aceleracao_x = 5
    ex3_aceleracao_y = 5
    pyxel.run(ex3_Update, ex3_Draw)
def ex3_Update():
    global ex3_x, ex3_y, ex3_aceleracao_x, ex3_aceleracao_y
    if ((ex3_x + ex3_aceleracao_x + 10 > 120) or (ex3_x + ex3_aceleracao_x  - 10 < 0)):
        ex3_aceleracao_x *= -1
    if ((ex3_y + ex3_aceleracao_y + 10 > 120) or (ex3_y + ex3_aceleracao_y  - 10 < 0)):
        ex3_aceleracao_y *= -1
    ex3_x += ex3_aceleracao_x
    ex3_y += ex3_aceleracao_y
def ex3_Draw():
    global ex3_x, ex3_y
    pyxel.cls(7)
    pyxel.circ(ex3_x, ex3_y, 10, 0)
def ex4():
    '''
        Faça um círculo se mover com as teclas de movimentação. Não deixe sair da janela
    '''
    pyxel.init(120, 120)
    global ex4_x, ex4_y, ex4_aceleracao
    ex4_x = 60
    ex4_y = 20
    ex4_aceleracao = 2
    pyxel.run(ex4_Update, ex4_Draw)
def ex4_Update():
    global ex4_x, ex4_y, ex4_aceleracao
    if (pyxel.btn(pyxel.KEY_LEFT) and (ex4_x - ex4_aceleracao - 10 >= 0)):
        ex4_x -= ex4_aceleracao
    if (pyxel.btn(pyxel.KEY_RIGHT) and (ex4_x + ex4_aceleracao + 10 <= 120)):
        ex4_x += ex4_aceleracao
    if (pyxel.btn(pyxel.KEY_UP) and (ex4_y - ex4_aceleracao - 10 >= 0)):
        ex4_y -= ex4_aceleracao
    if (pyxel.btn(pyxel.KEY_DOWN) and (ex4_y + ex4_aceleracao + 10 <= 120)):
        ex4_y += ex4_aceleracao
def ex4_Draw():
    global ex4_x, ex4_y
    pyxel.cls(7)
    pyxel.circ(ex4_x, ex4_y, 10, 0)
def ex5():
    '''
        Faça um círculo se mover com as teclas de movimentação, mas coloque alguns obstáculos (paredes). Não deixe sair da janela.
    '''
    global raio, x, y, velocidade, obstaculos, largura, altura
    largura = 1280
    altura = 720
    raio= 15
    x = 30
    y = 30
    velocidade = 5
    obstaculos = []
    for _ in range(20):
        x_obs = (random.randint(0, largura)//velocidade)*velocidade
        y_obs = (random.randint(0, altura)//velocidade)*velocidade
        w_obs = (random.randint(50, 200)//velocidade)*velocidade
        h_obs = (random.randint(20, 100)//velocidade)*velocidade
        obstaculos.append((x_obs, y_obs, w_obs, h_obs))
    pyxel.init(largura, altura)
    pyxel.run(ex5_Update, ex5_Draw)
def ex5_Update():
    global x, y, velocidade, raio
    novo_x = x
    novo_y = y
    if pyxel.btn(pyxel.KEY_LEFT):
        novo_x -= velocidade
    if pyxel.btn(pyxel.KEY_RIGHT):
        novo_x += velocidade
    if pyxel.btn(pyxel.KEY_UP):
        novo_y -= velocidade
    if pyxel.btn(pyxel.KEY_DOWN):
        novo_y += velocidade
    if ex5_Verifica_Colisao_Com_Parede(novo_x, novo_y):
        x = novo_x
        y = novo_y
def ex5_Draw():
    global x, y, raio
    pyxel.cls(7)
    desenha_paredes()
    pyxel.circ(x, y, raio, 3)
def desenha_paredes():
    global obstaculos
    for parede in obstaculos:
        pyxel.rect(parede[0], parede[1], parede[2], parede[3], 0)
def ex5_Verifica_Colisao_Com_Parede(x, y):
    global raio, obstaculos
    for parede in obstaculos:
        px, py, pw, ph = parede
        if((y+raio > py and y-raio < py+ph) and (x+raio > px and x-raio < px+pw)):
            return False
    return True
def ex6():
    '''
        Faça um jogo de labirinto completo
    '''
    global largura, altura, raio, velocidade, labirinto, x, y, labirinto
    raio = 15
    labirinto = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    largura = raio * 4 * len(labirinto)
    altura = raio * 4 * len(labirinto)
    x = raio * 6
    y = raio * 6
    velocidade = 10
    pyxel.init(largura, altura)
    pyxel.run(ex6_Update, ex6_Draw)
def ex6_Update():
    global x, y, labirinto
    novo_x = x
    novo_y = y
    if pyxel.btn(pyxel.KEY_LEFT):
        novo_x -= velocidade
    if pyxel.btn(pyxel.KEY_RIGHT):
        novo_x += velocidade
    if pyxel.btn(pyxel.KEY_UP):
        novo_y -= velocidade
    if pyxel.btn(pyxel.KEY_DOWN):
        novo_y += velocidade
    if (
        ex6_verifica_Colisao_Com_Parede(novo_x, novo_y)
    ):
        x = novo_x
        y = novo_y
def ex6_Draw():
    global raio, x, y, labirinto, largura, altura
    col = int(x//(largura/len(labirinto)))
    lin = int(y//(altura/len(labirinto)))
    pyxel.cls(15)
    if (labirinto[lin][col] == 2):
        ex6_Tela_Vencer()
        pyxel.quit()
    else:
        pyxel.circ(x, y, raio, 8) 
        desenha_labirinto()
def desenha_labirinto():
    global labirinto, raio, largura, altura
    tamanho = raio * 4
    for i, linha in enumerate(labirinto):
        print(i, linha)
        for j, celula in enumerate(linha):
            if celula == 2:
                pyxel.rect(j * tamanho, i * tamanho, tamanho, tamanho, 14)
            if celula == 1:
                pyxel.rect(j * tamanho, i * tamanho, tamanho, tamanho, 1)
def ex6_verifica_Colisao_Com_Parede(x, y):
    global raio, labirinto, largura, altura
    col = int(x//(largura/len(labirinto)))
    lin = int(y//(altura/len(labirinto)))
    if labirinto[lin][col] == 1:
        return False    
    return True
def ex6_Tela_Vencer():
    messagebox.showinfo('', "Parabens! Você venceu!")   
ex6()
