from turtle import *
import random as r

VELOCIDADE = 5

class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(VELOCIDADE)
        self.estado_de_lance = 0
        self.iniciar()
        
    def iniciar(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,0)
        self.direcao_inicio_bola()
        
    def direcao_inicio_bola(self):
        valores_lance = (r.randint(1,89))*2
        self.estado_de_lance = valores_lance
        self.corecao_lance(valores_lance)
        
    def corecao_lance(self, lance):
        self.seth(lance)
        self.estado_de_lance = lance
        
    def quicar(self):
        estado_novo = 360 - self.estado_de_lance
        self.corecao_lance(estado_novo)
    
    
    
    def mover(self):
        self.penup()
        self.seth(self.estado_de_lance)
        self.forward(20)
        self.pendown()
        
        
        