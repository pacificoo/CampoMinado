from estrutura import Campo
from interacao import Interacao
from log import Log
from analise import Analise
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import time


def main():
    ''' Roda o jogo Campo Minado '''
    
    while True:
        try:
            Interacao.menu_principal()
            break

        except:
            print('Erro inesperado')
            

main()
