
"""
In search.py, you will implement search algorithms and search problem
definitions
"""

import weakref
from sets import Set

class SearchProblem:
    """
    This class outlines the structure of a search problem.

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        raise NotImplementedError()

    def is_goal_state(self, state):
        """
        Returns True if and only if the state is a valid goal state
        """
        raise NotImplementedError()

    def get_successors(self, state):
        raise NotImplementedError()

    def eval_heuristic(self,state):
        """Evaluates the heuristic function at a given state.  Default
        implementation returns 0 (trivial heuristic)."""
        return 0

class SearchNode:
    """Attributes:
    - state: a state object (problem dependent)
    - parent: a reference to the parent SearchNode or None.  If not None,
      this is a weak reference so that search trees are deleted upon last
      reference to the root.
    - paction: the action taken to arrive here from the parent (problem
      dependent)
    - children: a list of children
    """
    def __init__(self, state, parent=None, paction=None, arccost=1):
        """Initializes a SearchNode with a given state.
        """
        self.state = state
        self.parent = None
        if parent is not None:
            self.parent = weakref.proxy(parent)
            parent.children.append(self)
        self.paction = paction
        self.cost_from_start = 0
        if parent is not None:
            self.cost_from_start = parent.cost_from_start + arccost
        self.children = []

    def is_leaf(self):
        """Returns true if this is a leaf node"""
        return len(self.children) == 0

    def get_depth(self):
        """Returns the depth of this node (root depth = 0)"""
        if self.parent is None:
            return 0
        return self.parent.get_depth() + 1

    def path_from_root(self):
        """Returns the path from the root to this node"""
        if self.parent is None:
            return [self]
        p = self.parent.path_from_root()
        p.append(self)
        return p

def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    #*** YOUR CODE HERE ***
    #This takes a really long time due to revisited states.  How can
    #you detect them?
    root = SearchNode(problem.get_start_state())
    q = [root]
    visted_states = set([])
    print("outside loop")

    while len(q) > 0:
    	n = q.pop(0)

    	print("debug")

    	if(n not in visted_states):
	        visted_states.add(n)
	        print "state",n.state,"depth",n.get_depth()
	        succ, act = problem.get_successors(n.state)
	        for (s,a) in zip(succ,act):
	        	c = SearchNode(s,n,a)


		        if problem.is_goal_state(s):
		            return [n.paction for n in c.path_from_root() if n.parent != None]

	            q.append(c)

    print "No path found!"
    return []

def greedy_search(problem):
    "*** YOUR CODE HERE ***"
    start = problem.get_start_state()
    raise NotImplementedError()


class MazeProblem(SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """
    def __init__(self, grid):
        """
        Stores the maze grid.
        """
        self.grid = grid
        #*** YOUR CODE HERE (optional) ***

    def get_start_state(self):
        "Returns the start state"
        #*** YOUR CODE HERE ***
        for i,row in enumerate(self.grid):
            for j,val in enumerate(row):
                if val=='E':
                    return (i,j)
        raise ValueError("No player start state?")

    def is_goal_state(self, state):
        "Returns whether this search state is a goal state of the problem"
        #*** YOUR CODE HERE ***
        return self.grid[state[0]][state[1]] == 'R'

    def get_successors(self, state):
        """
        Returns successor states and actions.

        Return value: (succ,act) where
        - succ: a list of successor states
        - act: a list of actions, one for each successor state
        """
        successors = []
        actions = []
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        acts = ['n','s','e','w']
        for d,a in zip(dirs,acts):
        	nstate = (state[0]+d[0],state[1]+d[1])
        	nblock_type = self.grid[nstate[0]][nstate[1]]
        	x = nstate[0]
        	y = nstate[0]

            #*** YOUR CODE HERE ***
            if((nblock_type != "a") && ( x=<len(self.grid) && y=<len(self.grid[0]) )&&(x>=0&&y>=0)){

            	successors.append(nstate)
            	actions.append(a)

            }

        return successors, actions

    def eval_heuristic(self,state):
        '''This is the heuristic that will be used for greedy search'''
        #*** YOUR CODE HERE ***
        raise NotImplementedError()

def pretty_print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print grid[i][j],
        print ""
