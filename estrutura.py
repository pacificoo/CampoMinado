import numpy as np
import random as rd


class Campo:

    def __init__(self,lado):
        ''' Define os atributos para um objeto de classe Campo '''

        self.lado = lado #Tamanho do lado do campo minado
        self.tamanho = lado**2 #Quantidade de casas do campo minado
        self.campo = [0]*self.tamanho #campo minado
        self.mascara = [(lado*['#'])]*lado #mascara
        self.casas = [] #casas abertas

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

    def transforma_em_mascara(self):
        ''' Transforma o atributo mascara no tipo lista organizado em matriz quadrada '''

        self.mascara = np.array(list(self.mascara))
        self.mascara.shape = (self.lado,self.lado)
        self.mascara = list(self.mascara)
        for elem in range(len(self.mascara)):
            self.mascara[elem] = list(self.mascara[elem])

            
    def imprimir_campo(self):
        '''Imprime campo para o usuário'''
        for linha in self.campo:
            print(*linha)


    def imprimir_mascara(self):
        ''' imprime campo que é visível ao usuário durante a partida
        Campo ->none'''
        for linha in self.mascara:
            print(*linha)


    def minar_campo(self):
        ''' Coloca as bombas em lugares aleatórios do campo '''
        self.transforma_em_lista()

        escopo = ['b']*18 + [0]*82
        
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
                    
    
    def contador(self):
        '''funcao que conta quantas bombas estão na mascara
        Campo->int'''
        cont = 0
        for linha in self.mascara:
            for elem in linha:
                if elem == '#':
                    cont+=1

        return cont


    def bombas(self):
        '''funcao que conta quantas bombas estão escondidas
        Campo->int'''
        cont = 0
        for linha in self.campo:
            for elem in linha:
                if elem == 'b':
                    cont+=1
        return cont


    def decifrar(self,pos1,pos2):
        '''funcao que abre a casa escolhida, modificando a mascara
        Campo,int,int->none'''
        num = self.campo[pos1][pos2]
        self.mascara[pos1][pos2] = num
        self.casas.append((pos1,pos2))


    def desmascarar(self,tupla):
        '''funcao que abre as casas e coloca o número de bombas ao seu redor
        Campo->tupla'''
        
        pos1 = tupla[0]
        pos2 = tupla[1]
        if self.campo[pos1][pos2]=='b': 
            return (False,False)
            
        else:
            if self.campo[pos1][pos2]==0:
                self.decifrar(pos1,pos2)
                self.zeros(tupla)
                
                
            else:
                self.decifrar(pos1,pos2)
                

            bools = (True,False)
            num_1 = self.contador()
            num_2 = self.bombas()
            
        if num_1 == num_2 and self.campo[pos1][pos2]!='b':
            bools = True, True 

        
        return bools


    def zeros(self,tupla):
        '''Funcao que revela todas as casas adjacentes a uma casa com zero bombas
        Campo,tupla ->none'''
        i = tupla[0]
        j = tupla[1]
        
        teste = [(i-1, j-1),
                 (i-1, j),
                 (i-1, j+1),
                 (i, j-1),
                 (i, j+1),
                 (i+1, j-1),
                 (i+1, j),
                 (i+1, j+1)]
            
        for casa in teste:
            if  casa[0] <= self.lado-1 and casa[1] <= self.lado-1 and casa[0]>= 0 and casa[1]>=0 and casa not in self.casas: 
                print(casa)
                self.desmascarar(casa)
    

    def fim_de_jogo(self):
        '''Funcao que abre todas as bombas na mascara quando o usuário perde o jogo
        Campo->none'''
        linha=0
        elem=0
        for i in self.campo:
            for j in i :
                if j=='b':
                    self.mascara[linha][elem]='b'
                elem+=1
            elem =0
            linha+=1
