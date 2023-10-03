from turtle import *
from jogador import *
from bola import *
from inimigo import *
import random as r

cor = ["red", "green", "pink", "purple"]

def quicar_parede():
    tela.tracer(0)
    bola.quicar()
    bola.mover()
    tela.update()
    tela.tracer(1)
    
        
def quicar_jogador(player):
    (posx, posy) = bola.pos()
    if player.distance(posx, posy) < 40:
        tela.tracer(0)
        bola.quicar_jogador()
        bola.color(cor[r.randint(0,3)])
        bola.mover()
        tela.update()
        tela.tracer(1)
            
# def setar_dificuldade(resposta):
#     jogador2.dificuldade = resposta
def jogada_pc():
    if bola.ycor() >= jogador2.ycor() + jogador2.dificuldade:
        jogador2.mover_para_cima()
    elif bola.ycor() <= jogador2.ycor() + jogador2.dificuldade:
        jogador2.mover_para_baixo()
    

    
    
tela = Screen()
tela.screensize(bg="black")
tela.setup(width=800, height=600)
tela.title("Pingue-Pongue")
tela.listen()

tela.tracer(0)
jogador = Jogador()
jogador2 = Computador()
tela.update()
tela.tracer(1)



bola = Bola()

tela.onkeypress(fun=jogador.mover_para_cima, key="w")
tela.onkeypress(fun=jogador.mover_para_baixo, key="s")



while True:
    tela.update()
    bola.mover()
    if bola.ycor() > 280 or bola.ycor() < -280:
        quicar_parede()
    if bola.xcor() > 420 or bola.xcor() < -420:
        bola = Bola()
    jogada_pc()
    quicar_jogador(jogador)
    quicar_jogador(jogador2)


    







tela.exitonclick()