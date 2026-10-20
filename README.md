# xadrez_python
Projeto de lógica de programação do jogo xadrez, desenvolvido inteiramente em Python.

- main.py: 

def main():
    --> arquivo inicial do projeto, ele faz a primeira chamada da função 'criar_tabuleiro()' do arquivo 'tabuleiro.py', função essa que não recebe parametro nenhum, porém retorna toda a matriz do tabuleiro.
    --> em sequência, incia-se o processo de iteração, que faz uma serie de requisições dos dados para o usuário, sendo essas:

    --> qual peça será jogada; coordenada inicial da peça e coordenada final da peça - essenciais para a execução do resto das funções do código.

    --> aqui é criada a variavel booleana 'lado' (define qual a cor do tabuleiro que ira jogar), a mesma é passada de parametro para a função 'mover_peça()' do arquivo 'tabuleiro.py', logo em sequencia a chamada da função 'mostrar_tabuleiro()' também do arquivo 'tabuleiro.py', garantindo a exibição do mesmo a cada jogada bem sucedida.

    --> todas as requisições feitas ao usuário são validadas, caso o input seja invalido, é feita outra requisição dos mesmo dados, para o usuário.

    --> as coordenadas informadas pelo usuário, seguem o mesmo padrão do tabuleiro original de xadrez, onde as linha são representadas numericamente e as colunas as partir da sequência de caracteres --> 'A','B','C','D','E','F','G','H'.

    --> para transforma-las em um valor numérico valído, para a manipulação da matriz 'tabuleiro', foi necessário o uso de um cálculo lógico simples, onde a linha = 8 - linha, isso é necessário pois as linhas de uma matriz, começam em zero e num tabuleiro de xadrez o lado branco começa na 8º linha, já o lado preto na 1º, portanto caso o usuário queira escolher uma peça preta da 1º linha, o calculo seria linha = 8 - 1, totalizando 7, valor esse referente a ultima linha da matriz. No caso da coluna, foi necessário outro cálculo consideravelmente simples, onde é usada a função ord(), que retorna um valor unicode de um caractere, essencial para que eu transformasse um caractere em um numero inteiro, é usada como base para a subtração o "ord('A')", pois o caractere 'A', faz referência a primeira coluna, ou seja caso a coluna inserida pelo usuário seja a primeira, o valor de coluna é '0', caso seja a ultima, valor retornado é igual a '7'.

- tabuleiro.py:

def criar_tabuleiro():
    --> sendo essa a primeira função chamada por 'main.py', como o nome ja diz, cria o tabuleiro inicial.

    --> é usada para a criação uma sequência simples de iteração, utilizando dois 'for' ambos iterando 8 vezes, o primeiro tem como função principal resetar o valor da lista 'linha' a cada iteração, pois a cada iteração do primeiro 'for', o segundo é executado 8 vezes, garantindo que a variavel 'casa' percorra todas as 64 casas de um tabuleiro, no segundo 'for' é utilizada como base para a criação das casas do tabuleiro, uma variavel chamada 'casa', com valor inicial de 0, valor esse que é somado + 1 à ele, depois de cada iteração do segundo 'for', logo em sequência, é usado um comando de condição 'if' que verifica se a linha do tabuleiro é par ou não, isso inverte a posição das casas a cada iteração, quando a variavel 'casa' é par é atribuido ao tabuleiro o icone '⬜', quando ele é impar '⬛', esses símbolos fazem referência a cor de cada casa do tabuleiro, caso a linha seja ímpar, é executado um comando de condição 'else', que inverte a lógica. Portanto o primeiro 'for' percorre as linhas do tabuleiro, e o segundo as colunas, as inverções do if e else, são essenciais para garantir que a o tabuleiro possua uma troca das colorações das casas adequadamente.

    --> depois de já criado o tabuleiro com as cores de cada casa, é necessário adicionar as peças em seus respectivos locais, é criado uma sequencia de 'ifs' e 'elifs', que verificam qual o valor da variavel 'casa', e adicionam as peças caso o valor seja igual ao da condição.

    --> no fim da função é retornada a matriz tabuleiro.

