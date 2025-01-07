import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .othello_minimax_custom import make_move as custom

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    Consider that this will be called in the Othello tournament situation,
    so you should call the best implementation you got.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    return custom(state)