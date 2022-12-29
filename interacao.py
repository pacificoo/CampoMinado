from analise import Analise
#acho que preciso importar do log tbm 

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
    
        #perguntar para o andre se precisa raise erro

    def posicao():
        '''função que pede a ao usuário posicao
        none->int,int'''
        posicao = input('Digite a posição escolhida separada por vírgulas')
        pos1 = int(posicao[0])
        pos2 = int(posicao[2])

        return pos1, pos2
    
    def carregar_jogo(arquivo):
        '''funçao que seleciona um jogo salvo anteriormente
        str->none'''
        nome = input('Digite o nome do jogo que deseja abrir com a sua respectiva extensao')
    
    def novo_jogo():
        '''funcao que inicia um novo jogo
        none->none'''
        pass
    
    def rodar_jogo():
        '''funcao que roda o jogo para o usuário
        interacao->none'''
        while True:
            pos = Interacao.posicao()
            

    def menu_Principal():
        '''funcao que escolhe entre as seguintes opções: Novo Jogo (1), carregar jogo
        (2), estatísticas (3), regras dos jogo (4), e sair do jogo (5)
        Interacao->none'''

        while True:
            print('\n--------Menu Principal----------\n')
            print('Para criar um Novo Jogo aperte 1\nPara carregar um jogo aperte 2\nPara ver as estatisticas aperte 3\nPara ver as regras do jogo aperte 4\nPara sair do jogo aperte 5')
            while True:
                num = input('Digite o número escolhido ')
                if not( len(num)!=1 or num[0] not in '12345'):
                    break
                print('O numero não é válido ou o valor digitado não é um número')
                
                
            if int(num) == 1:
                Interacao.novo_jogo()
            if int(num) == 2:
                Interacao.carregar_jogo()
            if int(num)==3:
                Interacao.estatisticas()
            if int(num) == 4:
                Interacao.regras()
            if int(num) ==5:
                break

    def estatisticas(dados):
        '''funcao que printa para o usuario as estatisticas dos jogos anteriores'''
        pass
        #importar de outras funcões 

class NumError(Exception):
    pass


    

        
