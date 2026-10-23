from peças_linha import movimento_torre,movimento_bispo,movimento_dama
from capturas import movimento_cavalo, movimento_rei
from peão import movimento_peão

from tabuleiro import criar_tabuleiro

# testa a principais funcionalidades do código
# o assert caso errado exibe erro no teste exato que ele parou
# todas as peças foram testadas

# movimento valido da torre
def teste_torre_valido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[2][0] = '♜ '

    movimento = [(2, 0), (4, 0)]

    assert movimento_torre(tabuleiro, movimento, True) is True
    assert tabuleiro[4][0] == '♜ '

    print("Teste 1: torre com movimento válido - OK")

# movimento diagonal da torre
def teste_torre_diagonal():
    tabuleiro = criar_tabuleiro()
    tabuleiro[4][0] = '♜ '

    movimento = [(4, 0), (2, 2)]

    assert movimento_torre(tabuleiro, movimento, True) is False
    assert tabuleiro[4][0] == '♜ '

    print("Teste 2: torre com movimento diagonal - OK")

# movimento da função caminho_livre()
def teste_torre_bloqueado():
    tabuleiro = criar_tabuleiro()

    movimento = [(0, 0), (2, 0)]

    assert movimento_torre(tabuleiro, movimento, True) is False
    assert tabuleiro[0][0] == '♜ '

    print("Teste 3: torre com caminho bloqueado - OK")

# movimento da diagonal do bispo
def teste_bispo_valido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[5][1] = '♝ '

    movimento = [(5, 1), (2, 4)]

    assert movimento_bispo(tabuleiro, movimento, True) is True
    assert tabuleiro[2][4] == '♝ '

    print("Teste 4: bispo com movimento válido - OK")

# movimento do movimento da dama
def teste_dama_valido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[6][0] = '♛ '

    movimento = [(6, 0), (3, 3)]

    assert movimento_dama(tabuleiro, movimento, True) is True
    assert tabuleiro[3][3] == '♛ '

    print("Teste 5: dama com movimento válido - OK")

# movimento da dama com diagonal imperfeita
def teste_dama_invalido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[6][0] = '♛ '

    movimento = [(6, 0), (3, 4)]

    assert movimento_dama(tabuleiro, movimento, True) is False
    assert tabuleiro[6][0] == '♛ '

    print("Teste 6: dama com movimento inválido - OK")

# movimento do cavalo
def teste_cavalo_valido():
    tabuleiro = criar_tabuleiro()

    movimento = [(0,1),(2,2)]

    assert movimento_cavalo(tabuleiro, movimento, True) is True
    assert tabuleiro[2][2] == '♞ '

    print('Teste 7: cavalo com movimento válido - OK')

# movimento do calo da vertical perfeita
def teste_cavalo_invalido():
    tabuleiro = criar_tabuleiro()

    movimento = [(0, 1), (2, 1)]

    assert movimento_cavalo(tabuleiro, movimento, True) is False
    assert tabuleiro[0][1] == '♞ '

    print('Teste 8: cavalo com movimento inválido - OK')

# movimento rei valido
def teste_rei_valido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[2][3] = '♚ '

    movimento = [(2,3),(2,4)]

    assert movimento_rei(tabuleiro, movimento, True) is True
    assert tabuleiro[2][4] == '♚ '

    print('Teste 9: rei com movimento valido - OK')

# movimento rei com peça no meio
def teste_rei_bloqueado():
    tabuleiro = criar_tabuleiro()

    movimento = [(0,3),(1,3)]

    assert movimento_rei(tabuleiro, movimento, True) is False
    assert tabuleiro[0][3] == '♚ '

    print('Teste 10: rei com movimento valido - OK')

# movimento do peão de duas casas
def teste_peão_valido():
    tabuleiro = criar_tabuleiro()

    movimento = [(1,0),(3,0)]

    assert movimento_peão(tabuleiro, movimento, True) is True
    assert tabuleiro[3][0] == '♟ '

    print('Teste 11: peão com movimento valido - OK')

# movimento do peão retrogrado
def teste_peão_invalido():
    tabuleiro = criar_tabuleiro()
    tabuleiro[3][0] = '♟ '

    movimento = [(3,0),(2,0)]

    assert movimento_peão(tabuleiro, movimento, True) is False
    assert tabuleiro[3][0] == '♟ '

    print('Teste 12: peão com movimento invalido = OK')
# só exibe quando rodada localmente
if __name__ == "__main__":
    teste_torre_valido()
    teste_torre_diagonal()
    teste_torre_bloqueado()
    teste_bispo_valido()
    teste_dama_valido()
    teste_dama_invalido()
    teste_cavalo_valido()
    teste_cavalo_invalido()
    teste_rei_valido()
    teste_rei_bloqueado()
    teste_peão_valido()
    teste_peão_invalido()

    print("\nPASSOU EM TODOS OS TESTES!")
