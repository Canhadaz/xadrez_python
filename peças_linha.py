from capturas import captura_permitida, capturar_peça, mesma_cor

def caminho_livre(tabuleiro: list, movimento: list, lado: bool) -> bool:
    diferença_linha = movimento[1][0] - movimento[0][0]
    diferença_col = movimento[1][1] - movimento[0][1]

    mov_vertical = (diferença_linha != 0) and (diferença_col == 0)
    mov_horizontal = (diferença_col != 0) and (diferença_linha == 0)    
    
    mov_diagonal = (abs(diferença_linha) == abs(diferença_col)) and diferença_linha != 0

    passo_linha = 1 if diferença_linha > 0 else -1 if diferença_linha < 0 else 0
    passo_col = 1 if diferença_col > 0 else -1 if diferença_col < 0 else 0  
    
    linha = movimento[0][0] + passo_linha
    coluna = movimento[0][1] + passo_col

    if not (mov_vertical or mov_horizontal or mov_diagonal):
        print('\033[31mDigite um movimento válido!\033[0m')
        return False

    while (linha, coluna) != movimento[1]:
        output = captura_permitida(tabuleiro, movimento, lado, linha, coluna)

        if output is False:
            return False

        if output is not True:
            return output

        linha += passo_linha
        coluna += passo_col

    # aqui ele verifica se a coordenada final for igual a coordenada da peça adversária
    # sem isso ele não exibe o print de 'PEÇA ADVERSÁRIA CAPTURADA!' (nas peças linha)   
    output = captura_permitida(tabuleiro, movimento, lado, movimento[1][0], movimento[1][1])

    if output is False:
        return False

    if output is not True:
        return output

    return True
    
def movimento_torre(tabuleiro: list, movimento: list, lado: bool) -> bool:
    from tabuleiro import posição_valida
    # inicio = movimento[0][0]
    # chegada = movimento[0][1]
    # aqui a diagonal não precisa ser perfeita, ela apenas precisa indicar que não é horizontal e nem vertical
    mov_diagonal = (movimento[0][0] != movimento[1][0] and movimento[0][1] != movimento[1][1]) 
    # para caso as coordenadas sejam iguais em ambos os casos
    mov_nulo = (movimento[0][0] == movimento[1][0] and movimento[0][1] == movimento[1][1])
    
    peça = ['♜ ', '♖ ']

    # pega as posições existentes da peça selecionada
    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    # verifica se a posição inicial da peça condiz com a escolhida
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False

    if (mov_diagonal or mov_nulo):
        print('\033[31mMOVIMENTO NÃO PODE SER DIAGONAL OU NULO!\033[0m')
        return False

    if not mesma_cor(tabuleiro, movimento, lado):
        return False
    
    output = caminho_livre(tabuleiro, movimento, lado)
    # checa se o return é falso
    if output == False:
        print('\033[31mEXISTE UMA PEÇA ALIADA NO CAMINHO!\033[0m')
        return False
    # checa se o return é verdadeiro
    if output == True:
        parada = movimento[1]
    # checa as outras possibilidade (linha, coluna)
    else:
        parada = output
        print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')

    end_game = capturar_peça(tabuleiro, movimento, lado, peça, parada)
    if end_game == 'fim':
        print('\n\033[32mLADO BRANCO VENCEU!\033[0m') if lado == True else print('\n\033[32mLADO PRETO VENCEU!\033[0m')
        exit()
    return True

def movimento_bispo(tabuleiro: list, movimento: list, lado: bool) -> bool:
    from tabuleiro import posição_valida

    peça = ['♝ ', '♗ ']

    # calculo proposicional da diagonal PERFEITA
    diferença_linha = movimento[0][0] - movimento[1][0]
    diferença_col = movimento[0][1] - movimento[1][1]
    mov_diagonal = (diferença_linha == diferença_col or diferença_linha == -diferença_col) and diferença_linha != 0

    # pega as posições existentes da peça selecionada
    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    # verifica se a posição inicial da peça condiz com a escolhida
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False
    
    if not mov_diagonal:
        print('\033[31mMOVIMENTO DEVE SER PERFEITAMENTE DIAGONAL!\033[0m')
        return False
    
    if not mesma_cor(tabuleiro, movimento, lado):
        return False
    
    output = caminho_livre(tabuleiro, movimento, lado)
    # checa se o return é falso
    if output == False:
        print('\033[31mEXISTE UMA PEÇA ALIADA NO CAMINHO!\033[0m')
        return False
    # checa se o return é verdadeiro
    if output == True:
        parada = movimento[1]
    # checa as outras possibilidade (linha, coluna)
    else:
        parada = output
        print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')
    
    end_game = capturar_peça(tabuleiro, movimento, lado, peça, parada)
    if end_game == 'fim':
        print('\n\033[32mLADO BRANCO VENCEU!\033[0m') if lado == True else print('\n\033[32mLADO PRETO VENCEU!\033[0m')
        exit()
    return True

def movimento_dama(tabuleiro: list, movimento: list, lado: bool) -> bool:
    from tabuleiro import posição_valida

    peça = ['♛ ', '♕ ']

    # calculo proposicional da vertical e horizontal perfeita
    mov_vertical = movimento[0][0] != movimento[1][0] and movimento[0][1] == movimento[1][1]
    mov_horizontal = movimento[0][1] != movimento[1][1] and movimento[0][0] == movimento[1][0]    
    # calculo proposicional da diagonal PERFEITA
    diferença_linha = movimento[0][0] - movimento[1][0]
    diferença_col = movimento[0][1] - movimento[1][1]
    mov_diagonal = (diferença_linha == diferença_col or diferença_linha == -diferença_col) and diferença_linha != 0

    # pega as posições existentes da peça selecionada
    posicao = posição_valida(tabuleiro, movimento, peça, lado)

    print(f'POSIÇÃO = {posicao}')
    # verifica se a posição inicial da peça condiz com a escolhida e se tem peça no caminho
    if movimento[0] not in posicao:
        print('\033[31mPOSIÇÃO ERRADA!\033[0m')
        return False

    if not (mov_horizontal or mov_vertical or mov_diagonal):
        print('\033[31mMOVIMENTO DEVE SER PERFEITAMENTE DIAGONAL; HORIZONTAL ou VERTICAL!\033[0m')
        return False
    
    if not mesma_cor(tabuleiro, movimento, lado):
        return False
    
    output = caminho_livre(tabuleiro, movimento, lado)
    # checa se o return é falso
    if output == False:
        print('\033[31mEXISTE UMA PEÇA ALIADA NO CAMINHO!\033[0m')
        return False
    
    # checa se o return é verdadeiro
    if output == True:
        parada = movimento[1]
    # checa as outras possibilidade (linha, coluna)
    else:
        parada = output
        print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m')

    end_game = capturar_peça(tabuleiro, movimento, lado, peça, parada)
    if end_game == 'fim':
        print('\n\033[32mLADO BRANCO VENCEU!\033[0m') if lado == True else print('\n\033[32mLADO PRETO VENCEU!\033[0m')
        exit()
    return True
    