from analise import Analise
from log import Log
from estrutura import Campo
import time

class Interacao:
        
    def regras():
        ''' funcao que printa as regras do jogo para usario caso seja pedido
        none->none'''
        print('O objetivo do jogo é descobrir as casas vazias. A cada casa vazia descoberta, o número de bombas ao seu redor é revelado')
        print('O jogador perde se a casa escolhida conter uma bomba')
        Interacao.menu_principal()
    

    def Tela_pause(nome_arquivo):
        '''função em que
o usuario pode escolher entre as seguintes opções: Voltar
        para o jogo(1), Para carregar outro jogo salvo(2), voltar para o menu principal(3) e
        sair do jogo(4).

        str->none'''
        print('\n--------Tela de Pause----------\n')
        print('Para voltar para o jogo aperte 1\nPara iniciar um jogo novo aperte 2\nPara carregar outro jogo já salvo aperte 3\nPara voltar para o menu principal aperte 4\nPara sair do jogo aperte 5')

        while True:
            
            try:
                num = int(input('Digite o número escolhido '))
                if num<1 or num>5:
                    raise ValueError
                break
                    
            except ValueError:
                
                print('O numero não é válido ou o valor digitado não é um número')
                Log.escrever_erros(nome_arquivo, 'Erro: Tela pause: O numero não é válido ou o valor digitado não é um número')

        
        return num
        
    def posicao(lado,nome_arquivo):
        '''função que pede a ao usuário posicao
        int,str->tuple'''
        while True:
            
            try:
                pos = input('''Digite a posição escolhida separada por x no tipo LINHAxCOLUNA ou digite "p" para pausar o jogo.
                            \nOs valores para linha e coluna devem estar entre 0 e tamanho do campo-1: ''')
                if pos == 'p':
                    return pos
                
                posicao = pos.split('x')
                if len(posicao) != 2:
                    raise ValueError
                
                pos1 = int(posicao[0])
                pos2 = int(posicao[1])
                
                if pos1 > lado-1 or pos2 > lado-1 or pos1<0 or pos2<0:
                    raise ValueError
                
                return (pos1, pos2)

            except ValueError:
                print('A posição digitada é inválida.')
                Log.escrever_erros(nome_arquivo,'Erro de posicão: A posição digitada é inválida.')



    def lista_de_graficos():
        '''Retorna a lista de todos os graficos salvos
        none -> list'''
        graficos_arquivo = open("LOG\Lista de graficos.txt")
        graficos= graficos_arquivo.readlines()
        graficos_arquivo.close()
        return graficos
        
    def lista_de_jogos():
        '''Retorna a lista de todos os jogos salvos
        none ->list'''
        jogos_arquivo = open("LOG\Lista de jogos.txt")
        jogos = jogos_arquivo.readlines()
        jogos_arquivo.close()
        return jogos


    def lista_de_jogos_ganhos():
        '''Retorna a lista de todos os jogos ganhos
        none ->list'''
        jogos_arquivo = open("LOG\Lista de jogos ganhos.txt")
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
                    jogo = int(input('Digite o número do jogo que deseja carregar dentre a lista acima: '))

                    if jogo <0 or jogo>= len(jogos):
                        raise IndexError

                    jogos_ganhos = Interacao.lista_de_jogos_ganhos()
                    
                    if jogos[jogo] in jogos_ganhos:
                        raise TypeError

                    break
                
                except ValueError:
                    print('Erro: o valor inserido deve ser um inteiro')
                    Log.escrever_erros('carregar_jogo','Erro: o valor inserido deve ser um inteiro')

                except IndexError:
                    print('Erro: o número digitado não está entre a lista disponibilizada')
                    Log.escrever_erros('carregar_jogo','Erro: o número digitado não está entre a lista disponibilizada')

                except TypeError:
                    print('Você já venceu este jogo. Escolha outro.')
                    

            Interacao.rodar_jogo(jogos[jogo].replace('\n',''))

        else:
            print('Não há jogos salvos')
            Interacao.menu_principal()
            return None
    
    def novo_jogo():
        '''funcao que inicia um novo jogo
        none->none'''
        jogos = Interacao.lista_de_jogos()
        while True:
            arquivo = input('Digite o nome do novo jogo: ')
            if arquivo + '\n' in jogos:
                print('Este nome já foi usado pra outro jogo. Digite outro')
            else:
                jogos_arquivo = open("LOG\Lista de jogos.txt", 'a')
                jogos_arquivo.write(arquivo + '\n')
                jogos_arquivo.close()

                Log.escrever_jogo(arquivo)
                
                
                break

        Analise.grava_tempo(arquivo,0)
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
                    Log.escrever_erros(nome_arquivo,'Erro: rodar_jogo: o tamanho do campo deve estar entre 5 e 20')
                except ValueError:
                    print('Erro: o valor digitado deve ser um inteiro entre 5 e 20')
                    Log.escrever_erros(nome_arquivo,'Erro: rodar_jogo: o valor digitado deve ser um inteiro entre 5 e 20')
                    

            jogo = Campo(lado_campo)
            jogo.minar_campo()
            jogo.numerar_campo()
            jogo.transforma_em_lista()

            for casa in jogo.campo:
                Log.escrever_jogo(nome_arquivo,str(casa) + ' ')
            
            Log.escrever_jogo(nome_arquivo, '\n')

            jogo.transforma_em_matriz()

        else:
            try:
                jogo = Campo(int(lado_campo))
                jogo.campo = campo_salvo
                jogo.transforma_em_matriz()
            except:
                print('Erro: o arquivo do jogo salvo foi corrompido')
                Log.escrever_erros(nome_arquivo,'Erro: o arquivo do jogo salvo foi corrompido')
                Interacao.carregar_jogo(nome_arquivo)
                return None

        try:
            
            for jogada_salva in jogadas:
                situ, venceu = jogo.desmascarar(jogada_salva)
        except:
            print('Erro: o arquivo do jogo salvo foi corrompido')
            Log.escrever_erros(nome_arquivo,'Erro: o arquivo do jogo salvo foi corrompido')
            Interacao.carregar_jogo(nome_arquivo)
            return None
            

        jogo.imprimir_campo() ### SOMENTE PARA TESTE ###
        jogo.imprimir_mascara()

        situ = True

        
        while situ:
            verificacao = True
            tempo = Analise.pega_tempo(nome_arquivo)
            tempo2 = round(time.time(),2)
            pos = Interacao.posicao(jogo.lado, nome_arquivo)
            tempo = round(time.time(),2) + tempo - tempo2
            Analise.grava_tempo(nome_arquivo, tempo)


            #tela pause
            if pos == 'p':
                
                pause = Interacao.Tela_pause(nome_arquivo)
                verificacao = False

                if pause == 1:
                    jogo.imprimir_mascara()
                if pause==2:
                    Interacao.novo_jogo()
                    return None
                if pause == 3:
                    Interacao.carregar_jogo()
                    return None
                if pause == 4:
                    Interacao.menu_principal()
                    return None
                if pause==5:
                    return None
            #tela pause

            else:
                Log.escrever_jogada(nome_arquivo,pos)
                situ, venceu = jogo.desmascarar(pos)
                Log.contagem_casas_abertas()
                
                if not situ:
                    jogo.fim_de_jogo()
                jogo.imprimir_mascara()
                
                if venceu:
                    break

        if verificacao:
            if venceu:
                print('Parabéns!!! Você venceu o jogo.')
                jogos_ganhos_arquivo = open("LOG\Lista de jogos ganhos.txt", 'a')
                jogos_ganhos_arquivo.write(nome_arquivo + '\n')
                jogos_ganhos_arquivo.close()
                
            else:
                print('Que pena! Você perdeu o jogo.')
            #replace (???)
            print(str.format('Você completou o jogo em {} segundos.',tempo))

            tempos = Analise.pega_todos_os_tempos(Interacao.lista_de_jogos_ganhos())

            if len(tempos) > 0:
                if tempo == tempos[0] and situ == True:
                    print('Parabéns!!! Você tem um novo recorde de tempo')
                elif tempo < tempos[0] and situ == True:
                    print('Parabéns!!! Você tem um novo recorde de tempo. O recorde anterior era de '+ str(tempos[0]))
    

            Interacao.menu_principal()
            

    def menu_principal():
        '''funcao que escolhe entre as seguintes opções: Novo Jogo (1), carregar jogo
        (2), estatísticas (3), regras dos jogo (4), e sair do jogo (5)
        Interacao->none'''

        
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
                Log.escrever_erros('menu_principal', 'Erro: O numero não é válido ou o valor digitado não é um número')
            
            
        if int(num) == 1:
            Interacao.novo_jogo()
        if int(num) == 2:
            
            Interacao.carregar_jogo()
        if int(num)==3:
            Interacao.estatisticas()
        if int(num) == 4:
            Interacao.regras()


    def estatisticas():
        '''funcao que printa para o usuario as estatisticas dos jogos anteriores'''
        jogos = len(Interacao.lista_de_jogos())
        jogos_ganhos = len(Interacao.lista_de_jogos_ganhos())
        lista_jogos_ganhos = Interacao.lista_de_jogos_ganhos()
        tempos = Analise.pega_todos_os_tempos(Interacao.lista_de_jogos_ganhos())
        tempos_sem_ordem = Analise.pega_todos_os_tempos_sem_ordem(Interacao.lista_de_jogos_ganhos())
        tempo_total = sum(Analise.pega_todos_os_tempos(Interacao.lista_de_jogos()))
        casas = Log.contagem_casas_abertas(False)

        tempo_recorde = 'Não há tempo recorde ainda.'
        if len(tempos) >=1:
            tempo_recorde = tempos[0]

        print('\nJogos jogados: ' + str(jogos)) #jogos jogados
        print('Tempo total jogado: ' + str(tempo_total) + ' seg') #tempo total de jogos
        print('Tempo recorde (em segundos): ' + str(tempo_recorde))  #tempo recorde
        print('Quantidade de jogos ganhos: '+ str(jogos_ganhos)) #jogos ganhos
        print('Quantidade de jogos perdidos ou incompletos: ' + str(jogos - jogos_ganhos)) #jogos perdidos
        print('Quantidade de casas abertas: ' + str(casas)) #total de casas abertas

        teste = input('\nSe você quiser visualizar o histograma de vitórias por intervalo de tempo, aperte 1. \nSe quiser salvar o histograma aperte 2.\nO gráfico será salvo na pasta data\nCaso não queira fazer nada aperte qualquer outro caracter ')

        if teste == '1':
            Analise.plotar_grafico(tempos_sem_ordem)
        if teste == '2':
            graficos = Interacao.lista_de_graficos()
            nome = input('Digite um nome para o seu gráfico' )

            if nome + '\n' in graficos:
                print('Este nome já foi usado pra outro grafico. Digite outro')
            else:
                graficos_arquivo = open("LOG\Lista de graficos.txt", 'a')
                graficos_arquivo.write(nome + '\n')
                
                graficos_arquivo.close()

            
            Analise.salvar_grafico(tempos_sem_ordem,nome)


        Interacao.menu_principal()

