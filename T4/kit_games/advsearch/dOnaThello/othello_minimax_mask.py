import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Você pode criar funções auxiliares neste arquivo
# e também módulos auxiliares neste pacote.
#
# Não esqueça de renomear 'your_agent' com o nome
# do seu agente.

# mask template adjusted from https://web.fe.up.pt/~eol/IA/MIA0203/trabalhos/Damas_Othelo/Docs/Eval.html
# could optimize for symmetries but just put all values here for coding speed :P
# DO NOT CHANGE! 

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def evaluate_mask(state, player: str) -> float:
    """
    Avalia um estado de Othello baseado nos valores posicionais das peças no tabuleiro.
    Se o estado for terminal, retorna sua utilidade.
    Se for não terminal, retorna uma estimativa com base no valor posicional das peças.
    :param state: estado a ser avaliado (instância de GameState)
    :param player: jogador a ser avaliado (B ou W)
    :return: valor estimado do estado para o jogador
    """
    opponent = 'W' if player == 'B' else 'B'  
    board = state.board.tiles  
    score = 0

    for y in range(8): 
        for x in range(8):
            if board[y][x] == player: 
                score += EVAL_TEMPLATE[y][x]
            elif board[y][x] == opponent:  
                score -= EVAL_TEMPLATE[y][x]

    return score

def make_move(state) -> Tuple[int, int]:
    """
    Calcula e retorna a melhor jogada usando minimax com poda alfa-beta e a heurística de valor posicional.
    :param state: estado do jogo
    :return: tupla (x, y) com as coordenadas da jogada escolhida
    """
    depth = 4  
    return minimax_move(state, depth, evaluate_mask)
