import random
import math
from typing import Tuple

def ucb(node):
    """
    Returns the UCB value for a given node
    :param node: current node
    :return: UCB value
    """
    c = math.sqrt(2) # Arbitrary constant (can be adjusted)
    exploitation_value = node.wins / node.visits
    exploration_value = 2*c * math.sqrt(2 * math.log(node.parent.visits) / node.visits)
    return exploitation_value + exploration_value

def prefered_child(node):
    """
    Returns the most promising next node for a given node. It balances
    exploration and exploitation
    :param node: current node
    :return: node that maximizes the criteria
    """
    best_ucb = float('-inf')
    best_node = None
    for child in node.children:
        ucb_value = ucb(child)
        if ucb_value > best_ucb:
            best_ucb = ucb_value
            best_node = child
    return best_node

class mcts_node:
    """
    Class to represent a node in the MCTS tree. Each node has a state,
    parent, wins, visits and children
    """
    def __init__(self, state, parent=None, wins=0, visits=0, children=[]):
        self.state = state
        self.parent = parent
        self.wins = wins
        self.visits = visits
        self.children = children

    def is_leaf(self):
        """
        Returns whether the node is a leaf or not
        :return: True if the node is a leaf, False otherwise
        """
        return len(self.children) == 0

    def select_node(self):
        """
        Returns the next non-leaf state for a given state following the
        prefered_child criteria
        :return: state that maximizes the criteria
        """
        node = self
        while not node.is_leaf():
            node = prefered_child(node)
        return node

    def expand_node(self):
        """
        Expands the current node and returns the first non-visited child
        :return: next non-visited child or None if node is already expanded
        """
        for move in self.state.legal_moves():
            if move not in self.children:
                self.children.append(move)
                return mcts_node(self.state.next_state(move), self)
        return None

    def simulate_game(self):
        """
        Simulates a game from the current node (taking random moves) and
        getting the result of the match
        :return: result of the match (1 for win, 0 for draw, -1 for loss)
        """
        state = self.state
        while not state.is_terminal():
            move = random.choice(state.legal_moves())
            state = state.next_state(move)
        self.visits += 1
        winner = state.winner()
        if winner == self.state.player:
            self.wins += 1
            return 1
        elif winner is None:
            return 0
        else:
            self.wins -= 1
            return -1

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo retorna uma jogada ilegal
    # Remova-o e coloque a sua implementacao do MCTS

    return (-1, -1)