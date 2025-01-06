import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Funções auxiliares
def count_stable_pieces(board: Board, player: str) -> int:
    """
    Conta as peças estáveis (que não podem ser capturadas).
    Isso inclui peças nas quinas ou completamente cercadas por outras peças do mesmo jogador.
    """
    stable_count = 0
    tiles = board.tiles

    
    stable_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]  # Quinas
    for x, y in stable_positions:
        if tiles[y][x] == player:
            stable_count += 1


    return stable_count


# Função principal de avaliação 
def evaluate_custom(state: GameState, player: str) -> float:
    """
    Avalia um estado do jogo Othello do ponto de vista do jogador especificado.
    Retorna um valor heurístico baseado em múltiplos critérios.
    """
    opponent = 'B' if player == 'W' else 'W'


    if state.is_terminal():
        winner = state.get_winner()
        if winner == player:
            return float('inf')  
        elif winner == opponent:
            return float('-inf')  
        else:
            return 0  


    board = state.board

    edge_positions = [(0, 0), (0, 7), (7, 0), (7, 7)] 
    edge_value = sum(1 if board.tiles[y][x] == player else -1 for x, y in edge_positions)

    player_moves = len(state.get_valid_moves(player))
    opponent_moves = len(state.get_valid_moves(opponent))
    mobility = player_moves - opponent_moves

    player_count = board.tiles_str().count(player)
    opponent_count = board.tiles_str().count(opponent)
    piece_difference = player_count - opponent_count

    stable_pieces = count_stable_pieces(board, player)

    return 10 * edge_value + 5 * mobility + 2 * piece_difference + 3 * stable_pieces


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada para o estado do jogo usando minimax com poda alfa-beta
    e a função de avaliação customizada.
    """
    return minimax_move(state, depth=4, evaluate=evaluate_custom)
