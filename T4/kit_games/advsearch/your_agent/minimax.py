import random
from typing import Tuple, Callable

def prune_test(state, current_depth:int, max_depth:int) -> bool:
    if max_depth != -1:
        if current_depth >= max_depth or state.is_terminal():
            return True
    else:
        return state.is_terminal()

def min(state, alpha, beta, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    raise NotImplementedError()

def max(state, alpha, beta, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    raise NotImplementedError()

def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    raise NotImplementedError()
