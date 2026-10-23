# xadrez_python
Projeto de lógica de programação do jogo xadrez, desenvolvido inteiramente em Python.

inicie o código por:

    --> main.py

forneça as coordenadas da peça que será movimentada.
- linha um valor numérico dentre [1 - 8]
- coluna um valor caractere dentre ['A','B','C','D','E','F','G','H']

# main.py: 

def main():
    --> arquivo inicial do projeto, ele faz a primeira chamada da função
    'criar_tabuleiro()' do arquivo 'tabuleiro.py', função essa que não recebe
    parametro nenhum, porém retorna toda a matriz do tabuleiro.
    --> em sequência, incia-se o processo de iteração, que faz uma serie de
    requisições dos dados para o usuário, sendo essas:

    --> qual peça será jogada; coordenada inicial da peça e coordenada final
    da peça - essenciais para a execução do resto das funções do código.

    --> aqui é criada a variavel booleana 'lado' (define qual a cor do
    tabuleiro que ira jogar), a mesma é passada de parametro para a função
    'mover_peça()' do arquivo 'tabuleiro.py', logo em sequencia a chamada da
    função 'mostrar_tabuleiro()' também do arquivo 'tabuleiro.py', garantindo
    a exibição do mesmo a cada jogada bem sucedida.

    --> todas as requisições feitas ao usuário são validadas, caso o input
    seja invalido, é feita outra requisição dos mesmo dados, para o usuário.

    --> as coordenadas informadas pelo usuário, seguem o mesmo padrão do
    tabuleiro original de xadrez, onde as linha são representadas
    numericamente e as colunas as partir da sequência de caracteres --> 'A'
    'B','C','D','E','F','G','H'.

    --> para transforma-las em um valor numérico valído, para a manipulação
    da matriz 'tabuleiro', foi necessário o uso de um cálculo lógico simples,
    onde a linha = 8 - linha, isso é necessário pois as linhas de uma matriz,
    começam em zero e num tabuleiro de xadrez o lado branco começa na 8º
    linha, já o lado preto na 1º, portanto caso o usuário queira escolher uma
    peça preta da 1º linha, o calculo seria linha = 8 - 1, totalizando 7,
    valor esse referente a ultima linha da matriz. No caso da coluna, foi
    necessário outro cálculo consideravelmente simples, onde é usada a função
    ord(), que retorna um valor unicode de um caractere, essencial para que
    eu transformasse um caractere em um numero inteiro, é usada como base
    para a subtração o "ord('A')", pois o caractere 'A', faz referência a
    primeira coluna, ou seja caso a coluna inserida pelo usuário seja a
    primeira, o valor de coluna é '0', caso seja a ultima, valor retornado é
    igual a '7'.

```python
    linha = 8 - linha
    col = ord(col) - ord('A')
```
# tabuleiro.py:

def criar_tabuleiro():
    --> sendo essa a primeira função chamada por 'main.py', como o nome ja
    diz, cria o tabuleiro inicial.

    --> é usada para a criação uma sequência simples de iteração, utilizando
    dois 'for' ambos iterando 8 vezes, o primeiro tem como função principal
    resetar o valor da lista 'linha' a cada iteração, pois a cada iteração do
    primeiro 'for', o segundo é executado 8 vezes, garantindo que a variavel
    'casa' percorra todas as 64 casas de um tabuleiro, no segundo 'for' é
    utilizada como base para a criação das casas do tabuleiro, uma variavel
    chamada 'casa', com valor inicial de 0, valor esse que é somado + 1 à
    ele, depois de cada iteração do segundo 'for', logo em sequência, é usado
    um comando de condição 'if' que verifica se a linha do tabuleiro é par ou
    não, isso inverte a posição das casas a cada iteração, quando a variavel
    'casa' é par é atribuido ao tabuleiro o icone '⬜', quando ele é impar
    '⬛', esses símbolos fazem referência a cor de cada casa do tabuleiro,
    caso a linha seja ímpar, é executado um comando de condição 'else', que
    inverte a lógica. Portanto o primeiro 'for' percorre as linhas do
    tabuleiro, e o segundo as colunas, as inverções do if e else, são
    essenciais para garantir que a o tabuleiro possua uma troca das
    colorações das casas adequadamente.

    --> depois de já criado o tabuleiro com as cores de cada casa, é
    necessário adicionar as peças em seus respectivos locais, é criado uma
    sequencia de 'ifs' e 'elifs', que verificam qual o valor da variavel
    'casa', e adicionam as peças caso o valor seja igual ao da condição.

    --> no fim da função é retornada a matriz tabuleiro.

