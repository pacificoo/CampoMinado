from estrutura import Campo
from interacao import Interacao
from log import Log
from analise import Analise

def main():
    ''' Roda o jogo Campo Minado '''
    
    while True:
        try:
            Interacao.menu_Principal()

        except:
            pass
