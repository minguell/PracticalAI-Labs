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

def minimax_min(state, alpha:float, beta:float, current_depth:int, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
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
    if prune_test(state, current_depth, max_depth):
        return eval_func(state, state.player), (-1, -1)
    v = float('inf')
    a = (-1, -1)
    current_depth += 1
    for move in state.legal_moves():
        new_state = state.next_state(move)
        u, _ = minimax_max(new_state, alpha, beta, current_depth, max_depth, eval_func)
        if u < v:
            v = u
            a = move
            beta = min(beta, v)
            if alpha >= beta:
                break
    return v, a

def minimax_max(state, alpha:float, beta:float, current_depth:int, max_depth:int, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
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
    if prune_test(state, current_depth, max_depth):
        return eval_func(state, state.player), (-1, -1)
    v = float('-inf')
    a = (-1, -1)
    current_depth += 1
    for move in state.legal_moves():
        new_state = state.next_state(move)
        u, _ = minimax_min(new_state, alpha, beta, current_depth, max_depth, eval_func)
        if u > v:
            v = u
            a = move
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    return v, a

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
    _, move = minimax_max(state, float('-inf'), float('inf'), 0, max_depth, eval_func)
    return move
