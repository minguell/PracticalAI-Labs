from typing import Iterable, Set, Tuple

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
        if self.get_estado() == other.get_estado() and self.get_acao() == other.get_acao() and self.get_custo() == other.get_custo():
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.estado, self.acao, self.custo))

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:str, representação do estado do 8-puzzle
    :return:Set[Tuple[str,str]], retorna um conjunto de tuplas (acao, estado) que o estado de entrada pode acessar
    """
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
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError