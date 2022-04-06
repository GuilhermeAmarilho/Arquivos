#como printar algo na tela
print("")
#pegando dados

input('informe o nome: ')

type(nome) #str

#transformar em um tipo

int()
str()
bool()
float()

#operadores

2  +  2 = 4
2  -  2 = 0
2  *  4 = 8 
9  %  3 = 0
3  %  9 = 3
3  ** 3 = 27    #(potencia)
20 /  8 = 2.5
20 // 8 = 2     #(apenas divisao exata)
"banana"*3 =    "bananabananabanana"
2 >  5 #false
2 <  5 #true
3 >= 4 #false
3 <= 4 #true
2 == 2 #true
2 != 2 #false
5 != 3 and 4 > 2 #true
5 != 5 or  4 > 2 #true
(not 5!= 5) and 2 > 1 #true

#funcoes

x= input("digite um numero: ")

if x<10:
    print("menor que 10")
elif x<100:
    print("entre 10 e 99")
else:
    print("maior que 100")

x=0
while x<=10:
    print(“x: {}”.format(x))
    x=x+1
print("fim:fora do while")

#var: existirá apenas no bloco do loop
#Var iterável: uma lista ou range por exemplo
#Range() define uma sequencia de números
range(5)      #de 0 a 5 com incremento de 1
Range(2,8)    #de 2 a 8 com incremento de 1
Range(5,15,3) #de 5 a 15 com incremento de 3
for x in range(10):
    print("x: {}".format(x))
print("acabou")

for x in [1,2,3,4,5,6,7]:
    print(x)

def soma(x,y=10):
    return x+y

print(  soma(2) ) #12
print(  soma(3,5)   ) #8

#string
(pega o correspondente a posicao
pega ate o anterior a essa posicao
a cada quantos caracteres ele se repete)
a = "123456789"
a[1] = "2"
a[-1] = "9"
a[1:4] = "234"
a[:4] = "1234" 
a[3:] = "456789"
a = "abcdefghijklmno" 
a[1:10:4]


#lista
i = [1,2,3,4]
i.append(8) # [1,2,3,4,8]
i.insert(2,219) # [1,2,219,3,4,8]
i[1] # 2
i = ["a","ab","casa","maca","refri","agua","mochila"]

i.pop() # ["a","ab","casa","maca","refri","agua"]
i.pop(2) # ["a","ab","maca","refri","agua"]
i.remove("maca") # ["a","ab","refri","agua"]
i.count("casa") # 1
i.sort() # ["a","ab","agua","refri"]
len(i) # 4

#tupla
i = tuple(2,4,6)
print(i) # ()

#dict

d = dict()
d = {'nome' : 'guilherme', 'idade' : 18, 'sexo': 'masculino'}
d['nome'] # guilherme
d['nome'] = 'gui'
d['nome'] # gui

d.pop('sexo') # Masculino (dps disso apaga)
d.popitem('nome') # gui (não apaga)
d.keys() # nome, idade
d.values() # gui, 18
d.items() # (nome, idade) , (gui,18)

#datas
#date-> data com ano mes e dia
#time-> horario com hora minuto e segundo e microsegundo com 6 digitos
#datetime-> ano, mês, dia, hora, minuto, segundo, microsegundos
#timedelta->diferença entre 2 datas
from datetime import datetime #sempre tem q ter
d = datetime(2019,3,12,15,10,10,123456) 
e = datetime.today()