def mostrar_tabuleiro():
    --> valor esse retornado, usado logo em sequência pela função
    'mostrar_tabuleiro()', que tem como objetivo, formatar a exibição do
    mesmo, a partir de um comando de iteração 'for', é exibida cada linha em
    por iteração, ao lado uma sequencia de valores numéricos que fazem juz ao
    valor de cada linha, e um 'print' final, com a exibição dos caracteres de
    cada coluna. 
```python
    for i in range(8):
        print(f'{8 - i}|',''.join(tabuleiro[i]))
    print('  -----------------\n   A B C D E F G H')
```

def posição_valida():
    --> recebe de parametro a matriz 'tabuleiro' a lista das coordenadas
    chamada 'movimento', a 'peça' (peça selecionada), e o 'lado' cor da
    rodada atual.

    --> é criada a lista posição, que recebe os valores percorridos dentro da
    matriz tabuleiro, a partir da mesma sequencia de dois 'for' como na
    função 'criar_tabuleiro()', ele verifica se a cor atual é branca ou preta
    e ve se a casa que está percorrendo o tabuleiro, tem o mesmo valor da
    peça selecionada pelo usuário.

    --> caso o valor seja o mesmo, a lista posição recebe as coordenadas
    desta casa, e eventualmente, depois de percorrer todas as 64 casas do
    tabuleiro, é retornado o valor da lista 'posição'

def mover_peça():
    --> essa função recebe o valor inteiro da peça selecionada pelo usuário,
    recebe as coordenadas da posição inicial da peça, e da posição de
    destino, recebe a matriz tabuleiro, e o lado atual.

    --> aqui é criada a lista 'movimento', que recebe as posições iniciais e
    finais da peça, lista essa extremamente importante para o funcionamento
    do sistema.

    --> posteriormente é criada uma sequencia de comandos de condição 'match
    case', a partir do valor inteiro de 'peça', ele vai selecionar qual
    função de movimento será chamada, caso o input do usuário seja '1',
    função chamada pelo match case, será 'movimento_peão()', ele faz a mesma
    coisa para as outras peças, e passa de parametro à elas o tabuleiro, a
    lista 'movimento' e o lado atual.

    --> na mesma linha de chamada da função, é criada uma variavel chamada
    'movimento_valido', que usa da lógica proposicional, para atribuir seu
    respectivo valor booleano a partir do retorno da função chamada.

    --> em sequência é chamada a função 'controlar_turno()', que vai retornar
    o valor, que será atribuido ao lado atual.

# peças_linha.py
    --> arquivo esse, um pouco mais complexo, com objetivo de garantir a
    movimentação correta das peças --> torre; bispo e dama, visto que ambas
    essas se movimentam apenas em linhas (movimentos verticais, horizontais e
    perfeitamente diagonais).

def caminho_livre():
    --> função essa, essencial para o funcionamente de ambas peças presentes
    nesse arquivo, ela tem como objetivo, impedir as peças de atravessarem
    outras peças, garantindo maior controle de jogo.

    --> ela começa criando as variaveis 'diferença_linha' e 'diferença_col',
    que recebem a diferença do valor das coordenadas iniciais e finais do
    movimento.

    --> depois cria as variaveis proposicionais dos movimentos verticais e
    horizontais, usando uma lógica simples, caso a diferenças das linha seja
    diferente de 0 e as diferenças das colunas sejam iguais a 0, o movimento
    é vertical, caso contrario o movimento é horizontal.

    --> em seguida a criação da variavel proposicional do movimento diagonal,
    ela verifica o valor absoluto das variaveis diferença_linha e
    diferença_coluna são iguais e diferente de zero, caso seja esse o caso, o
    movimento é diagonal.

    --> depois é criado as variaveis 'passo_linha' e 'passo_coluna', elas são
    essencial para manipular as iterações que percorrem o tabuleiro, elas
    recebem os valores a partir das diferenças de linha e coluna, garantindo
    que caso o valor seja negativo, o passo_linha e coluna também receberam
    um valor negativo de -1 (ou seja elas verificam as casas intermediarias
    dentre a posição inicial da peça até a posição de chegada)
    
    --> é também criado um comando de condição 'if', caso ambos movimento
    vertical, horizontal e diagonal sejam falsos, ele retorna False
    (movimento não se encaixa em nenhum dos padrões calculados por essas
    variaveis, portanto - inválido).

    --> agora a iteração 'while', que continua iterando até que as variaveis
    linha e coluna sejam iguais a linha_final e coluna_final do movimento,
    dentro dessa iteração é chamada a função 'captura_permitida()', que
    retorna o valor recebido pela variavel 'output', caso o output seja
    Falso, é retornado Falso da função 'caminho_livre()', caso não seja True
    é retornado a variavel output, com o valor das coordenadas atuais da
    iteração.

    --> fora da iteração, é chamada novamente a função 'captura_permitida()',
    porém desta vez, ao invez de passar linha e coluna, é passado as
    coordenadas do movimento, isso é necessário para que ele obrigatoriamente 
    retorne algum valor, pois caso não ouvesse essa chamada, ele percorreria
    apenas as casas intermediarias do movimento, deixando assim de exibir
    o print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m'), nas funções de
    movimento em alguns casos específicos.

