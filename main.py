from turtle import *
from jogador import *
from bola import *
from inimigo import *

def quicar_parede():
    tela.tracer(0)
    bola.quicar()
    bola.mover()
    tela.update()
    tela.tracer(1)
    
        
def quicar_jogador(jogador):
    (posx, posy) = bola.pos()
    for parte in jogador.corpo:
        if parte.distance(posx, posy) < 20:
            quicar_parede()
            
def setar_dificuldade(resposta):
    jogador2.dificuldade = resposta
    
    
    
    

    
    
    
    
tela = Screen()
tela.screensize(bg="black")
tela.setup(width=800, height=600)
tela.title("Pingue-Pongue")
tela.listen()

jogador = Jogador()
jogador2 = Computador()
jogador.criar_jogador()

bola = Bola()


while True:
    tela.update()
    bola.mover()
    tela.onkeypress(fun=jogador.mover_para_cima, key="w")
    tela.onkeypress(fun=jogador.mover_para_baixo, key="s")
    if bola.ycor() > 280 or bola.ycor() < -280:
        quicar_parede()
    quicar_jogador(jogador)
    quicar_jogador(jogador2)


    







tela.exitonclick()