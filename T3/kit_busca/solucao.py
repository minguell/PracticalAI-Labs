from typing import Iterable, Set, Tuple
from queue import Queue, LifoQueue, PriorityQueue
import time

class Nodo:
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def get_estado(self):
        return self.estado

    def get_pai(self):
        return self.pai

    def get_acao(self):
        return self.acao    

    def get_custo(self):
        return self.custo

    def __eq__(self, other):
        # Utilizada para comparar nodos
        if self.get_estado() == other.get_estado() and \
           self.get_acao() == other.get_acao():
            return True
        else:
            return False

    def __hash__(self):
        # Utilizada para mapear nodos em um conjunto
        return hash((self.estado, self.acao))
    
    def __str__(self):
        # Utilizada para imprimir nodos em uma string (debug)
        return f"Estado: {self.get_estado()}, Estado Pai: {self.get_pai().get_estado() if self.get_pai() is not None else None}, Acao: {self.get_acao()}, Custo: {self.get_custo()}"

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:str, representação do estado do 8-puzzle
    :return:Set[Tuple[str,str]], retorna um conjunto de tuplas (acao, estado) que o estado de entrada pode acessar
    """
    if estado is None or estado == "":
        return set()

    # Descobre espaço vazio ("_")
    pos_vazio = estado.index("_")
    acoes = []
    # Converte pra linha e coluna
    linha, coluna = divmod(pos_vazio, 3)

    # Movimentos possíveis
    movimentos = {
        "acima": (linha - 1, coluna),
        "abaixo": (linha + 1, coluna),
        "esquerda": (linha, coluna - 1),
        "direita": (linha, coluna + 1)
    }

    for acao, (nova_linha, nova_coluna) in movimentos.items():
        # Garante que o movimento é válido 
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            # Calcula novo vazio
            nova_pos = nova_linha * 3 + nova_coluna
            # Troca o "_" pela nova posição
            estado_lista = list(estado)
            estado_lista[pos_vazio], estado_lista[nova_pos] = estado_lista[nova_pos], "_"
            novo_estado = "".join(estado_lista)
            acoes.append((acao, novo_estado))

    return set(acoes)

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo:Nodo, objeto da classe Nodo (estado inicial)
    :return:Set[Nodo], conjunto com os nodos sucessores do nodo recebido
    """
    # Inicializa o conjunto de sucessores como vazio para evitar erros
    sucessores = set()
    if nodo is not None:
        # Converte todas as tuplas de ação, estado atingíveis pelo nodo raiz em nodos sucessores 
        for acao, estado in sucessor(nodo.get_estado()):
            sucessores.add(Nodo(estado, nodo, acao, nodo.get_custo() + 1))
    return sucessores

def hamming(estado: str)-> int:
    """
    Calcula a heurística de Hamming para o estado.
    Número de peças fora do lugar em relação ao objetivo.
    """
    objetivo = "12345678_"
    return sum(1 for i in range(len(estado)) if estado[i] != objetivo[i])

def manhattan(estado: str)-> int:
    """
    Calcula a heurística de Manhattan para o estado.
    Soma das distâncias de Manhattan para cada peça até sua posição objetivo.
    """
    objetivo = "12345678_"
    distancia = 0
    for i, val in enumerate(estado):
        pos_objetivo = objetivo.index(val)
        linha_atual, coluna_atual = divmod(i, 3)
        linha_objetivo, coluna_objetivo = divmod(pos_objetivo, 3)
        distancia += abs(linha_atual - linha_objetivo) + abs(coluna_atual - coluna_objetivo)
    return distancia

def astar(estado:str,heuristica)->list[str]:
    """
    Recebe um estado (string), executa a busca A* e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Recebe heurística específica, podendo ser de Hamming ou Manhattan.
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str, estado inicial do problema
    :param heuristica: function, função heurística indicada
    :return: list[str], lista de ações que levam até o objetivo
    """
    objetivo = "12345678_"
    raiz = Nodo(estado, None, None, 0)
    visitados = set()
    solucao = []
    fronteira = PriorityQueue()
    fronteira.put((heuristica(estado),raiz))
    nodos_expandidos = 0

    while not fronteira.empty():
        _, nodo = fronteira.get()

        if nodo.get_estado() == objetivo:
            print(f'\nA* ({heuristica._name_})')
            print(f'Número de nós expandidos: {nodos_expandidos}')
            print(f'Custo da Solução: {nodo.get_custo()}\n')

            while nodo is not raiz:
                solucao.append(nodo.get_acao())
                nodo = nodo.get_pai()
            return solucao[::-1]
        
        if nodo not in visitados:
            visitados.add(nodo)
            for sucessor in expande(nodo):
                if sucessor not in visitados:
                    custo_total = sucessor.get_custo() + heuristica(sucessor.get_estado())
                    fronteira.put((custo_total, sucessor))
            nodos_expandidos += 1
    
    print(f'\nA* ({heuristica._name_}):')
    print(f'Número de nós expandidos: {nodos_expandidos}')
    print(f'Solução não encontrada')
    return None