def movimento_torre():
    --> é feito um import do arquivo tabuleiro.py, diretamente pelas funções 
    de movimento, isso tem como base, evitar erros de ciclos de chamada.

    --> criada uma variavel proposicional que identifica apenas se o
    movimento é diagonal,mas não necessariamente diagonal perfeita, pois no
    caso da torre, oque importa é se é apenas horizontal ou vertical
    portanto, caso esta seja verdadeira, é retornado False em um futuro
    comando de condição. E em sequência, uma variavel proposicional que
    verifica se as coordenadas iniciais e de movimento são ambas iguais.

    --> lista peça[], é usada para passar seu valor para função 'capturar_peça
    ()', do arquivo capturas.py.

    --> chamada da função posição_valida(), de tabuleiro.py. Usada para
    confirmar se a coordenada inicial inserida pelo usuário é verdadeira,
    caso contrário, é retornado False, junto de um print('\033[31mPOSIÇÃO
    ERRADA!\033[0m').

    --> depois desta chamada, é utilazado uma sequencia de comandos de
    condição, com o foco em detectar cada situação inadequada com relação
    as regras do xadrez.

    --> no fim de ambas as condições principais, é chamada a função 'capturar
    _peça()', com uma variavel chamada 'end_game' recebendo seu retorno. Seu
    valor só é igual a 'fim', caso o rei adversário tenha sido capturado, e
    eventualmente o jogo é finalizado.

def movimento_bispo():
    --> em geral ele segue uma sequencia de comandos de condição, muito
    semelhante aos de movimento_torre(), porém possui diferenças, quando
    comparado suas condições de movimento valído, além de receber os mesmos
    parâmetros.

    --> ele verifica apenas se o movimento é perfeitamente diagonal, e pelo
    fato de ja possuir as variaveis de diferença_linha e diferença_col,
    é mais possibilitado a capacidade de adicionar a condição proposicional de
    verificar se o movimento é nulo, pela própria variavel de mov_diagonal,
    ainda mantendo um código visualmente limpo.

    --> todos os outros comandos de condição, são semelhantes aos de 
    movimento_torre()
    
def movimento_dama():
    --> também não foge da mesma semelhança de parâmetros recebidos e
    dos comandos de condição semelhantes, porém utiliza, para sua
    verificação de movimentos, as variaveis mov_vertical; mov_horizontal e
    mov_diagonal, ambas verificam se o movimento é realizado na direção
    perfeita de cada movimento selecionado.

    --> caso nenhuma delas se encaixe com o movimento descrito pelo usuário
    é retornado False, junto da exibição de erro e eventualmente é requisitado
    os dados para o usuário novamente.

# capturas.py:
    --> este arquivo tem como objetivo garantir que a captura das peças
    adversárias ocorra sem erros. Além de desenvolver as funções de movimento
    do rei e do cavalo.

    --> inicia com a criação das constantes globais - uma lista com os
    caracteres de cada peça do tabuleiro, usada para verificar se as
    peças da casa atual, com as peças da lista.

def capturar_peça()
    --> essa função é a etapa final da captura de peças, ela só é
    chamada depois que as funções 'mesma_cor()' e 'capturar_peça()'
    já retornaram valores valídos.

    --> ela faz a atualização do tabuleiro, faz com que ele continue formatado
    de maneira correta, usando a mesma lógica da função 'criar_tabuleiro()', ele
    recebe como parâmetro a variavel parada, que faz com que caso as coordenadas
    de movimento final atravessem uma peça adversária, a peça selecionada pare de
    se movimentar, parando onde ocorreu a captura.

    --> caso a peça que foi capturada seja o rei ele retorna end_game que é
    usado para finalizar o jogo, considerando que ja foi chamada a função
    mesma_cor(), eu não preciso colocar uma condição para cada cor usei o
    valor '1' e não True or False, pois isso facilita quando vou fazer as
    condições dos valores retornados, visto que essa função ja tem outros
    retornos em valores booleanos

def captura_permitida():
    --> segunda função a ser chamada, para verificar se a peça à ser capturada
    é adversária, caso essa condição seja condição seja falsa, é retornado False,
    caso a coordenada final esteja dentro de ('⬜', '⬛'), é retornado True.

    --> por fim, caso a coordenada final, não esteja não esteja em nenhuma das
    condições acima, é retornado 'linha' e 'coluna', que tem o valor das 
    coordenadas finais do movimento. Isso tem como funcionalidade, a exibição
    do print('\033[32mPEÇA ADVERSÁRIA CAPTURADA!\033[0m').

def mesma_cor():
    --> primeira função a ser chamada, para verificar se a peça à ser capturada
    não é da mesma cor, caso essa confição seja falsa é retornado o valor False
    e o print('\033[31mNÃO É POSSÍVEL CAPTURAR UMA PEÇA ALIADA!\033[0m'),
    refazendo as requisições dos inputs para o usuário.

def movimento_rei():
    --> também possui uma estrutura de código muito semelhante, com as funções
    de movimento anteriores, as variaveis booleanas de movimento, garantem os
    movimentos verticais, horizontais e diagonais de apenas uma casa.

    --> caso nenhuma das variaveis sejam verdadeiras é retornado false, e feito
    outra requisição dos dados ao usuário.

    --> nessa função não é chamada a função 'caminho_livre()', pois o movimento
    é de apenas uma casa, tirando assim a necessidade de verificar as peças
    intermediarias do movimento. O resto desta função é semelhante as funções
    de movimento já abordadas no README.    

def movimento_cavalo():
    --> a estrutura desta função também é semelhante as outras de movimento,
    as principais diferenças são observadas nas variaveis de movimento.

    --> essa função possui uma lógica de movimento ainda não abordada no código,
    elas verificam os valores absolutos das variaveis 'diferença_linha' e 
    'diferença_col', com o objetivo de garantir, que o movimento realizado tem o
    formato de 'L', o movimento horizontal do cavalo verifica se o movimento é
    igual a um 'L' deitado.

# peão.py
    --> arquivo esse que possui como objetivo principal, gerenciar o movimento
    do peão, sendo a peça com maior quantidade de requisitos para movimentação.

def movimento_peão():
    --> o peão ele possui uma serie de caracteristicas unicas de movimento, sendo
    elas a capacidade de se mover apenas para frente quando movimento possui como
    objetivo apenas a movimentação, movimento diagonal apenas quando for capturar
    uma peça adversária, ele não pode se movimentar para trás e na primeira
    jogada ele pode se mover 2 peças para frente.

    --> a função tem que cumprir todos esses requisitos, portanto é verificado
    se as variaveis diferença_linha e diferença_col possuem um valor igual a 1 ou
    2, caso o valor seja diferente de qualquer um destes números, é impedido o
    movimento da peça.

    --> a condição para verificar se o peão pode se movimentar 2 casas, é True
    quando o peão está na segunda linha de cada lado do tabuleiro, visto que o
    peão se movimenta apenas para frente, portanto o peão só vai estar na segunda
    linha, quando este não tiver se movido ainda.

    --> caso não seja seu primeiro movimento, é exibido a mensagem de erro
    print('\033[31mO PEÃO NÃO PODE MAIS AVANÇAR DUAS CASAS!\033[0m') e retornado
    False, fazendo uma nova requisição dos dados fornecidos pelo usuário.

    --> esta função também não possui a chamada da função caminho livre, visto que
    esta função só seria utilizada em uma situação muito específica (movimento de
    2 casas), porém é utilizada uma lógica semelhante, como demonstrado no trecho
    do código a seguir:

```python    
    if tabuleiro[linha_intermediaria][movimento[0][1]] not in ('⬜', '⬛'):
        print('\033[31mO PEÃO NÃO PODE AVANÇAR!\033[0m')
        return False
```
    --> para a lógica da movimentação retrógrada, foi usada a variavel lado,
    para conseguir manipular o movimento de maneira mais pratica, caso o lado
    seja branco, a diferença_linha deve possuir um valor positivo, caso preto
    deve possuir um valor negativo.

    --> por fim é verificado se a posição final do peão está dentre ('⬜', '⬛'),
    neste caso, se o movimento for vertical, sua condição veficara se a coordenada
    de chegada esta fora de ('⬜', '⬛'), nesse caso ele não pode avançar. Se o
    movimento for diagonal a coordenada de chegada deve obrigatoriamente estar
    fora de ('⬜', '⬛'), pois o peão só se movimenta na diagonal para a captura
    de uma peça. O resto do código é semelhante as funções de movimento
    anteriormente apresentadas.

def controlar_turno():
    --> caso o movimento valido, o turno é alterado, caso contrario o return é
    o valor original de lado, e eventualmente as requisições ao usuário são
    realizadas novamente sem alterar o turno.
