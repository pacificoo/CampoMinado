import time

class Log:

    def escrever_jogo(nome_arquivo, texto = ''):
        '''função que escreve dentro de um arquivo com os dados do jogo
        str, str -> none'''
        caminho_arquivo = 'LOG\\' + nome_arquivo + '.txt'
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(texto)
        arquivo.close()


    def escrever_jogada(nome_arquivo,jogada):
        '''função que escreve uma jogada em uma nova linha
        dentro de um arquivo com os dados do jogo
        str, tuple -> none'''
        caminho_arquivo = 'LOG\\' + nome_arquivo + '.txt'
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(str(jogada[0]) + ' ' + str(jogada[1]) + '\n')
        arquivo.close()


    def escrever_erros(nome_arquivo, erro):
        '''função que escreve os erros ocorridos durante o funcionamento
        do jogo dentro de um arquivo com os dados do jogo
        str -> none'''
        caminho_arquivo = 'LOG\\erros\\' + nome_arquivo + '_ERRORS.txt'
        erro += '\n'
        erro = time.ctime() + ' ' + erro
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(erro)
        arquivo.close()

    def interpretar_jogo_salvo(nome_arquivo):
        '''Retorna as informações de um jogo: campo,
        jogadas já realizadas e tamanho do lado do campo'''

        arquivo = open('LOG\\' + nome_arquivo + '.txt')
        linhas = arquivo.readlines()
        arquivo.close()
        
        if len(linhas) == 0:
            return False, False, []
        
        campo = linhas[0].split()
        
        jogadas = []

        for jogada in linhas[1:len(linhas)]:
            jogadas.append(tuple(jogada.split()))

        lado_campo = len(campo)**0.5

        for elem in campo:
            if type(elem) == int:
                elem = int(elem)
        
        return lado_campo, campo, jogadas


    def contagem_casas_abertas():
        '''Atualiza a contagem de casas abertas no LOG
        None -> int'''
        
        arquivo = open('data\casas abertas.txt')
        try:
            casas = int(arquivo.read()) +1
        except:
            print('O arquivo da quantidade de casas abertas foi corrompido.')
            Log.escrever_erros('Log', 'Erro: O arquivo da quantidade de casas abertas foi corrompido.')
            return 0
            
        arquivo.close()
        
        arquivo2.open('data\casas abertas.txt','w')
        arquivo2.write(str(casas))
        arquivo2.close()

        return casas
        
