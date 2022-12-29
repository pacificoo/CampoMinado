import numpy as np
import random as rd

class Campo:

    def __init__(self,lado):
        ''' Define os atributos para um objeto de classe Campo '''

        self.lado = lado #Tamanho do lado do campo minado
        self.tamanho = lado**2 #Quantidade de casas do campo minado
        self.campo = [0]*self.tamanho #campo minado

    def transforma_em_array(self):
        ''' Transforma o atributo campo no tipo np.array '''

        self.campo = np.array(self.campo)
        self.campo.shape = (self.lado,self.lado)

    def transforma_em_lista(self):
        ''' Transforma o atributo campo no tipo lista '''

        self.campo = np.array(list(self.campo))
        self.campo.shape = (self.tamanho)
        self.campo = list(self.campo)

    def transforma_em_matriz(self):
        ''' Transforma o atributo campo no tipo lista organizado em matriz quadrada '''

        self.campo = np.array(list(self.campo))
        self.campo.shape = (self.lado,self.lado)
        self.campo = list(self.campo)
        for elem in range(len(self.campo)):
            self.campo[elem] = list(self.campo[elem])
        

    def minar_campo(self):
        ''' Coloca as bombas em lugares aleatórios do campo '''
        self.transforma_em_lista()

        escopo = ['b'] + [0]*int((self.lado/2))
        
        for casa in range(len(self.campo)):
            situação = rd.sample(escopo,1)
            self.campo[casa] = situação

        self.transforma_em_array()

    def numerar_campo(self):
        ''' Numera o campo conforme a quantidade de bombas adjacentes à cada casa '''

        self.transforma_em_matriz()

        for i in range(len(self.campo)):
            for j in range(len(self.campo[i])):
                cont = 0
                if not self.campo[i][j] == 'b':

                    for n in range(8):
                        teste = [(i-1, j-1),
                                 (i-1, j),
                                 (i-1, j+1),
                                 (i, j-1),
                                 (i, j+1),
                                 (i+1, j-1),
                                 (i+1, j),
                                 (i+1, j+1)]

                        x,y = teste[n]

                        if not(x <0 or y<0 or x>= self.lado or y>= self.lado):
                            if self.campo[x][y] == 'b':
                                cont += 1

                    self.campo[i][j] = cont

    def mascara(self):
        ''' Campo que é visível ao usuário durante a partida '''

        pass



