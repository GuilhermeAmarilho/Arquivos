# Projeto Algoritimos

## Cada metodo deve:
- abrir
- ler
- escrever
- fechar
    - os arquivos necessario
- Todos os metodos devem tratar o erro para o caso do arquivo de entrada nao existir ou ser invalido.
- Caso seja preciso, voce pode declarar outras classes, atributos, metodos e funcoes.

### PGM
- as trees primeiras linhas do arquivo sao:
	- A primeira linha contem uma palavra chave “P2”
	- A segunda linha contem dois numeros (altura e largura)
	- A terceira linha contem um numero que e o maior numero da imagem (maxval)
	- Os outros valores representam os pixeis

### PPM
- as trees primeiras linhas do arquivo sao:
	- A primeira linha contem uma palavra chave “P2”
	- A segunda linha contem dois numeros (altura e largura)
	- A terceira linha contem um numero que e o maior numero da imagem (maxval)
	- Os outros valores são agrupados em matrizes de 3 itens (R, G, B)

### Metodo brilho
- cria uma nova imagem .pgm alterando o brilho da imagem de entrada. 
    - O metodo deve retornar:
        - True se a operacao foi realizada com sucesso.
        - False caso contrario. 
    - Preste atencao no valor max

### Metodo espelha
- cria uma nova imagem .pgm com a imagem espelhada.
    - O metodo deve retornar:
        - True se a operacao foi realizada com sucesso.
        - False caso contrario

### Metodo rotaciona90
- cria uma nova imagem .ppm com a imagem rotacionada em 90 graus.
    - O metodo deve retornar:
        - True se a operacao foi realizada com sucesso.
        - False caso contrario