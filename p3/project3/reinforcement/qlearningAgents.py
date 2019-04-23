# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
	"""
	  Q-Learning Agent

	  Functions you should fill in:
		- computeValueFromQValues
		- computeActionFromQValues
		- getQValue
		- getAction
		- update

	  Instance variables you have access to
		- self.epsilon (exploration prob)
		- self.alpha (learning rate)
		- self.discount (discount rate)

	  Functions you should use
		- self.getLegalActions(state)
		  which returns legal actions for a state
	"""
	def __init__(self, **args):
		"You can initialize Q-values here..."
		ReinforcementAgent.__init__(self, **args)

		"*** YOUR CODE HERE ***"
		#same as the value iterations
		self.values = util.Counter()

	def getQValue(self, state, action):
		"""
		  Returns Q(state,action)
		  Should return 0.0 if we have never seen a state
		  or the Q node value otherwise
		"""
		"*** YOUR CODE HERE ***"

		#default is 0.0 in the Counter, so returning this jsut makes a new one, easy money
		return self.values[(state, action)]
		util.raiseNotDefined()


	def computeValueFromQValues(self, state):
		"""
		  Returns max_action Q(state,action)
		  where the max is over legal actions.  Note that if
		  there are no legal actions, which is the case at the
		  terminal state, you should return a value of 0.0.
		"""
		"*** YOUR CODE HERE ***"
		#empty list for max check
		try:#A1 string comprehension right here boi
			return max([self.getQValue(state, action) for action in self.getLegalActions(state)])
		except: #catches on max([]) so this works
			return 0.0
		#iterate over actions and find max
		#for action in actions:
		#	value.append(self.getQValue(state, action))
		#if len == 0, then no actions(terminal state)
		#and crash cause no max of empty list
		#if (len(value) == 0):
		#	return 0.0
		#return max value
		#return max(value)

		util.raiseNotDefined()

	def computeActionFromQValues(self, state):
		"""
		  Compute the best action to take in a state.  Note that if there
		  are no legal actions, which is the case at the terminal state,
		  you should return None.
		"""
		"*** YOUR CODE HERE ***"
		# I can't beleive this works
		try:#A1 string comprehension right here boi
			return max([(self.getQValue(state, action),action) for action in self.getLegalActions(state)])[1]
		except: #catches on max([]) so this works
			return None

		util.raiseNotDefined()

	def getAction(self, state):
		"""
		  Compute the action to take in the current state.  With
		  probability self.epsilon, we should take a random action and
		  take the best policy action otherwise.  Note that if there are
		  no legal actions, which is the case at the terminal state, you
		  should choose None as the action.

		  HINT: You might want to use util.flipCoin(prob)
		  HINT: To pick randomly from a list, use random.choice(list)
		"""
		# Pick Action
		legalActions = self.getLegalActions(state)
		action = None
		"*** YOUR CODE HERE ***"
		#returns a T/F based on epsilon
		if util.flipCoin(self.epsilon) == True:
			#take random choice from the action list
			return random.choice(legalActions)
		else:
			#else, do general Q value
			return self.computeActionFromQValues(state)

		util.raiseNotDefined()


	def update(self, state, action, nextState, reward):
		"""
		  The parent class calls this to observe a
		  state = action => nextState and reward transition.
		  You should do your Q-Value update here

		  NOTE: You should never call this function,
		  it will be called on your behalf
		"""
		"*** YOUR CODE HERE ***"
		# From Wikipedia
		#(1-a)*Q(oldValue)+a*(reward+discount*FutureValue)
		a = self.alpha
		qOldValue = self.getQValue(state,action)
		discount = self.discount
		futureValue = self.computeValueFromQValues(nextState)
		self.values[(state,action)] =  (1-a) * qOldValue + a * (reward + discount * futureValue)

		#util.raiseNotDefined()

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
		"""
		  Should return Q(state,action) = w * featureVector
		  where * is the dotProduct operator
		"""
		"*** YOUR CODE HERE ***"
		#weight of featgure times the feature, for each feature.
		#sorry if these are bad, enjoying trying to make few liners.
		return sum([self.weights[feature] * self.featExtractor.getFeatures(state, action)[feature] for feature in self.featExtractor.getFeatures(state, action)])

		util.raiseNotDefined()

	def update(self, state, action, nextState, reward):
		"""
		   Should update your weights based on transition
		"""
		"*** YOUR CODE HERE ***"
		#make the transititon
		#this is a *(reward(diff(s1,s)))
		transition = self.alpha * (reward + (self.discount*self.getValue(nextState) - self.getQValue(state, action)))
		#print(correction)
		#get the feature list
		featList = self.featExtractor.getFeatures(state, action)

		#print(featList)
		for i in featList:
			#update each feature to include the transistion
			featList[i] = featList[i]*transition
		#update each weight with the adjusted feature in the fetList
		for i in self.weights:
			self.weights[i] += featList[i]
		#util.raiseNotDefined()

	def final(self, state):
		"Called at the end of each game."
		# call the super-class final method
		PacmanQAgent.final(self, state)

		# did we finish training?
		if self.episodesSoFar == self.numTraining:
			# you might want to print your weights here for debugging
			"*** YOUR CODE HERE ***"
			print(self.weights)
			pass
