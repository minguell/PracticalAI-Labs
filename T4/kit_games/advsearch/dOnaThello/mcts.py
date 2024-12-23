import random
import math
import time
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
    def __init__(self, state, parent=None, parent_move=(-1, -1), wins=0, visits=0, children=[]):
        self.state = state
        self.parent = parent
        self.parent_move = parent_move
        self.wins = wins
        self.visits = visits
        self.children = list(children)

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
        # Discover the movements of children
        children_moves = set()
        for child in self.children:
            children_moves.add(child.parent_move)

        # Check if a move is already in the movements of children
        new_child = self
        if self.state.is_terminal():
            return new_child
        legal_moves = set(self.state.legal_moves())
        for move in legal_moves:
            new_child = mcts_node(self.state.next_state(move), self, move)
            if move not in children_moves:
                self.children.append(new_child)
                return new_child
        return new_child

    def get_root(self):
        """
        Returns the root of the tree
        :return: root of the tree
        """
        node = self
        while node.parent is not None:
            node = node.parent
        return node

    def simulate_game(self):
        """
        Simulates a game from the current node (taking random moves) and
        getting the result of the match
        :return: result of the match (1 for win, 0 for draw, -1 for loss)
        """
        # Discover the player of the root of the tree
        player = self.get_root().state.player

        # Simulate the rest of the game randomly
        state = self.state
        while not state.is_terminal():
            move = random.choice(list(state.legal_moves()))
            state = state.next_state(move)
        winner = state.winner()
        if winner == player:
            return 1
        elif winner is None:
            return 0
        else:
            return -1

    def backpropagate(self, result):
        """
        Backpropagates the result of the last match to parent nodes
        :param result: result of the match (1 for win, 0 for draw, -1 for loss)
        """
        # Discover the player of the root of the tree
        player = self.get_root().state.player

        # Backprogate the result to the parent nodes (respecting the player of each node)
        node = self
        while node is not None:
            node.visits += 1
            node_player = node.state.player
            if node_player == player:
                node.wins += result
            else:
                node.wins -= result
            node = node.parent

    def get_best_move(self) -> Tuple[int, int]:
        """
        Returns the best move for the current node
        :return: (int, int) tuple with x, y coordinates of the best move (remember: 0 is the first row/column)
        """
        best_score = float('-inf')
        best_move = (-1, -1)
        for child in self.children:
            score = child.wins / child.visits
            if score > best_score:
                best_score = score
                best_move = child.parent_move
        return best_move

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    max_iterations = 2000 # Adjustable parameter
    max_time = 5
    initial_time = time.time()
    spent_time = 0
    iterations = 0
    root = mcts_node(state)
    while spent_time < max_time and iterations < max_iterations:
        node = root.select_node()
        node = node.expand_node()
        result = node.simulate_game()
        node.backpropagate(result)
        iterations += 1
        spent_time = time.time() - initial_time
    return root.get_best_move()