def mostrar_tabuleiro():
    --> valor esse retornado, usado logo em sequência pela função 'mostrar_tabuleiro()', que tem como objetivo, formatar a exibição do mesmo, a partir de um comando de iteração 'for', é exibida cada linha em por iteração, ao lado uma sequencia de valores numéricos que fazem juz ao valor de cada linha, e um 'print' final, com a exibição dos caracteres de cada coluna. 

def posição_valida():
    --> recebe de parametro a matriz 'tabuleiro' a lista das coordenadas chamada 'movimento', a 'peça' (peça selecionada), e o 'lado' cor da rodada atual.

    --> é criada a lista posição, que recebe os valores percorridos dentro da matriz tabuleiro, a partir da mesma sequencia de dois 'for' como na função 'criar_tabuleiro()', ele verifica se a cor atual é branca ou preta e ve se a casa que está percorrendo o tabuleiro, tem o mesmo valor da peça selecionada pelo usuário.

    --> caso o valor seja o mesmo, a lista posição recebe as coordenadas desta casa, e eventualmente, depois de percorrer todas as 64 casas do tabuleiro, é retornado o valor da lista 'posição'

def mover_peça():
    --> essa função recebe o valor inteiro da peça selecionada pelo usuário, recebe as coordenadas da posição inicial da peça, e da posição de destino, recebe a matriz tabuleiro, e o lado atual.

    --> aqui é criada a lista 'movimento', que recebe as posições iniciais e finais da peça, lista essa extremamente importante para o funcionamento do sistema.

    --> posteriormente é criada uma sequencia de comandos de condição 'match case', a partir do valor inteiro de 'peça', ele vai selecionar qual função de movimento será chamada, caso o input do usuário seja '1', a função chamada pelo match case, será 'movimento_peão()', ele faz a mesma coisa para as outras peças, e passa de parametro à elas o tabuleiro, a lista 'movimento' e o lado atual.

    --> na mesma linha de chamada da função, é criada uma variavel chamada 'movimento_valido', que usa da lógica proposicional, para atribuir seu respectivo valor booleano a partir do retorno da função chamada.

    --> em sequência é chamada a função 'controlar_turno()', que vai retornar o valor, que será atribuido ao lado atual.

- peças_linha.py
    --> arquivo esse, um pouco mais complexo, com objetivo de garantir a movimentação correta das peças --> torre; bispo e dama, visto que ambas essas se movimentam apenas em linhas (movimentos verticais, horizontais e perfeitamente diagonais).

def caminho_livre():
    --> função essa, essencial para o funcionamente de ambas peças presentes nesse arquivo, ela tem como objetivo, impedir as peças de atravessarem outras peças, garantindo maior controle de jogo.

    --> ela começa criando as variaveis 'diferença_linha' e 'diferença_col', que recebem a diferença do valor das coordenadas iniciais e finais do movimento.

    --> depois cria as variaveis proposicionais dos movimentos verticais e horizontais, usando uma lógica simples, caso a diferenças das linha seja diferente de 0 e as diferenças das colunas sejam iguais a 0, o movimento é vertical, caso contrario o movimento é horizontal.

    --> em seguida a criação da variavel proposicional do movimento diagonal, ela verifica o valor absoluto das variaveis diferença_linha e diferença_coluna são iguais e diferente de zero, caso seja esse o caso, o movimento é diagonal.

    --> depois é criado as variaveis 'passo_linha' e 'passo_coluna', elas são essencial para manipular as iterações que percorrem o tabuleiro, elas recebem os valores a partir das diferenças de linha e coluna, garantindo que caso o valor seja negativo, o passo_linha e coluna também receberam um valor negativo de -1 (ou seja elas verificam as casas intermediarias dentre a posição inicial da peça até a posição de chegada)
    
    --> é também criado um comando de condição 'if', caso ambos movimento vertical, horizontal e diagonal sejam falsos, ele retorna False (movimento não se encaixa em nenhum dos padrões calculados por essas variaveis, portanto - inválido).

    --> agora a iteração 'while', que continua iterando até que as variaveis linha e coluna sejam iguais a linha_final e coluna_final do movimento, dentro dessa iteração é chamada a função 'captura_permitida()', que retorna o valor recebido pela variavel 'output', caso o output seja Falso, é retornado Falso da função 'caminho_livre()', 

