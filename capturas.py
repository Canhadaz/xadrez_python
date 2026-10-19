#impedir captura de peça da mesma cor
#permitir capturar apenas peças adversárias
#atualizar corretamente o tabuleiro após a captura
def capturar_peça(tabuleiro, movimento, lado, peça, parada):
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

    # caso a peça que foi capturada seja o rei ele retorna end_game
    # que é usado para finalizar o jogo, considerando que ja foi chamada a
    # função mesma_cor(), eu não preciso colocar uma condição para cada cor
    # usei o valor '1' e não True or False, pois isso facilita
    # quando vou fazer as condições dos valores retornados, visto que
    # essa função ja tem outros retornos em valores booleanos
    if capturada in ('♚ ', '♔ '):
        return 'fim'
    
    return True     

def captura_permitida(tabuleiro, movimento, lado, linha, coluna):
    # diferença_linha = movimento[0][0] - movimento[1][0]
    # diferença_col = movimento[0][1] - movimento[1][1]
    # mov_vertical = (diferença_linha != 0) and (diferença_col == 0)
    # mov_horizontal = (diferença_col != 0) and (diferença_linha == 0)    
    # mov_diagonal = (abs(diferença_linha) == abs(diferença_col)) and diferença_linha != 0
    # passo_linha = 1 if movimento[1][0] > movimento[0][0] else -1
    # passo_col = 1 if movimento[1][1] > movimento[0][1] else -1
    
    peça_branca = ['♟ ', '♜ ', '♞ ', '♝ ', '♛ ', '♚ ']
    peça_preta = ['♙ ', '♖ ', '♘ ', '♗ ', '♕ ', '♔ ']

    if tabuleiro[linha][coluna] in ('⬜', '⬛'):
        return True

    if lado == True and tabuleiro[linha][coluna] in peça_branca:
        return False

    if lado == False and tabuleiro[linha][coluna] in peça_preta:
        return False

    return (linha, coluna)

    # #ultima posição da peça
    # chegada = tabuleiro[movimento[1][0]][movimento[1][1]]
    # #caso a localização final da peça seja numa peça aliada, ele interrompe a função  
    # if lado == True and chegada not in peça_branca:
    #     print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')
    #     return True
    # elif lado == False and chegada not in peça_preta:
    #     print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')
    #     return True

def mesma_cor(tabuleiro, movimento, lado):
    peça_branca = ['♟ ', '♜ ', '♞ ', '♝ ', '♛ ', '♚ ']
    peça_preta = ['♙ ', '♖ ', '♘ ', '♗ ', '♕ ', '♔ ']

    #ultima posição da peça
    chegada = tabuleiro[movimento[1][0]][movimento[1][1]]
    #caso a localização final da peça seja numa peça aliada, ele interrompe a função  
    if lado == True and chegada in peça_branca:
        print('\033[31mNÃO É POSSÍVEL CAPTURAR UMA PEÇA ALIADA!\033[0m')
        return False
    
    elif lado == False and chegada in peça_preta:
        print('\033[31mNÃO É POSSÍVEL CAPTURAR UMA PEÇA ALIADA!\033[0m')
        return False

    return True

def movimento_rei(tabuleiro, movimento, lado):
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

def movimento_cavalo(tabuleiro, movimento, lado):
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
