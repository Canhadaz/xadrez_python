from capturas import mesma_cor, captura_permitida, capturar_peça

# funções meio inuteis, mas adicionei por conta do enunciado
def trocar_turno(lado):
    return not lado

def controlar_turno(lado, movimento_valido):
    
    if movimento_valido:
        return trocar_turno(lado)
    
    return lado

def movimento_peão(tabuleiro, movimento, lado):
    from tabuleiro import posição_valida

    peça = ['♟ ', '♙ ']
    
    diferença_linha = movimento[0][0] - movimento[1][0]
    diferença_col = movimento[0][1] - movimento[1][1]

    direção = -1 if lado == True else 1
    # checa se a diferença das coluna é 0
    # checa se a diferença de colunas esta em direção ou direção * 2
    # caso esteja em direção vezes 2, ele vai para a condição das linhas [33 - 45]
    mov_vertical = (diferença_col == 0) and (diferença_linha in (direção, 2 * direção))

    #caso o lado seja branco, a linha do peão é a 7º, caso seja preto, é a 2º
    #como o peão não pode ir para trás, ele sempre será true para o peão que ainda
    #não foi movimentado.
    linha_peão = 1 if lado == True else 6
    primeira = movimento[0][0] == linha_peão

    if mov_vertical and abs(diferença_linha) == 2:
        # checa se é a primeira jogada do peão
        if not primeira:
            print('\033[31mO PEÃO NÃO PODE MAIS AVANÇAR DUAS CASAS!\033[0m')
            return False

        linha_intermediaria = (movimento[0][0] - direção)

        if tabuleiro[linha_intermediaria][movimento[0][1]] not in ('⬜', '⬛'):
            print('\033[31mO PEÃO NÃO PODE AVANÇAR!\033[0m')
            return False
    
    linha = movimento[1][0]
    coluna = movimento[1][1]

    # isso garante q ele não se mova para trás, e confirma qnd o movimento é diagonal = 1
    if lado == True:
        mov_diagonal = abs(diferença_linha) == 1 and abs(diferença_col) == 1 and diferença_linha < 0
    elif lado == False:
        mov_diagonal = abs(diferença_linha) == 1 and abs(diferença_col) == 1 and diferença_linha > 0

    # pega as posições existentes da peça selecionada
    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    # verifica se a posição inicial da peça condiz com a escolhida
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False
    
    if not (mov_vertical or mov_diagonal):
        print('\033[31mO MOVIMENTO DEVE SER DE APENAS "1" CASA E NUNCA RETRÓGRADO!\033[0m')
        return False

    # para = coluna inicial, coluna final (não preciso da linha, pois é apenas 1 casa e o peão com certeza
    # muda a coluna caso seja diagonal)
    parada = tabuleiro[movimento[1][0]][movimento[1][1]]

    if mov_vertical:
        if parada not in ('⬜', '⬛'):
            print('\033[31mO PEÃO NÃO PODE AVANÇAR!\033[0m')
            return False

    if mov_diagonal:
        if parada in ('⬜', '⬛'):
            print('\033[31mAPENAS NA CAPTURA O PEÃO SE MOVE NA DIAGONAL!\033[0m')
            return False
    
    if not mesma_cor(tabuleiro, movimento, lado):
        return False

    output = captura_permitida(tabuleiro, movimento, lado, linha, coluna)

    if output == False:
        return False
    if output == True:
        pass
    else:
        print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')

    end_game = capturar_peça(tabuleiro, movimento, lado, peça, movimento[1])
    if end_game == 'fim':
        print('\n\033[32mLADO BRANCO VENCEU!\033[0m') if lado == True else print('\n\033[32mLADO PRETO VENCEU!\033[0m')
        exit()
    return True