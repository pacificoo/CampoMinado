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
        arquivo.write(jogada[0] + ' ' + jogada[1] + '\n')
        arquivo.close()


    def escrever_erros(nome_arquivo, erro):
        '''função que escreve os erros ocorridos durante o funcionamento
        do jogo dentro de um arquivo com os dados do jogo
        str -> none'''
        caminho_arquivo = 'LOG\\' + nome_arquivo + '_ERRORS.txt'
        erro += '\n'
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(erro)
        arquivo.close()

    def interpretar_jogo_salvo(nome_arquivo):
        '''Retorna as informações de um jogo: campo,
        jogadas já realizadas e tamanho do lado do campo'''

        arquivo = open('LOG\\' + nome_arquivo + '.txt')
        linhas = arquivo.readlines()
        
        if len(linhas) == 0:
            return False, False, []
        
        campo = linhas[0].split()
        del(campo[-1])
        
        jogadas = []

        for jogada in linhas[1:len(linhas)]:
            jogadas.append(tuple(jogada.split()))

        lado_campo = len(campo)^0.5

        for elem in campo:
            if type(elem) == int:
                elem = int(elem)
        
        return lado_campo, campo, jogadas
