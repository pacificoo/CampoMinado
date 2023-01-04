import numpy as np
import matplotlib.pyplot as plt
from log import Log

class Analise:

    def grava_tempo(nome_arquivo, tempo):
        '''Grava o tempo de um jogo salvo em um arquivo na pasta data.
        str, float -> None'''
        
        arquivo = open('data\\' + nome_arquivo + '_tempo.txt', 'w')
        arquivo.write(str(tempo))
        arquivo.close()


    def pega_tempo(nome_arquivo):
        '''Retorna o tempo já gasto em um jogo
        str -> float'''
        
        arquivo = open('data\\' + nome_arquivo + '_tempo.txt')
        tempo = float(arquivo.read())
        arquivo.close()

        return tempo


    def pega_todos_os_tempos(jogos):
        '''Retorna os tempos, em ordem crescente, de todos os jogos salvos.
        None -> list'''
        
        tempos = []
        for jogo in jogos:
            
            tempos += [float(Analise.pega_tempo(str.replace(jogo,'\n','')))]

        tempos.sort()
        
        return tempos


    def pega_todos_os_tempos_sem_ordem(jogos):
        '''Retorna os tempos de todos os jogos salvos.
        None -> list'''
        
        tempos = []
        for jogo in jogos:
            
            tempos += [float(Analise.pega_tempo(str.replace(jogo,'\n','')))]

        
        return tempos

    def plotar_grafico(tempos):
        '''funcao que plota um infograma que relaciona o numero de vitorias com o tempo
        list->none'''
        fig, ax = plt.subplots()
        ax.set_title('Vitórias por intervalo de tempo')
        plt.xlabel('Tempo(s)')
        cont =1
        for n in tempos:
            cont+=1
        ax.set_yticks(np.arange(0,cont,1))
        plt.ylabel('Número de Jogos')
        plt.hist(tempos,rwidth=1)
        plt.show()

                
    def salvar_grafico(tempos,nome_arquivo):
        '''funcao que salva o grafico na pasta data
        list,str ->none'''
        ig, ax = plt.subplots()
        ax.set_title('Vitórias por intervalo de tempo')
        plt.xlabel('Tempo(s)')
        cont =1
        for n in tempos:
            cont+=1
        ax.set_yticks(np.arange(0,cont,1))
        plt.ylabel('Número de Jogos')
        plt.hist(tempos,rwidth=1)
        plt.savefig('data\\'+nome_arquivo +'.pdf')
