from turtle import *

VELOCIDADE = 20
TAMANHO = 300
POSICAO_Y = -280
CORPO_INICIAL = [(POSICAO_Y,20),(POSICAO_Y,0),(POSICAO_Y,-20)]
class Jogador(Turtle):
    
    
    
    def __init__(self):
        super().__init__()
        self.corpo = []
        
    
    def criar_jogador(self):
        for posicao in CORPO_INICIAL:
            segmento = Jogador()
            segmento.shape("square")
            segmento.color("white")
            segmento.penup()
            segmento.goto(posicao)
            self.corpo.append(segmento)
