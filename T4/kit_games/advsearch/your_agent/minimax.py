import random
from typing import Tuple, Callable

def prune_test(state, current_depth:int, max_depth:int) -> bool:
    """
    Returns if the search should be pruned for the given game state and current depth
    :param state: state to make the move (instance of GameState)
    :param current_depth: current depth of search
    :param max_depth: maximum depth of search (-1 = unlimited)
    :return: bool representing whether the search should be pruned
    """
    if max_depth != -1:
        if current_depth >= max_depth or state.is_terminal():
            return True
        else:
            return False
    else:
        return state.is_terminal()

def min(state, alpha, beta, current_depth:int, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    """
    Returns a move computed by the min algorithm with alpha-beta pruning for the given game state
    :param state: state to make the move (instance of GameState)
    :param alpha: alpha value for alpha-beta pruning
    :param beta: beta value for alpha-beta pruning
    :param current_depth: current depth of search
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (float, int, int) tuple with the utility value, x, y coordinates of the move (remember: 0 is the first row/column)
    """
    raise NotImplementedError()

def max(state, alpha, beta, current_depth:int, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    """
    Returns a move computed by the max algorithm with alpha-beta pruning for the given game state
    :param state: state to make the move (instance of GameState)
    :param alpha: alpha value for alpha-beta pruning
    :param beta: beta value for alpha-beta pruning
    :param current_depth: current depth of search
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (float, int, int) tuple with the utility value, x, y coordinates of the move (remember: 0 is the first row/column)
    """
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
