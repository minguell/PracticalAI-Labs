import random
import math
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move
   
    _, best_move = minimax_alpha_beta(state, depth=-1, alpha=-math.inf, beta=math.inf, maximizing=True,player=state.player)
    return best_move

def minimax_alpha_beta(state: GameState, depth: int, alpha: float, beta: float, maximizing: bool, player: str) -> Tuple[float, Tuple[int, int]]:
    """
    Implementação do algoritmo Minimax com poda alfa-beta.
    :param state: estado atual do jogo
    :param depth: profundidade máxima (-1 para ilimitada)
    :param alpha: valor alfa para poda
    :param beta: valor beta para poda
    :param maximizing: True se for a vez do jogado; False, caso contrário
    :param player: jogador para quem estamos calculando o valor ('B' ou 'W')
    :return: Tupla (valor da avaliação, melhor movimento)
    """

    if state.is_terminal():
        return utility(state, state.player), None

    best_move = None

    if maximizing:
        max_eval = -math.inf
        for move in state.legal_moves():
            next_state = state.next_state(move)
            eval, _ = minimax_alpha_beta(next_state, depth -1, alpha, beta, False, player)
            if eval > max_eval:
                max_eval = eval
                best_move = move 
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in state.legal_moves():
            next_state = state.next_state(move)
            eval, _ = minimax_alpha_beta(next_state, depth -1, alpha, beta, True, player)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def utility(state, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    winner = state.board.check_winner()

    if winner == player:
        return -1
    
    elif winner != 'D' and winner is not None:
        return -1
    
    return 0

