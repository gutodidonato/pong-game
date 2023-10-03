from turtle import *

VELOCIDADE = 20
POSICAO_X = -350
POSICAO_INICIAL = (POSICAO_X, 0)

class Jogador(Turtle):
    
    
    
    def __init__(self):
        super().__init__()
        self.criar_jogador(POSICAO_INICIAL)
        self.posicaoAtual = 0
        self.posicaoX = POSICAO_X

        
    
    def criar_jogador(self, posicao):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicao)
        
    
    def mover_para_cima(self):
        posicao_y = self.ycor() + 20
        self.penup()
        self.posicaoAtual = posicao_y
        self.goto(self.posicaoX, posicao_y)
        return self.posicaoAtual
        
            
    def mover_para_baixo(self):
        posicao_y = self.ycor() - 20
        self.penup()
        self.posicaoAtual = posicao_y
        self.goto(self.posicaoX, posicao_y)
        return self.posicaoAtual
            
