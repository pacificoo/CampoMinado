import numpy as np
import matplotlib.pyplot as plt
from log import Log

class Analise:

    def grava_tempo(nome_arquivo, tempo):
        '''Grava o tempo de um jogo salvo em um arquivo na pasta data.
        str, float -> None'''
        
        arquvo = open('\\data\\' + nome_arquivo + '_tempo.txt', 'w')
        arquivo.write(str(tempo))
        arquivo.close()


    def pega_tempo(nome_arquivo):
        '''Retorna o tempo já gasto em um jogo
        str -> float'''
        
        arquvo = open('\\data\\' + nome_arquivo + '_tempo.txt')
        tempo = float(arquivo.read())
        arquivo.close()

        return tempo


    def pega_todos_os_tempos():
        '''Retorna os tempos, em ordem crescente, de todos os jogos salvos.
        None -> list'''
        
        jogos = Interacao.lista_de_jogos_ganhos()
        tempos = []
        for jogo in jogos:
            
            tempos += [float(Analise.pega_tempo(str.replace(jogo,'\n','')))]

        tempos.sort()
        
        return tempos


    def pega_todos_os_tempos_sem_ordem():
        '''Retorna os tempos de todos os jogos salvos.
        None -> list'''
        
        jogos = Interacao.lista_de_jogos_ganhos()
        tempos = []
        for jogo in jogos:
            
            tempos += [float(Analise.pega_tempo(str.replace(jogo,'\n','')))]
        
        return tempos
    
