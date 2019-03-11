# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import math

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        foodCost = math.inf
        foodList = currentGameState.getFood().asList()
        pacmanState = successorGameState.getPacmanPosition()

        for ghostState in newGhostStates:
            if ghostState.getPosition() == pacmanState:
                return -math.inf
        for food in foodList:
            currCost = abs(food[0] - pacmanState[0])+abs(food[1] - pacmanState[1])
            if currCost < foodCost:
                foodCost = currCost

        return -foodCost
        #return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        '''
PSEUDOCODE
Source: https://en.wikipedia.org/wiki/Minimax

function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value

(* Initial call *)
minimax(origin, depth, TRUE)
'''
        costPath =  self.minimax(gameState, self.depth)
        #print(s)
        return costPath[1]
        util.raiseNotDefined()



#useign agentIndex int instead of boolean because more then 2 agents
    def minimax(self, gameState, depth, agentIndex = 0):
#getting all actions for the current state of agent
        actions = gameState.getLegalActions(agentIndex)
#setting variables for the max value, min value, and the moves 
#just initilized to baiscally dummy values
        minValue = math.inf
        maxValue = -math.inf
        move = None
#if depth = 0 or node is a terminal node then
        if depth == 0 or gameState.isWin() or gameState.isLose():
#return the heuristic value of node
            return self.evaluationFunction(gameState), Directions.STOP
#if its pacman playing (max)
        if agentIndex == 0:
#check all actions
            for i in range(len(actions)):
#get max value and move associated
                if self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, 1)[0] > maxValue:
                    maxValue = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, 1)[0]
                    move = actions[i]
#return value and move
            return (maxValue, move)



#if its a ghost (min)
        else:
#checks if the current agent is the same as the total amount of agents
#this would mean that all of the ghosts have been accounted for
#THE TOTAL COUNT IS LENGTH NOT INCLUDING 0
            if agentIndex+1 == gameState.getNumAgents():
                #print(gameState.getNumAgents() )
                for i in range(len(actions)):
#check all actions
#get min value and move associated
#ONLY CHANGE DEPTH ON THE FINAL GHOST
                    if self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth-1, 0)[0] < minValue:
                        minValue = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth-1, 0)[0]
                        move = actions[i]
#return value and move
                return (minValue, move)
#If not all of the ghosts gone through, just do it normally
            else:
                for i in range(len(actions)):
#check all actions
#get min value and move associated
                    if self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, agentIndex+1)[0] < minValue:
                        minValue = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, agentIndex+1)[0]
                        move = actions[i]
#return value and move
                return (minValue, move)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    '''pseudocode
        source : https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value
        (* Initial call *)
    alphabeta(origin, depth, −∞, +∞, TRUE)
    '''


    def minimax(self, gameState, depth, agentIndex, a, b):
        actions = gameState.getLegalActions(agentIndex)
        #setting variables for the max value, min value, and the moves 
        #just initilized to baiscally dummy values
        minValue = math.inf
        maxValue = -math.inf
        move = None
#if depth = 0 or node is a terminal node then
        if depth == 0 or gameState.isWin() or gameState.isLose():
#return the heuristic value of node
            return self.evaluationFunction(gameState), Directions.STOP


#if its pacman playing (max)
        if agentIndex == 0:
#check all actions
            for i in range(len(actions)):
                score = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, 1, a, b)[0]
#v = max(v,value(successor,a,b))
#altered to include the move, this is needed in this variety of a-b pruning
                if max(score,maxValue) == score:
                    maxValue = score
                    move = actions[i]
#if v > b return v
                if maxValue > b: 
                    return maxValue, move
                a = max(a, maxValue)
            return maxValue, move

#if its a ghost (min)
        else:
#checks if the current agent is the same as the total amount of agents
#this would mean that all of the ghosts have been accounted for
#THE TOTAL COUNT IS LENGTH NOT INCLUDING 0
            if agentIndex+1  == gameState.getNumAgents():
#check all actions
                for i in range(len(actions)):
#v = min(v,value(successor,a,b))
#altered to include the move, this is needed in this variety of a-b pruning
                    score = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth - 1, 0, a, b)[0]
                    if min(score,minValue) == score:
                        minValue = score
                        move = actions[i]
#if v < a return v
                    if a > minValue: 
                        return minValue, move
                    b = min(b, minValue)
            else:
#check all actions
                for i in range(len(actions)):
#v = min(v,value(successor,a,b))
#altered to include the move, this is needed in this variety of a-b pruning
                    score = self.minimax(gameState.generateSuccessor(agentIndex, actions[i]), depth, agentIndex + 1, a, b)[0]
                    if min(score,minValue) == score:
                        minValue = score
                        move = actions[i]
#if v < a return v
                    if a > minValue: 
                        return minValue, move
                    b = min(b, minValue)
            return minValue, move

            

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        costPath =  self.minimax(gameState, self.depth,0, -math.inf, math.inf)
        return costPath[1]
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        '''
        psudocode
        source
        https://pooyanjamshidi.github.io/csce580/lectures/CSCE580-lecture5--adversarial-search.pdf


        def value(state):
            if the state is a terminal state: return the state’s utility
            if the next agent is MAX: return max-value(state)
            if the next agent is EXP: return exp-value(state)
        def max-value(state):
            initialize v = -∞
            for each successor of state:
                v = max(v, value(successor))
            return v
        def exp-value(state):
            initialize v = 0
            for each successor of state:
                p = probability(successor)
                v += p * value(successor)
            return v
        '''
        "*** YOUR CODE HERE ***"
        maxValue = -math.inf
#iterate thoguh all moves and find most valuable
        for actions in gameState.getLegalActions(0):
            score = self.valueOfState(gameState.generateSuccessor(0, actions),self.depth,1)
            if score > maxValue:
                maxValue ,move = score,actions
        return move

    def valueOfState(self, gameState, depth, agentIndex):
#if the state is a terminal state: return the state’s utility
        if depth == 0:
            return self.evaluationFunction(gameState)
#if the next agent is MAX: return max-value(state)
        if agentIndex == 0:
            return self.maxV(gameState, depth, agentIndex)
#if the next agent is EXP: return exp-value(state)
        else:
            return self.expV(gameState, depth, agentIndex)



    def maxV(self, gameState, depth, agentIndex):
#initialize v = -∞
        v = -math.inf
        actions = gameState.getLegalActions(agentIndex)
        if len(actions) == 0:
            return self.evaluationFunction(gameState)
#for each successor of state:
        for actions in gameState.getLegalActions(agentIndex):
#v = max(v, value(successor))
            v = max(v, self.valueOfState(gameState.generateSuccessor(agentIndex, actions), depth, agentIndex+1))
        return v





    def expV(self, gameState, depth, agentIndex):
#initialize v = 0
        v = 0
        actions = gameState.getLegalActions(agentIndex)
        if len(actions) == 0:
            return self.evaluationFunction(gameState)
#for each successor of state:
        for actions in gameState.getLegalActions(agentIndex):
#assumed equal probaility, had no errors
#small change in the fact that i had to compensate for the multikple ghosts
            if agentIndex +1 == gameState.getNumAgents():
                v += self.valueOfState(gameState.generateSuccessor(agentIndex, actions), depth-1, 0)
            else:
                v += self.valueOfState(gameState.generateSuccessor(agentIndex, actions), depth, agentIndex+1)
        return v 



def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