def astar_hamming(estado:str)->list[str]:
    """
    Busca A* com heurística de Hamming.
    """
    return astar(estado,hamming)

def astar_manhattan(estado:str)->list[str]:
    """
    Busca A* com heurística de Manhattan.
    """
    return astar(estado,manhattan)

def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado:str, estado inicial do problema
    :return: list[str], lista de ações que levam até o objetivo
    """
    objetivo = "12345678_"
    raiz = Nodo(estado, None, None, 0)
    visitados = set()
    solucao = []
    fronteira = Queue()
    fronteira.put(raiz)
    nodos_expandidos = 0

    while True:
        # Neste caso, não foi encontrada uma solução (o problema é impossível)
        if fronteira.empty():
            print(f'BFS:\nA quantidade de nodos expandidos foi {nodos_expandidos}.')
            print(f'Solução não encontrada.\n')
            return None

        # Para o BFS, a expansão é feita em largura (desenfileirando nodos da fronteira)
        nodo = fronteira.get()
        if nodo.get_estado() == objetivo:
            print(f'\nBFS:\nA quantidade de nodos expandidos foi {nodos_expandidos}.')
            print(f'Custo da solução: {nodo.get_custo()}\n')
            # Descobre a ordem das ações reversamente, revertendo-as na saída
            while nodo is not raiz:
                solucao.append(nodo.get_acao())
                nodo = nodo.get_pai()
            return solucao[::-1]

        # Só visita nodos não explorados
        if nodo not in visitados:
            visitados.add(nodo)
            for sucessor in expande(nodo):
                if sucessor not in visitados:
                    fronteira.put(sucessor)
            nodos_expandidos += 1

def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado:str, estado inicial do problema
    :return: list[str], lista de ações que levam até o objetivo
    """
    objetivo = "12345678_"
    raiz = Nodo(estado, None, None, 0)
    visitados = set()
    solucao = []
    fronteira = LifoQueue()
    fronteira.put(raiz)
    nodos_expandidos = 0

    while True:
        # Neste caso, não foi encontrada uma solução (o problema é impossível)
        if fronteira.empty():
            print(f'DFS:\nA quantidade de nodos expandidos foi {nodos_expandidos}.')
            print(f'Solução não encontrada.\n')
            return None

        # Para o BFS, a expansão é feita em profundidade (desempilhando nodos da fronteira)
        nodo = fronteira.get()
        if nodo.get_estado() == objetivo:
            print(f'\nDFS:\nA quantidade de nodos expandidos foi {nodos_expandidos}.')
            print(f'Custo da solução: {nodo.get_custo()}\n')
            # Descobre a ordem das ações reversamente, revertendo-as na saída
            while nodo is not raiz:
                solucao.append(nodo.get_acao())
                nodo = nodo.get_pai()
            return solucao[::-1]

        # Só visita nodos não explorados
        if nodo not in visitados:
            visitados.add(nodo)
            for sucessor in expande(nodo):
                if sucessor not in visitados:
                    fronteira.put(sucessor)
            nodos_expandidos += 1

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado:str, estado inicial do problema
    :return: list[str], lista de ações que levam até o objetivo
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

if __name__ == "__main__":
    start_bfs = time.time()
    print(bfs("2_3541687"))
    end_bfs = time.time()
    print(f'\nTempo de execução do algoritmo BFS: {end_bfs - start_bfs} segundos.\n')

    start_dfs = time.time()
    dfs("2_3541687")
    end_dfs = time.time()
    print(f'\nTempo de execução do algoritmo DFS: {end_dfs - start_dfs} segundos.\n')

    start_hamming = time.time()
    astar_hamming("2_3541687")
    end_hamming = time.time()
    print(f'\nTempo de execução do algoritmo A* com heurística de Hamming: {end_hamming - start_hamming} segundos.\n')

    start_manhattan = time.time()
    astar_manhattan("2_3541687")
    end_manhattan = time.time()
    print(f'\nTempo de execução do algoritmo A* com heurística de Manhattan: {end_manhattan - start_manhattan} segundos.\n')