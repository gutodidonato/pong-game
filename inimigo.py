from jogador import *
import random as r

VELOCIDADE = 20
POSICAO_X = 350
COMPUTADOR_POSICAO_INICIAL = (POSICAO_X, 0)
DIFICULDADE = 1


class Computador(Jogador):
    
    def __init__(self):
        super().__init__()
        self.dificuldade = (r.randint(1,20)+ DIFICULDADE)
        self.posicaoAtual = 0
        self.posicaoX = POSICAO_X
        self.criar_jogador(COMPUTADOR_POSICAO_INICIAL)
        

        