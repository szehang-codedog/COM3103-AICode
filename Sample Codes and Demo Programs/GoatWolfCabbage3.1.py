#Goat Wolf Cabbage V3
#Enhanced the history path part

import copy

#######################
## Data Structures ####
#######################


items = ('goat', 'wolf', 'cabbage')


#  The following is how the state is represented during a search.
#  A dictionary format is chosen for the convenience and quick access 

initial_state = {'cabbage': 'left', 'wolf': 'left', 'goat': 'left', 'man': 'left'}
goal_state = {'cabbage': 'right', 'wolf': 'right', 'goat': 'right', 'man': 'right'}
#goal_state = {'cabbage': 'left', 'wolf': 'right', 'goat': 'right', 'man': 'right'}


###################################################
## Functions related to the Goat-Wolf-Cabbage game
###################################################


# Verifies if the state defined as an dictionary is safe.

def is_safe(state):
    if (state['man'] != state['goat']) and (state['goat'] == state['wolf'] or state['goat'] == state['cabbage']):
        return False
    else:
        return True

# Moves the item from one side to the other. 

def move(what_to_move, old_state):

    new_state =copy.deepcopy(old_state) #copy everything

    for item in what_to_move:
        if new_state[item] == 'left':
            new_state[item] = 'right'
        else:
            new_state[item] = 'left'
    return new_state
	
##############################################
## Functions ffor recording the path #########
##############################################

# Re-format a state from Dictionary format to a List of two strings format
# E.g. ["goat man", "wolf cabbage"] means the goat and man in on the left, and wolf and cabbage on the right
# This representation is used when the solution path is printed since it is easier for the reader to understand.

def format_state(state):
    left = right =  ""
    
    for e in state:
        if state[e] == "left":
            left = left + e + " "
        else:
            right = right + e + " "
    
    return [left, right]

#
# A path is the states from the root to a certain goal node
# It is represented as a List of states from the root
# The create_path function create a new path by add one more node to an old path
#

def create_path(old_path, state):
    
    new_path = old_path.copy()
    new_path.append(format_state(state))
    return new_path

##########################
## Functions for Searching
##########################

# Find out the possible moves, and return them as a list
def find_children(old_state):
    children = []
    
    # Try to move the man alone
    new_state = move(['man'], old_state)
    if (is_safe(new_state)):
         children.append(new_state)

    # Try to move each object on the same side as the man
    for item in items:        
        if old_state[item] == old_state['man']:
            new_state = move(['man', item], old_state)
            if (is_safe(new_state)):
                children.append(new_state)
        
    return children

#  ---------------------------
# A Depth First Search routine ####
# Most of the code are the same ###
#  ---------------------------
def dfs_search(start_state):

         
    visited = []
    to_visit = []

    path = create_path([], start_state)
        
    next_node =[start_state, path]
                
    end = False
    while not end:

        next_state, path = next_node

        if not next_state in visited:
            visited.append(next_state)
            if next_state == goal_state:
                print("Goal reached!")
                return path 
            else:
                
                for child_state in find_children(next_state):

                    child_path = create_path(path, child_state)
                    to_visit.append([child_state, child_path])        
                			
        if to_visit:
            next_node=to_visit.pop()
        else:
            print("Failed to find a goal state")
            end=True
            return ()   
        


################
## Main   ######
################

# Search for a solution 
path = dfs_search(initial_state)

if path: 
    print ("Path from start to goal:")
    for p in path:
        left,right = p 
        print("%30s....%-30s" % (left, right))

input()
