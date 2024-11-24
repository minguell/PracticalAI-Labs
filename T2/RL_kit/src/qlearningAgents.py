# Trabalho 2 – Aprendizado por Reforço
# Arquivo qlearningAgents.py
#
# Integrantes do Grupo (Turma A):
# - Ana Cláudia Rodrigues (00343123);
# - Miguel Dutra Fontes Guerra (00342573);
# - Pedro Lubaszewski Lima (00341810).

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    def __init__(self, **args):
        ReinforcementAgent.__init__(self, **args)

        # Initialize QValues table
        self.QValues = {}

    def getQValue(self, state, action):
        # Check if it's necessary to append a new state to the QValues
        if state not in self.QValues:
            self.QValues[state] = {}
            for action in self.getLegalActions(state):
                self.QValues[state][action] = 0.0
        return self.QValues[state][action]

    def computeValueFromQValues(self, state):
        # Returns 0.0 if there is no legal action
        maxValue = 0.0
        stateActions = self.getLegalActions(state)
        if len(stateActions) != 0:
          # Otherwise, returns the biggest QValue of the state
          stateQValues = []
          for action in stateActions:
              stateQValues.append(self.getQValue(state, action))
          maxValue = max(stateQValues)
        return maxValue

    def computeActionFromQValues(self, state):
        # Returns None if there is no legal action
        bestAction = None
        stateActions = self.getLegalActions(state)
        if len(stateActions) != 0:
          # Otherwise, returns the action that maximizes the QValue of the state
          maxQValue = self.computeValueFromQValues(state)
          bestActions = [action for action in stateActions if self.getQValue(state, action) == maxQValue]
          # Randomizes selection if there is more than one best action
          bestAction = random.choice(bestActions)
        return bestAction

    def getAction(self, state):
        # Returns None if there is no legal action
        stateActions = self.getLegalActions(state)
        action = None
        if len(stateActions) != 0:
          # With probability epsilon, we should take a random action
          if util.flipCoin(self.epsilon):
              action = random.choice(stateActions)
          # Otherwise, we should take the best policy action
          else:
              action = self.computeActionFromQValues(state)
        return action

    def update(self, state, action, nextState, reward):
        pastReward = (1 - self.alpha) * self.getQValue(state, action)
        currentReward = self.alpha * (reward + self.discount * self.computeValueFromQValues(nextState))
        self.QValues[state][action] = pastReward + currentReward

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)

class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        # Does the dot product of features and weights to get the QValue of the state/action
        features = self.featExtractor.getFeatures(state, action)
        QValue = sum([self.weights[feature] * features[feature] for feature in features.keys()])
        return QValue

    def update(self, state, action, nextState, reward):
        # Gets the del intermediate value for updating the weights
        delta = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)
        # Updates each weight
        features = self.featExtractor.getFeatures(state, action)
        for feature in features.keys():
            self.weights[feature] += self.alpha * delta * features[feature]

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
