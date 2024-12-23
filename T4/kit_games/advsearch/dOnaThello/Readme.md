# Trabalho 4 – Busca Competitiva

## Integrantes do Grupo (Turma A):

- Ana Cláudia Rodrigues (00343123);
- Miguel Dutra Fontes Guerra (00342573);
- Pedro Lubaszewski Lima (00341810).

## Avaliação do Minimax para o Tic-Tac-Toe Misere:

<!-- 
    Colocar aqui um relatório do desempenho da implementação do Minimax para o Tic-Tac-Toe Misere. Além disso, responder:
    (i)   O minimax sempre ganha ou empata jogando contra o randomplayer?
    (ii)  O minimax sempre empata consigo mesmo?
    (iii) O minimax não perde para você quando você usa a sua melhor estratégia?
-->

## Implementações para o Othello:

### Heurística Customizada:

<!--
    Explicar como funciona e como foi elaborada a heurística customizada. Se foi consultada alguma fonte (site, livro, ...),
    referenciar aqui e explicar como que foi utilizado o conteúdo da referência (foi implementado exatamente como a referência,
    foi a inspiração para a implementação, foi uma combinação dessa e mais alguma outra referência, etc.).
-->

### Critério de Parada do Agente:

Para o agente que utiliza a Heurística de Contagem de Peças, o critério de parada utilizado foi a profundidade máxima de 5 (partindo
da profundidade 0 na raiz). Esse número foi escolhido a partir de testes empíricos em partidas consigo mesmo (o agente contra o próprio
agente em algumas partidas); se o agente agisse de forma rápida, sem perder jogadas por inatividade, então esse seria um bom número de
produndidade.

<!--
    Explicar qual foi o critério de parada do algoritmo minimax para os demais agentes de Othello (profundidade máxima fixa?
    aprofundamento iterativo parado por tempo? Etc...).
-->

### Avaliação do Minimax para o Othello:

<!--
    Realizar o mini-torneio abaixo, relatando quem ganhou (ou se houve empate) em cada partida e o número final de peças de cada
    agente. Na lista a seguir, o nome do agente da esquerda começa a jogar naquela partida:
    Partidas:
    - Contagem de peças x Valor posicional;
    - Valor posicional x Contagem de peças;
    - Contagem de peças x Heurística customizada;
    - Heurística customizada x Contagem de peças;
    - Valor posicional x Heurística customizada;
    - Heurística customizada x Valor posicional;
    - MCTS x Contagem de peças;
    - Contagem de peças x MCTS;
    - MCTS x Valor posicional;
    - Valor posicional x MCTS;
    - MCTS x Heurística customizada;
    - Heurística customizada x MCTS.

    Relatar também qual foi a implementação mais bem sucedida de todas (com mais vitórias e, em caso de empates, que capturou mais
    peças).
-->

### Implementação do Torneio:

<!--
    Explicar qual e o porquê da implementação escolhida para o torneio.
-->

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

<!--
    Relatar quaisquer outros extras implementados ao longo do trabalho (como melhorias não vistas em aula).
-->