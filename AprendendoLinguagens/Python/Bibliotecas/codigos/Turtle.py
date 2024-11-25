from turtle import *
value = int(
  input(
    'Informe a opção desejada:\n'+
    'Sua resposta: '
  )
)

clearscreen()
setup(400,400)
speed(5)
i = 0
# penup() - levanta caneta
# pendown() - volta a desenhar


def square():
  while i < 4:
    forward(100)
    left(90)
    i+=1

def exagono():
  penup()
  forward(40)
  pendown()
  i = 0
  while i < 6:
    left(120)
    forward(40)
    i+=1

  

match value:
    case 1:
      square()
    case 2:
      exagono()
    # case _:
