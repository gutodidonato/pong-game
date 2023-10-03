from turtle import *

VELOCIDADE = 20
POSICAO_X = -350
CORPO_INICIAL = [(POSICAO_X,40),(POSICAO_X,20),(POSICAO_X,0),(POSICAO_X,-20),(POSICAO_X,-40)]

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
    
    def mover_para_cima(self):
        for parte in self.corpo:
            posicao_y = parte.ycor()
            posicao_x = parte.xcor()
            parte.goto(posicao_x, posicao_y + 20)
            
    def mover_para_baixo(self):
        for parte in self.corpo:
            posicao_y = parte.ycor()
            posicao_x = parte.xcor()
            parte.goto(posicao_x, posicao_y - 20)
            
