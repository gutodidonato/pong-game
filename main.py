from turtle import *
from jogador import *
from bola import *

tela = Screen()
tela.screensize(bg="black")
tela.setup(width=800, height=600)
tela.title("Pingue-Pongue")

jogador = Jogador()


jogador.criar_jogador()


def quicar_parede():
    if bola.ycor() > 280 or bola.ycor() < -280:
        tela.tracer(0)
        estado_novo = 360 - bola.estado_de_lance
        bola.corecao_lance(estado_novo)
        bola.mover()
        tela.update()
        tela.tracer(1)
    

bola = Bola()
while True:
    bola.mover()
    print(bola.ycor())
    quicar_parede()
    










tela.exitonclick()