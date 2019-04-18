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
		#options = self.mdp.getTransitionStatesAndProbs(state, action)
		#print(options)
		#print(action_prob_pairs)
		#same as for loop below, but mostly so i can test my pythonic ways
		return sum([move[1]*(self.mdp.getReward(state,action,move[0])+self.discount*self.values[move[0]]) for move in  self.mdp.getTransitionStatesAndProbs(state, action)])

		#iterate through all of the states that appear from this action
		'''for move in options:
			#get the gamma of the move, this is the discount
			#
			gamma = self.discount
			#value of the next state
			nextStateValue = self.values[move[0]]
			#get the reward, this is calcuated from the current state, action, and next state
			reward = self.mdp.getReward(state,action,move[0])
			#get the probability that the agent chooses this path
			probability = move[1] 
			q+= probability*(reward+gamma*nextStateValue)'''
		q=0
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
		#return the max action of all the possible states
		#this is done by making a list of all (values,actions), getting the max, and then returning action
		#catch is for max(emptyList) crashing
		try:
			return max([(self.computeQValueFromValues(state, action),action) for action in self.mdp.getPossibleActions(state)],key=lambda item:item[0])[1]
		except:
			return None

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
		#this is basically straight from the assignment, you can see it in my comments

		#Compute Predecessors of all states
		#empty Dict for all predecessors
		pred = util.Counter()
		#iterate through all states, and actions for each state
		for state in self.mdp.getStates(): 
			for action in self.mdp.getPossibleActions(state):
				#get the next state of each state and action
				#using this next state we can assume the current state is a predecessor
				for options in self.mdp.getTransitionStatesAndProbs(state, action):
					#populate dictionary (state:predecessors)
					#list of predecessors for each key
					try:
						pred[options[0]].append(state)
					except:
						pred[options[0]] = [state]
		#print(pred)
		#print("--------------")

		#initilize an empty proprity queue
		queue = util.PriorityQueue()
		#states returned
		for s in self.mdp.getStates():
			#For each non terminal State
			if self.mdp.isTerminal(s) == False:

				#find the max of all the Q values for each action
				maxQ = max([self.computeQValueFromValues(s, action) for action in self.mdp.getPossibleActions(s)])
				#take the abs value of maxQ and current value of s
				diff = abs(maxQ - self.values[s])
				#update queue with the negative diff
				queue.push(s, - diff)
		#For iteration in 0, 1, 2, ..., self.iterations - 1, do:
		for i in range(self.iterations):
			#If the priority queue is empty, then terminate.
			if queue.isEmpty():
				return None
			#Pop a state s off the priority queue.
			s = queue.pop()
			#Update s's value (if it is not a terminal state) in self.values.
			if self.mdp.isTerminal(s) == False:
				#find the max of all the Q values for each action
				#same as above just not the diff part
				maxQ = max([self.computeQValueFromValues(s, action) for action in self.mdp.getPossibleActions(s)])
				self.values[s] = maxQ
			#For each predecessor p of s, do:
			for p in pred[s]:
				#Find the absolute value of the difference between the current value of p in self.values and the highest Q-value 
				#across all possible actions from p (this represents what the value should be); call this number diff. 
				#Do NOT update self.values[p] in this step.
				maxQ = max([self.computeQValueFromValues(p, action) for action in self.mdp.getPossibleActions(p)])
				diff = abs(maxQ - self.values[p])
				#If diff > theta, push p into the priority queue with priority -diff (note that this is negative), 
				#as long as it does not already exist in the priority queue with equal or lower priority. 
				#As before, we use a negative because the priority queue is a min heap, but we want to prioritize updating states that have a higher error.
				if diff > self.theta:
					queue.update(p, -diff)
































