from analise import Analise
from log import Log
from estrutura import Campo

class Interacao:
        
    def regras():
        ''' funcao que printa as regras do jogo para usario caso seja pedido
        none->none'''
        print('O objetivo do jogo é descobrir as casas vazias. A cada casa vazia descoberta, o número de bombas ao seu redor é revelado')
        print('O jogador perde se a casa escolhida conter uma bomba')
    

    def Tela_pause():
        '''função em que o usuario pode escolher entre as seguintes opções: Voltar
        para o jogo(1), salvar o jogo em outro arquivo(2), voltar para o menu principal(3) e
        sair do jogo(4).
        none->none'''
        print('\n--------Tela de Pause----------\n')
        print('Para voltar para o jogo aperte 1\nPara recarregar um jogo já salvo aperte 2\nPara criar um novo jogo aperte 3\nPara voltar ao menu inicial aperte 4')

        while True:
            num = input('Digite o número escolhido ')
            if not( len(num)!=1 or num[0] not in '1234'):
                break
            print('O numero não é válido ou o valor digitado não é um número')
        if int(num) == 2:
            Interacao.carregar_jogo()
        if int(num) == 3:
            Interacao.novo_jogo()
        if int(num)==4:
            Interacao.menu_Principal()
  
    def possibilidades_pos():
        ''' funcao que gera todas as possíveis de jogadas
        none ->list'''
        combinacao= []
        for i in range(Campo.tamanho()): #confirmar essa 'chamada'
                for j in range(Campo.tamanho()):
                    combinacao.append([i,j])            
        return combinacao

    def posicao():
        '''função que pede a ao usuário posicao
        none->int,int'''
        pos = input('Digite a posição escolhida separada por vírgulas')
        if pos in 'abcdefghijklmnopq':
            raise NumError
        
        posicao = pos.split(',')
        pos1 = posicao[0]
        pos2 = posicao[1]
        
        if [pos1,pos2] not in possibilicades_pos():
            raise PosError
        return (pos1, pos2)

    def lista_de_jogos():
        '''Retorna a lista de todos os jogos salvos'''
        jogos_arquivo = open("LOG\Lista de jogos.txt")
        jogos = jogos_arquivo.readlines()
        jogos_arquivo.close()
        return jogos
   

    def carregar_jogo():
        '''funçao que seleciona um jogo salvo anteriormente
        str->none'''
        jogos = Interacao.lista_de_jogos()
        
        if len(jogos) > 0:
            
            for i in range(len(jogos)):
                print(i,jogos[i])
            
            jogo = input('\nDigite o número do jogo que deseja carregar dentre a lista acima: ')
            Interacao.rodar_jogo(jogos[jogo])

        else:
            print('Não há jogos salvos')
    
    def novo_jogo():
        '''funcao que inicia um novo jogo
        none->none'''
        jogos = Interacao.lista_de_jogos()
        while True:
            arquivo = input('Digite o nome do novo jogo: ')
            if arquivo in jogos:
                print('Este nome já foi usado pra outro jogo. Digite outro')
            else:
                jogos_arquivo = open("LOG\Lista de jogos.txt", 'a')
                jogos_arquivo.write(arquivo + '\n')
                jogos_arquivo.close()

                Log.escrever_jogo(arquivo)
                
                break
        
        Interacao.rodar_jogo(arquivo)
        
        
    
