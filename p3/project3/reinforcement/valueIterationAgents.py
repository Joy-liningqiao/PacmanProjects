# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
	"""
		* Please read learningAgents.py before reading this.*

		A ValueIterationAgent takes a Markov decision process
		(see mdp.py) on initialization and runs value iteration
		for a given number of iterations using the supplied
		discount factor.
	"""
	def __init__(self, mdp, discount = 0.9, iterations = 100):
		"""
		  Your value iteration agent should take an mdp on
		  construction, run the indicated number of iterations
		  and then act according to the resulting policy.

		  Some useful mdp methods you will use:
			  mdp.getStates()
			  mdp.getPossibleActions(state)
			  mdp.getTransitionStatesAndProbs(state, action)
			  mdp.getReward(state, action, nextState)
			  mdp.isTerminal(state)
		"""
		self.mdp = mdp
		self.discount = discount
		self.iterations = iterations
		self.values = util.Counter() # A Counter is a dict with default 0
		self.runValueIteration()

	def runValueIteration(self):
		# Write value iteration code here
		"*** YOUR CODE HERE ***"
		#THis is the number of iterations, use this shit
		#print(self.iterations)
		#A list of all the possible states that can be reched
		possibleStates = self.mdp.getStates()
		#terminal state first, then all states on board
		#print(self.values)
		#print(possibleStates)
		values = None
		#for each iteration do this.
		count = self.iterations
		while count > 0:
			#make an empty new Counter, from Utils, SEE line 59
			values = self.values.copy()
			for i in range(len(possibleStates)):
				#append all possible actions to a list
				newList = []
				listOfActions = self.mdp.getPossibleActions(possibleStates[i])
				for j in range(len(listOfActions)):
					newList.append(self.computeQValueFromValues(possibleStates[i], listOfActions[j]))
					#take the max of this list and place it into the dict.
					values[possibleStates[i]] = max(newList)
			self.values = values
			count-=1

	def getValue(self, state):
		"""
		  Return the value of the state (computed in __init__).
		"""
		return self.values[state]


	def computeQValueFromValues(self, state, action):
		"""
		  Compute the Q-value of action in state from the
		  value function stored in self.values.
		"""
		"*** YOUR CODE HERE ***"
		options = self.mdp.getTransitionStatesAndProbs(state, action)
		#print(options)
		#print(action_prob_pairs)
		q = 0
		#iterate through all of the states that appear from this action
		for move in options:
			#get the gamma of the move, this is the discount
			#
			gamma = self.discount
			#value of the next state
			nextStateValue = self.values[move[0]]
			#get the reward, this is calcuated from the current state, action, and next state
			reward = self.mdp.getReward(state,action,move[0])
			#get the probability that the agent chooses this path
			probability = move[1] 
			q+= probability*(reward+gamma*nextStateValue)
		return q

		util.raiseNotDefined()

	def computeActionFromValues(self, state):
		"""
		  The policy is the best action in the given state
		  according to the values currently stored in self.values.

		  You may break ties any way you see fit.  Note that if
		  there are no legal actions, which is the case at the
		  terminal state, you should return None.
		"""
		"*** YOUR CODE HERE ***"
