from tabuleiro import criar_tabuleiro, mover_peca, mostrar_tabuleiro

def main():
    #lado True = branco, lado False = preto
    lado = True
    colunas = ['A','B','C','D','E','F','G','H']
    tabuleiro = criar_tabuleiro()

    while True:
        # altera a exibição jogador de cada rodada
        print('\nBRANCO:') if lado == True else print('\nPRETO:')
        # valida os dados inseridos pelo usuário
        while True:
            try:
                peça = int(input(
                    '--> [1] Peão,[2] Torre,[3] Cavalo,'
                    '[4] Bispo,[5] Dama,[6] Rei,[7] Sair do jogo.\n--> '))
                # o ValueError normalmente só acontece quando o tipo dos
                # dados do usuario é diferente do tipo pedido, nesse caso,
                # quando o valor é errado (mesmo sendo inteiro), ele exibe erro
                if (0 >= peça) or (peça >= 8):
                    raise ValueError

                break
                    
            except ValueError:
                print('\033[31mDIGITE APENAS NÚMEROS DENTRE [1 - 7]!\033[0m')
        # caso o usuario queira sair do jogo
        if peça == 7:
            while True:
                    
                saida = input('Deseja mesmo sair ? [S/N]\n--> ').upper()

                if len(saida) == 1 and saida in ('S', 'N'):
                    break

                print('\033[031mDIGITE APENAS 1 CARACTERE DENTRE [S/N]\033[0m')
                
            # sai do jogo (sai do codigo)
            #esse break é completamente inutil, ele so ta ai
            #pra enganar o VScode e ele deixar de 'apagar' o resto do codigo
            if saida == 'S':
                exit()
            elif saida == 'N':
                print('\nBRANCO:') if lado == True else print('\nPRETO:')
                continue

        # faz a validação dos dados inseridos pelo usuário (mesma coisa da anterior)
        while True:
            while True:
                try:
                    linha = int(input('Qual a linha da peça: '))
                    
                    if (0 >= linha) or (linha >= 9):
                        raise ValueError
                    
                    break

                except ValueError:
                    print('\033[31mDIGITE APENAS NÚMEROS DENTRE [1 - 8]!\033[0m')

            while True:
                try:
                    col = input('Qual a coluna da peça: ').upper()

                    if (len(col) > 1) or (col not in colunas):
                        raise ValueError
                    
                    break

                except ValueError:
                    print('\033[31mDIGITE APENAS LETRAS DENTRE [A - H]!\033[0m')
            # pega o valor inteiro do caractere inserido (tabela UNICODE)
            linha = 8 - linha
            col = ord(col) - ord('A')
            break

        # seta o valor de inicio
        inicio = (linha, col)

        # faz a validação dos dados inseridos pelo usuário
        while True:
            while True:
                try:
                    linha = int(input('Qual a linha de destino: '))

                    if (0 >= linha) or (linha >= 9):
                        raise ValueError

                    break

                except ValueError:
                    print('\033[31mDIGITE APENAS NÚMEROS DENTRE [1 - 8]!\033[0m')

            while True:
                try:
                    col = input('Qual a coluna de destino: ').upper()

                    if (len(col) > 1) or (col not in colunas):
                        raise ValueError

                    break

                except ValueError:
                    print('\033[31mDIGITE APENAS LETRAS DENTRE [A - H]!\033[0m')

            linha = 8 - linha
            col = ord(col) - ord('A')
            break
        
        chegada = (linha,col)

        lado = mover_peca(peça, inicio, chegada, tabuleiro, lado)
        mostrar_tabuleiro(tabuleiro)
# boas praticas de modularização
# evita que a main rode globalmente
if __name__ == '__main__':
    main()