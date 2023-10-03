from jogador import *

VELOCIDADE = 20
TAMANHO = 300
POSICAO_X = 350
CORPO_INICIAL = [(POSICAO_X,40),(POSICAO_X,20),(POSICAO_X,0),(POSICAO_X,-20),(POSICAO_X,-40)]


class Computador(Jogador):
    
    def __init__(self):
        super().__init__()
        self.dificuldade = 1
        

        