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
        print('Para voltar para o jogo aperte 1\nsalvar o jogo em outro arquivo aperte 2\nvoltar para o menu principal aperte 3\nsair do jogo aperte 4')
        num = input('Digite o número escolhido ')
        while True:
            
            try:
                num = int(input('Digite o número escolhido '))
                if num<0 or num>5:
                    raise ValueError
                break
                    
            except ValueError:
                
                print('O numero não é válido ou o valor digitado não é um número')
              
        if num  == 2:
            Interacao.carregar_jogo() 
        if num == 3:
            Interacao.menu_principal()
        if num==4:
            Interacao.novo_jogo()
        
    def posicao(lado):
        '''função que pede a ao usuário posicao
        none->int,int'''
        while True:
            
            try:
                pos = input('''Digite a posição escolhida separada por x no tipo LINHAxCOLUNA.
                            \nOs valores para linha e coluna devem estar entre 0 e tamanho do campo-1: ''')
                posicao = pos.split('x')
                
                pos1 = int(posicao[0])
                pos2 = int(posicao[1])
                
                if pos1 > lado-1 or pos2 > lado-1 or pos1<0 or pos2<0:
                    raise ValueError
                
                return (pos1, pos2)

            except ValueError:
                print('A posição digitada é inválida.')

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
            
            while True:
                try:
                    jogo = int(input('\nDigite o número do jogo que deseja carregar dentre a lista acima: '))

                    if jogo <0 or jogo>= len(jogos):
                        raise IndexError
                    
                    break
                
                except ValueError:
                    print('Erro: o valor inserido deve ser um inteiro')

                except IndexError:
                    print('Erro: o número digitado não está entre a lista disponibilizada')

            Interacao.rodar_jogo(jogos[jogo].replace('\n',''))

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
        
        
    
    def rodar_jogo(nome_arquivo):
        '''funcao que roda o jogo para o usuário
        interacao->none'''

        lado_campo, campo_salvo, jogadas = Log.interpretar_jogo_salvo(nome_arquivo)

        if not lado_campo:

            while True:

                try:
                    lado_campo = int(input('Digite um tamanho para o campo entre 5 e 20: '))
                    if lado_campo<5 or lado_campo>20:
                        raise TypeError

                    break
                except TypeError:
                    print('Erro: o tamanho do campo deve estar entre 5 e 20')
                except ValueError:
                    print('Erro: o valor digitado deve ser um inteiro entre 5 e 20')

            jogo = Campo(lado_campo)
            jogo.minar_campo()
            jogo.numerar_campo()
            jogo.transforma_em_lista()

            for casa in jogo.campo:
                Log.escrever_jogo(nome_arquivo,str(casa) + ' ')
            
            Log.escrever_jogo(nome_arquivo, '\n')

            jogo.transforma_em_matriz()

        else:
            jogo = Campo(int(lado_campo))
            jogo.campo = campo_salvo

        
        for jogada_salva in jogadas:
            jogo.desmascarar(jogada_salva)

        jogo.imprimir_campo()
        jogo.imprimir_mascara()

        situ = True

        while situ:
            pos = Interacao.posicao(jogo.lado)
            Log.escrever_jogada(nome_arquivo,pos)
            situ, venceu = jogo.desmascarar(pos)
            if not situ:
                jogo.fim_de_jogo()
            jogo.imprimir_campo() ### SOMENTE PARA TESTE ###
            jogo.imprimir_mascara()
            
            if venceu:
                break

        if venceu:
            print('Parabéns!!! Você venceu o jogo.')
        else:
            print('Que pena! Você perdeu o jogo.')

        Interacao.menu_principal()
            

    def menu_principal():
        '''funcao que escolhe entre as seguintes opções: Novo Jogo (1), carregar jogo
        (2), estatísticas (3), regras dos jogo (4), e sair do jogo (5)
        Interacao->none'''

        while True:
            print('\n--------Menu Principal----------\n')
            print('Para criar um Novo Jogo aperte 1\nPara carregar um jogo aperte 2\nPara ver as estatisticas aperte 3\nPara ver as regras do jogo aperte 4\nPara sair do jogo aperte 5')
            while True:
                try:
                    num = int(input('Digite o número escolhido '))

                    if num<1 or num>5:
                        raise ValueError

                    break

                except ValueError:
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









