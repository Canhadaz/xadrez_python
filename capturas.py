#impedir captura de peça da mesma cor
#permitir capturar apenas peças adversárias
#atualizar corretamente o tabuleiro após a captura
PEÇA_BRANCA = ['♟ ', '♜ ', '♞ ', '♝ ', '♛ ', '♚ ']
PEÇA_PRETA = ['♙ ', '♖ ', '♘ ', '♗ ', '♕ ', '♔ ']

def capturar_peça(tabuleiro: list, movimento: list, lado: bool, peça: list, parada: list) -> bool:
    casa = 0

    # pega a peça que vai ser capturada, antes das iterações
    capturada = tabuleiro[parada[0]][parada[1]]

    tabuleiro[parada[0]][parada[1]] = (peça[0] if lado == True else peça[1])
    
    for n in range(8):
        for i in range(8):
            casa += 1
            if (n, i) == movimento[0]:
                if n %2 == 0:
                    tabuleiro[n][i] = '⬜' if  casa %2 == 0 else '⬛'
                else:
                    tabuleiro[n][i] = '⬜' if  casa %2 != 0 else '⬛'

    # caso a peça capturada seja o rei, o jogo é encerrado.
    if capturada in ('♚ ', '♔ '):
        return 'fim'
    
    return True     

def captura_permitida(tabuleiro: list, movimento: list, lado: bool, linha: list, coluna: list) -> bool:

    if tabuleiro[linha][coluna] in ('⬜', '⬛'):
        return True

    if lado == True and tabuleiro[linha][coluna] in PEÇA_BRANCA:
        return False

    if lado == False and tabuleiro[linha][coluna] in PEÇA_PRETA:
        return False

    return (linha, coluna)

def mesma_cor(tabuleiro: list, movimento: list, lado: list) -> bool:

    #ultima posição da peça
    chegada = tabuleiro[movimento[1][0]][movimento[1][1]]
    #caso a localização final da peça seja numa peça aliada, ele interrompe a função  
    if lado == True and chegada in PEÇA_BRANCA:
        print('\033[31mNÃO É POSSÍVEL CAPTURAR UMA PEÇA ALIADA!\033[0m')
        return False
    
    elif lado == False and chegada in PEÇA_PRETA:
        print('\033[31mNÃO É POSSÍVEL CAPTURAR UMA PEÇA ALIADA!\033[0m')
        return False

    return True

def movimento_rei(tabuleiro: list, movimento: list, lado: bool) -> bool:
    from tabuleiro import posição_valida

    peça = ['♚ ', '♔ ']

    # calculo proposicional da vertical e horizontal perfeita = 1
    mov_vertical = (
        ((movimento[0][0] - movimento[1][0] == 1) or (movimento[0][0] - movimento[1][0] == -1)) 
        and movimento[0][1] == movimento[1][1]
    )
    mov_horizontal = (
        ((movimento[0][1] - movimento[1][1] == 1) or (movimento[0][1] - movimento[1][1] == -1)) 
        and movimento[0][0] == movimento[1][0]
    )  
    # calculo proposicional (BOOLEANO) da diagonal PERFEITA = 1
    diferença_linha = (movimento[0][0] - movimento[1][0] == 1) or (movimento[0][0] - movimento[1][0] == -1)
    diferença_col = (movimento[0][1] - movimento[1][1] == 1) or (movimento[0][1] - movimento[1][1] == -1)
    mov_diagonal = (diferença_linha == diferença_col) and diferença_linha != 0

    linha = movimento[1][0]
    coluna = movimento[1][1]

    # pega as posições existentes da peça selecionada
    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    # verifica se a posição inicial da peça condiz com a escolhida
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False
    
    if not (mov_vertical or mov_horizontal or mov_diagonal):
        print('\033[31mO MOVIMENTO DEVE SER DE APENAS "1" CASA!\033[0m')
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
        print('\n\033[31mUM REI NÃO PODE DAR XEQUE-MATE EM OUTRO REI!\033[0m')
    return True

def movimento_cavalo(tabuleiro: list, movimento: list, lado: bool) -> bool:
    from tabuleiro import posição_valida

    peça = ['♞ ', '♘ ']

    diferença_linha = movimento[0][0] - movimento[1][0]
    diferença_col = movimento[0][1] - movimento[1][1]

    mov_ver_cavalo = (abs(diferença_linha) == 2) and (abs(diferença_col) == 1)
    mov_hor_cavalo = (abs(diferença_linha) == 1) and (abs(diferença_col) == 2)
    
    linha = movimento[1][0]
    coluna = movimento[1][1]

    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False

    if not (mov_ver_cavalo or mov_hor_cavalo):
        print('\033[31mO MOVIMENTO DEVE SER NO FORMATO DE "L"!\033[0m')
        return False

    if not mesma_cor(tabuleiro, movimento, lado):
        return False

    output = captura_permitida(tabuleiro, movimento, lado, linha, coluna)

    if output == False:
        return False
    if output is not True:
        print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')
    
    end_game = capturar_peça(tabuleiro, movimento, lado, peça, movimento[1])
    if end_game == 'fim':
        print('\n\033[32mLADO BRANCO VENCEU!\033[0m') if lado == True else print('\n\033[32mLADO PRETO VENCEU!\033[0m')
        exit()

    return True
