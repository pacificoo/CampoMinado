class Log:

    def escrever_jogo(nome_arquivo,jogada):
        '''função que escreve dentro de um arquivo com os dados do jogo
        str -> none'''
        caminho_arquivo = 'LOG\\' + nome_arquivo + '.txt'
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(jogada)
        arquivo.close()


    def escrever_erros(nome_arquivo, erro):
        '''função que escreve dentro de um arquivo com os dados do jogo
        str -> none'''
        caminho_arquivo = 'LOG\\' + nome_arquivo + '_ERRORS.txt'
        erro += '\n'
        
        arquivo = open(caminho_arquivo,'a')
        arquivo.write(erro)
        arquivo.close()
        
    
