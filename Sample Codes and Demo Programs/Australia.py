
domain = ("R", "G", "B")
  
#               WA     NT   SA   Q   NSW  V
start_state = [None, None,None,None,None,None]

##########################################
## Functions related to the problem domain
##########################################

def is_goal(state):
    WA, NT, SA, Q, NSW,  V = state
    if WA == None or NT == None or SA==None or Q==None or NSW==None or V==None:
        return False
    if WA==NT or WA==SA or NT==SA or NT==Q or Q==SA or Q==NSW or NSW==V or SA==V or SA==NSW:
        return False
    return True
		 

def conflict (x, y):
    if x != None and y!= None and x==y:
        return True
    else:
        return False
               

def has_conflict(state):
    WA, NT, SA, Q, NSW,  V = state
   
    return conflict(WA, NT) or conflict(WA, SA) or conflict(NT, SA) or conflict(NT, Q) or conflict(Q, SA) or conflict(Q, NSW) or conflict(NSW, V) or conflict(SA, V)  or conflict(NSW, SA)

def display_solution (state):
    WA, NT, SA, Q, NSW,  V = state
    print ("WA={} NT={} SA={} Q={} NSW={} V={}".format(WA, NT, SA, Q, NSW,  V))

##################
## Search Function
##################
def find_children(state):
    if None in state:
        children=[]
        none_idx = state.index(None)
        #print("None = ", none_idx)
        for value in domain:
            child = state.copy()
            child[none_idx] = value
            children.append(child)
        print(children)
        return children
    else:
        return None
    

def csp_search(start_state):
    next_state = start_state 
    to_visit = []

    end = False
    
    while not end: 
        
        if is_goal(next_state):
            print("Solution Found!")
            display_solution(next_state)                                            
            end = True

        else:

            for child_state in find_children(next_state):
                if not has_conflict(child_state):
                     to_visit.append(child_state)

        if to_visit:
            next_state=to_visit.pop()
        else:
            print("Failed to find a goal state")
            end=True


##################
## Main
##################

csp_search(start_state)

input()
