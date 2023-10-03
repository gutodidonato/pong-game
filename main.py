from turtle import *
from jogador import *
from bola import *

def quicar_parede():
    tela.tracer(0)
    estado_novo = 360 - bola.estado_de_lance
    bola.corecao_lance(estado_novo)
    bola.mover()
    tela.update()
    tela.tracer(1)
    
        
def quicar_jogador(jogador):
    (posx, posy) = bola.pos()
    for parte in jogador.corpo:
        print(parte.pos())
        if parte.distance(posx, posy) < 20:
            quicar_parede()
    
    
    
    
tela = Screen()
tela.screensize(bg="black")
tela.setup(width=800, height=600)
tela.title("Pingue-Pongue")

jogador = Jogador()
jogador.criar_jogador()

bola = Bola()

while True:
    bola.mover()
    if bola.ycor() > 280 or bola.ycor() < -280:
        quicar_parede()
    quicar_jogador(jogador)


    







tela.exitonclick()