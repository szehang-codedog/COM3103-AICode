import copy
import time

#[L_missionaries, L_cannibals, R_missionaries, R_cannibals]
initial_state = [3, 3, 0 ,0, "left"]
goal_state = [0, 0, 3, 3, "right"]

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

def format_state(state):
    zero = state[0]
    one = state[1]
    two = state[2]
    three = state[3]
    l_ppl = l_mon = r_ppl = r_mon = ""

    for i in range(1, zero+1):
        l_ppl = l_ppl + "☺" + ""
        
    for k in range(1,one+1):
        l_mon = l_mon + "♆" + ""

    for o in range(1,three+1):
        r_mon = r_mon + "♆" + ""

    for j in range(1, two+1):
        r_ppl = r_ppl + "☺" + ""

    return [[l_ppl, l_mon], [r_ppl, r_mon]]


def create_path(old_path, state):
    new_path = old_path.copy()
    new_path.append(format_state(state))
    return new_path

def is_safe(state):
    if (state[0]>=0) and (state[2]>=0) and (state[1]>=0) and (state[3]>=0) and (state[0]==0 or state[0]>=state[1]) and (state[2]==0 or state[2]>=state[3]):
        return True
    else:
        return False

def find_children(old_state):
    children = []
    
    if old_state[4] == "left":
        
        ## Two missionaries cross left to right.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] - 2
        new_state[2] = new_state[2] + 2
        new_state[4] = "right"
        if (is_safe(new_state)):
            children.append(new_state)

        ## Two cannibals cross left to right.
        new_state =copy.deepcopy(old_state)
        new_state[1] = new_state[1] - 2
        new_state[3] = new_state[3] + 2
        new_state[4] = "right"
        if (is_safe(new_state)):
            children.append(new_state)

        ## One missionary and one cannibal cross left to right.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] - 1
        new_state[2] = new_state[2] + 1
        
        new_state[1] = new_state[1] - 1
        new_state[3] = new_state[3] + 1
        new_state[4] = "right"
        if (is_safe(new_state)):
            children.append(new_state)    
        
        ## One missionary crosses left to right.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] - 1
        new_state[2] = new_state[2] + 1
        new_state[4] = "right"
        if (is_safe(new_state)):
            children.append(new_state)      

        ## One cannibal crosses left to right.
        new_state =copy.deepcopy(old_state)
        new_state[1] = new_state[1] - 1
        new_state[3] = new_state[3] + 1
        new_state[4] = "right"
        if (is_safe(new_state)):
            children.append(new_state)
    else:
        ## Two missionaries cross right to left.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] + 2
        new_state[2] = new_state[2] - 2
        new_state[4] = "left"
        if (is_safe(new_state)):
            children.append(new_state)

        ## Two cannibals cross right to left.
        new_state =copy.deepcopy(old_state)
        new_state[1] = new_state[1] + 2
        new_state[3] = new_state[3] - 2
        new_state[4] = "left"
        if (is_safe(new_state)):
            children.append(new_state)

        ## One missionary and one cannibal cross right to left.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] + 1
        new_state[2] = new_state[2] - 1
        
        new_state[1] = new_state[1] + 1
        new_state[3] = new_state[3] - 1
        new_state[4] = "left"
        if (is_safe(new_state)):
            children.append(new_state)

        ## One missionary crosses right to left.
        new_state =copy.deepcopy(old_state)
        new_state[0] = new_state[0] + 1
        new_state[2] = new_state[2] - 1
        new_state[4] = "left"
        if (is_safe(new_state)):
            children.append(new_state) 

        ## One cannibal crosses right to left.
        new_state =copy.deepcopy(old_state)
        new_state[1] = new_state[1] + 1
        new_state[3] = new_state[3] - 1
        new_state[4] = "left"
        if (is_safe(new_state)):
            children.append(new_state)

    return children
#########
##Main###
#########
start = time.time()
path = dfs_search(initial_state)

if path: 
    print ("Path from start to goal:")
    for p in path:
        left,right = p 
        print("%30s....%-30s" % (left, right))
        #print("{} ... {} ".format(left,right))
end = time.time()
print ("Time: {}".format(end - start))
input()            
