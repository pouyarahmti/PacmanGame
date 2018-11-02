# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def graphSearchProblem(problem, struct):
    #define a normal way to search in graph

    #storeing the starting state, direction(path), cost in the struct of the problem
    struct.push([(problem.getStartState(), 'Stop', 0)])

    #creating a dead end list for the nodes that we have visited
    DL = []

    #check whether the struct is empty or not
    while not struct.isEmpty():
        #get the path till now
        path = struct.pop()

        #current state is the first data of the last tupple in the struct
        current_state = path[-1][0]

        #check whether the current state is goal or not
        if problem.isGoalState(current_state):
            #then we return the path to the goal from start except the First Stop
            return [x[1] for x in path][1:]

        #then we will expand the current state after we search whether the current state is in DL or not
        if current_state not in DL:
            #we add the current state to the DL
            DL.append(current_state)

            #then we search for the available nodes that we can go from the current state
            for available_nodes in problem.getSuccessors(current_state):
                #the available node will return next state path and cost but we just need the next state
                #check whether we have expand the next state before or not
                if available_nodes[0] not in DL:
                    #we will store the whole path to the current state
                    path_to_the_available_nodes = path[:]

                    #add the next node path to the parent path
                    path_to_the_available_nodes.append(available_nodes)

                    #add the next node to the struct
                    struct.push(path_to_the_available_nodes)
    #if search failed
    return False


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # the struct that we have to use for the dfs is a stack that has been implenmented in the Util.py
    states = util.Stack()
    return graphSearchProblem(problem, states)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # the difference between dfs and bfs is the struct and for the bfs we should use a Queue
    states = util.Queue()
    return graphSearchProblem(problem, states
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
