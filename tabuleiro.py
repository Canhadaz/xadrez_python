from peças_linha import movimento_torre, movimento_bispo, movimento_dama
from capturas import movimento_rei, movimento_cavalo
from peão import movimento_peão, controlar_turno

def mover_peca(peça: list, inicio: list, chegada: list, tabuleiro: list, lado: bool) -> bool:
    movimento = []
    movimento.append(inicio)
    movimento.append(chegada)
    match(peça):
        #peão --> 50%
        case 1:
            movimento_valido = movimento_peão(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido)
        #torre --> 100%
        case 2:
            movimento_valido = movimento_torre(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido) 
        #cavalo --> 100%
        case 3:
            movimento_valido = movimento_cavalo(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido) 
        #bispo --> 100%
        case 4:
            movimento_valido = movimento_bispo(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido)
        #dama --> 100%
        case 5:
            movimento_valido = movimento_dama(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido)
        #rei --> 100%
        case 6:
            movimento_valido = movimento_rei(tabuleiro, movimento, lado) == True
            lado = controlar_turno(lado, movimento_valido)
        
    return lado

# pega as posições existentes da peça selecionada
def posição_valida(tabuleiro: list, movimento: list, peça: list, lado: bool) -> list:
    print(movimento)
    posicao = []

    for n in range(8):
        for i in range(8):
            if lado == True:
                if tabuleiro[n][i] == peça[0]:
                    posicao.append((n , i))
            elif lado == False:
                if tabuleiro[n][i] == peça[1]:
                    posicao.append((n , i))

    return posicao

def criar_tabuleiro() -> list:
    tabuleiro = []
    #variavel da casa do tabuleiro (usei para criar a posição das peças)
    #a cada iteração (64 iterações na criação), o valor dele é aumentado e eventualmente
    #consigo manipular as casas dum jeito mais facil
    casa = 0
    for n in range(8):
        linha = []
        for i in range(8):
            casa += 1
            if n % 2 == 0:
                linha.append('⬜') if casa % 2 == 0 else linha.append('⬛')
            else:
                linha.append('⬜') if casa % 2 != 0 else linha.append('⬛')

        #posição inicial (peão)
            if n == 1:
                linha[i] = '♟ '
            elif n == 6:
                linha[i] = '♙ '

        #posição inicial (torre)
            if casa == 1 or casa == 8:
                linha[i] = '♜ '
            elif casa == 57 or casa == 64:
                linha[i] = '♖ '

        #posição inicial (cavalo)
            if casa == 2 or casa == 7:
                linha[i] = '♞ '
            elif casa == 58 or casa == 63:
                linha[i] = '♘ '

        #posição inicial (bispo)
            if casa == 3 or casa == 6:
                linha[i] = '♝ '
            elif casa == 59 or casa == 62:
                linha[i] = '♗ '

        #posição inicial (dama)
            if casa == 5:
                linha[i] = '♛ '
            elif casa == 61:
                linha[i] = '♕ '

        #posição inicial (rei)
            if casa == 4:
                linha[i] = '♚ '
            if casa == 60:
                linha[i] = '♔ '
        tabuleiro.append(linha)
    
    return tabuleiro

def mostrar_tabuleiro(tabuleiro: list):
    
    #print('TABULEIRO 8X8 XADREZ\n')
    for i in range(8):
        print(f'{8 - i}|',''.join(tabuleiro[i]))
    print('  -----------------\n   A B C D E F G H')

def main():
    #cria a variavel tabuleiro a partir da chamada da função de criação,
    #q é passada de parametro para a função de exibição
    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(tabuleiro)

main()