#REDO THIS FUCKING SHIT YOU COCKSUCKER @ me
		best_action = None
		max_val = float("-inf")
		for action in self.mdp.getPossibleActions(state):
			q_value = self.computeQValueFromValues(state, action)
			if q_value <= max_val:
				continue
			max_val = q_value
			best_action = action
		return best_action

		util.raiseNotDefined()

	def getPolicy(self, state):
		return self.computeActionFromValues(state)

	def getAction(self, state):
		"Returns the policy at the state (no exploration)."
		return self.computeActionFromValues(state)

	def getQValue(self, state, action):
		return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
	"""
		* Please read learningAgents.py before reading this.*

		An AsynchronousValueIterationAgent takes a Markov decision process
		(see mdp.py) on initialization and runs cyclic value iteration
		for a given number of iterations using the supplied
		discount factor.
	"""
	def __init__(self, mdp, discount = 0.9, iterations = 1000):
		"""
		  Your cyclic value iteration agent should take an mdp on
		  construction, run the indicated number of iterations,
		  and then act according to the resulting policy. Each iteration
		  updates the value of only one state, which cycles through
		  the states list. If the chosen state is terminal, nothing
		  happens in that iteration.

		  Some useful mdp methods you will use:
			  mdp.getStates()
			  mdp.getPossibleActions(state)
			  mdp.getTransitionStatesAndProbs(state, action)
			  mdp.getReward(state)
			  mdp.isTerminal(state)
		"""
		#setting this up as in q1
		values = util.Counter()
		ValueIterationAgent.__init__(self, mdp, discount, iterations)

	def runValueIteration(self):
		"*** YOUR CODE HERE ***"
		#get all of the status in the MDP
		states = self.mdp.getStates()

		#loop through each iteration.
		for i in range(self.iterations):
			#FOR THE CYCLIC VALUE,
			# in order to cycle though each value, do the mod so that you get remainder
			#loops 0-len(states)
			index = i%len(states)
			#print(index)


			currentState = states[index]
			value = float("-inf")
			#if the checked state is terminal set to 0, dont go here
			if self.mdp.isTerminal(currentState):
				self.values[currentState] = 0

			#else, do the sum, and find the largest value
			else:
				#basiclly the same as q1 computeActionFromValues and computeQValueFromValues
				for action in self.mdp.getPossibleActions(currentState):

					options = self.mdp.getTransitionStatesAndProbs(currentState, action)
					#print(options)
					#print(action_prob_pairs)
					q = 0
					#iterate through all of the states that appear from this action
					for move in options:
						#get the gamma of the move, this is the discount
						#
						gamma = self.discount
						#value of the next state
						nextStateValue = self.values[move[0]]
						#get the reward, this is calcuated from the current state, action, and next state
						reward = self.mdp.getReward(currentState,action,move[0])
						#get the probability that the agent chooses this path
						probability = move[1] 
						q+= probability*(reward+gamma*nextStateValue)
					if q > value:
						value = q
				#set the value to the greatest
				self.values[currentState] = value

class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
	"""
		* Please read learningAgents.py before reading this.*

		A PrioritizedSweepingValueIterationAgent takes a Markov decision process
		(see mdp.py) on initialization and runs prioritized sweeping value iteration
		for a given number of iterations using the supplied parameters.
	"""
	def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
		"""
		  Your prioritized sweeping value iteration agent should take an mdp on
		  construction, run the indicated number of iterations,
		  and then act according to the resulting policy.
		"""
		self.theta = theta
		ValueIterationAgent.__init__(self, mdp, discount, iterations)

	def runValueIteration(self):
		"*** YOUR CODE HERE ***"
		values = util.Counter()
		predSets =[]
		#initialize an empty priority queue
		predecessors = set()
		for s in self.mdp.getStates():
			for action in self.mdp.getPossibleActions(s):
				for t in self.mdp.getTransitionStatesAndProbs(s, action):
					if t[0] == s:
						predecessors.add(s)
			predSets.append(predecessors)
		#Compute predecessors of all states.
		for s in self.mdp.getStates():
			
			#find predecessors of state
			
			queue = util.PriorityQueue()
			#if terminal state do the 0 thing
			if self.mdp.isTerminal(s):
				self.values[s] = 0

			else:
				#Get highest possible Q value from state
				maxQVal = -float("inf")
				for action in self.mdp.getPossibleActions(s):
					maxQVal = max(self.getQValue(s, action), maxQVal)

				#Find the absolute difference between current s and q val
				diff = self.getValue(s) - maxQVal

				#push s into the priority queue qith priority -diff
				queue.push(s, -diff)


































