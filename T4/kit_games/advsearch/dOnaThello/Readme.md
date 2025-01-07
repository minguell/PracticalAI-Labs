# Trabalho 4 – Busca Competitiva

## Integrantes do Grupo (Turma A):

- Ana Cláudia Rodrigues (00343123);
- Miguel Dutra Fontes Guerra (00342573);
- Pedro Lubaszewski Lima (00341810).

## Avaliação do Minimax para o Tic-Tac-Toe Misere:

(i)   O minimax sempre ganha jogando contra o randomplayer.
- Minimax TTTM x randomplayer:
    - Ganhador: Minimax TTTM;
        " W    W   B "
        " W    B   B "
        " W    B   . "

- randomplayer x Minimax TTTM:
    - Ganhador: Minimax TTTM;
        " B    W   . "
        " W    B   W "
        " .    B   B "
        
(ii)  O minimax sempre empata consigo mesmo.
        " N    B   W "
        " W    B   B "
        " B    W   W "
        
(iii) O minimax não perde para você ao usarmos nossa melhor estratégia; O melhor resultado obtido é o empate.
        " W    B   B "
        " B    B   W "
        " W    W   B "
        

## Implementações para o Othello:

### Heurística Customizada:

Basicamente a heurística customizada combina três critérios principais como mobilidade (multiplicado por 5), diferença de peças (multiplicado por 2) e peças estáveis (multiplicado por 13). O primeiro diz respeito ao número de jogadas válidas para o jogador, pela função state.legal_moves(), contando positivamente se for turno do jogador e negativamente se for turno do inimigo. O segundo critério conta a diferença do número de peças do jogador e do inimigo, com as funções board_num_player() para contar o número de peças de cada e uma subtração simples para o cálculo.  Por fim, peças estáveis é o critério que indica as peças que não podem cer capturadas por outros jogadores, geralmente estão na quina ou cercada pelas outras peças, sendo verificadas pela função count_stable_pieces.

### Critério de Parada do Agente:

Para o agente que utiliza a Heurística de Contagem de peças, o critério de parada utilizado foi a profundidade máxima de 5 (partindo
da profundidade 0 na raiz). Esse número foi escolhido a partir de testes empíricos em partidas consigo mesmo (o agente contra o próprio
agente em algumas partidas); se o agente agisse de forma rápida, sem perder jogadas por inatividade, então esse seria um bom número de
profundidade.

Já o agente com heurística de Valor posicional tem critério de parada por profundida máxima 4, valor adquirido empiricamente.

Por fim, o agente com heurística customizada tem critério de parada de profundidade máxima de 4, também testado empiricamente.

### Avaliação do Minimax para o Othello:

Resultados do Mini-torneio:

- Contagem de peças x Valor posicional:
    - Ganhador: Valor posicional;
    - Quantidade de peças ao final da partida: 23 (Contagem de peças) x 41 (Valor posicional);

- Valor posicional x Contagem de peças:
    - Ganhador: Valor posicional;
    - Quantidade de peças ao final da partida: 45 (Valor posicional) x 19 (Contagem de peças);

- Contagem de peças x Heurística customizada:
    - Ganhador: Heurística customizada;
    - Quantidade de peças ao final da partida: 19 (contagem de peças) x 45 (Heurística customizada);

- Heurística customizada x Contagem de peças:
    - Ganhador: Heurística customizada;
    - Quantidade de peças ao final da partida: 45 (Heurística customizada) x 19 (Contagem de peças);

- Valor posicional x Heurística customizada:
    - Ganhador: Valor posicional;
    - Quantidades de peças ao final da partida: 33 (Valor posicional) x 31 (Heurística customizada);

- Heurística customizada x Valor posicional:
    - Ganhador: Valor posicional;
    - Quantidade de peças ao final da partida: 20 (Heurística customizada) x 44 (Valor posicional);

- MCTS x Contagem de peças:
    - Ganhador: Contagem de peças;
    - Quantidade de peças ao final da partida: 0 (MCTS) x 26 (Contagem de peças);

- Contagem de peças x MCTS:
    - Ganhador: Contagem de peças;
    - Quantidade de peças ao final da partida: 38 (Contagem de peças) x 26 (MCTS);

- MCTS x Heurística customizada:
    - Ganhador: Heurística customizada;
    - Quantidade de peças ao final da partida: 4 (MCTS) x 58 (Heurística customizada);

- Heurística customizada x MCTS:
    - Ganhador: Heurística customizada;
    - Quantidade de peças ao final da partida: 36 (Heurística customizada) x 28 (MCTS).

A implementação mais bem sucedida foi a de Valor Posicional, que capturou mais peças do que a Heurística Customizada (com a qual empatou).

- Valor posicional:
    - Vitórias no total: 4;
    - Peças capturadas no total: 163;

- Heurística Costumizada:
    - Vitórias no total: 4;
    - Peças capturadas no total: 141.

### Implementação do Torneio:

Como todos os alunos terão as mesmas implementações para as heurísticas de contagem de peças e de valor posicional, o grupo escolheu a sua implementação com heurística customizada para colocar no torneio (que foi a segunda melhor implementação e é diferente das demais).

### Extras:

Foi implementado o agente genérico com MCTS (testado em ambos os jogos). Essa implementação conta com uma nova classe chamada de
mcts_node. Os objetos dessa classe apresentam os métodos descritos no algoritmo original do MCTS. Ou seja, há um método de seleção,
um de expansão, um de simulação e um de retropropagação dos resultados para os nodos. Além disso, para facilitar o método de seleção,
criou-se uma função de escolha de filho preferido a qual chama uma função de cálculo do UCB de todos os filhos de um nodo. A constante
do UCB é ajustável no código e está atualmente configurada para raiz quadrada de 2. Ademais, há também um método para computar a melhor
jogada a partir de um certo nodo.

Com essas implementações, realizou-se o encadeamento desses métodos na função make_move() do arquivo mcts.py, onde os critérios de parada
para a construção da árvore do algoritmo são o tempo máximo de 5s (determinado pelo próprio servidor de jogos como tempo máximo de timeout)
e o número máximo de iterações do loop que é ajustável (atualmente está configurado para 2000).