from jogador import *

VELOCIDADE = 20
POSICAO_X = 350
COMPUTADOR_POSICAO_INICIAL = (POSICAO_X, 0)


class Computador(Jogador):
    
    def __init__(self):
        super().__init__()
        self.dificuldade = 1
        self.posicaoAtual = 0
        self.posicaoX = POSICAO_X
        self.criar_jogador(COMPUTADOR_POSICAO_INICIAL)
        

        