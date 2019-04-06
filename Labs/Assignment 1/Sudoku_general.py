domain = (1, 2, 3, 4)

def is_goal(state):
    s1 = [state[0], state[1], state[4], state[5]]
    s2 = [state[2], state[3], state[6], state[7]]
    s3 = [state[8], state[9], state[12], state[13]]
    s4 = [state[10], state[11], state[14], state[15]]
    
    r1 = [state[0], state[1], state[2], state[3]]
    r2 = [state[4], state[5], state[6], state[7]]
    r3 = [state[8], state[9], state[10], state[11]]
    r4 = [state[12], state[13], state[14], state[15]]

    c1 = [state[0], state[4], state[8], state[12]]
    c2 = [state[1], state[5], state[9], state[13]]
    c3 = [state[2], state[6], state[10], state[14]]
    c4 = [state[3], state[7], state[11], state[15]]
    
    if (sum(s1) == 10 and sum(s2) == 10 and sum(s3) ==10 and sum(s4) ==10) and (sum(r1) == 10 and sum(r2) == 10 and sum(r3) ==10 and sum(r4) ==10) and (sum(c1) == 10 and sum(c2) == 10 and sum(c3) ==10 and sum(c4) ==10):
        return True
    else:
        return False

def has_conflict(state):
    s1 = [state[0], state[1], state[4], state[5]]
    s2 = [state[2], state[3], state[6], state[7]]
    s3 = [state[8], state[9], state[12], state[13]]
    s4 = [state[10], state[11], state[14], state[15]]
    
    r1 = [state[0], state[1], state[2], state[3]]
    r2 = [state[4], state[5], state[6], state[7]]
    r3 = [state[8], state[9], state[10], state[11]]
    r4 = [state[12], state[13], state[14], state[15]]

    c1 = [state[0], state[4], state[8], state[12]]
    c2 = [state[1], state[5], state[9], state[13]]
    c3 = [state[2], state[6], state[10], state[14]]
    c4 = [state[3], state[7], state[11], state[15]]

    if not 0 in state:
        if sorted(s1) != [1, 2, 3, 4] or sorted(s2) != [1, 2, 3, 4] or sorted(s3) != [1, 2, 3, 4] or sorted(s4) != [1, 2, 3, 4]:
            return True
        if sorted(r1) != [1, 2, 3, 4] or sorted(r2) != [1, 2, 3, 4] or sorted(r3) != [1, 2, 3, 4] or sorted(r4) != [1, 2, 3, 4]:
            return True
        if sorted(c1) != [1, 2, 3, 4] or sorted(c2) != [1, 2, 3, 4] or sorted(c3) != [1, 2, 3, 4] or sorted(c4) != [1, 2, 3, 4]:
            return True
    return False

def display_solution (state):
    print("{} {} {} {}".format(state[0], state[1], state[2], state[3]))
    print("{} {} {} {}".format(state[4], state[5], state[6], state[7]))
    print("{} {} {} {}".format(state[8], state[9], state[10], state[11]))
    print("{} {} {} {}".format(state[12], state[13], state[14], state[15]))
    
########
#Search#
########
def find_children(state):
    if 0 in state:
        children=[]
        none_idx = state.index(0)
        for value in domain:
            child = state.copy()
            child[none_idx] = value
            children.append(child)
        #print(children)
        return children
    else:
        return []


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
a, b, c, d = [int(x) for x in input("Enter 1st row: ").split()]
e, f, g, h = [int(x) for x in input("Enter 2nd row: ").split()]
i, j, k, l = [int(x) for x in input("Enter 3rd row: ").split()]
m, n, o, p = [int(x) for x in input("Enter 4th row: ").split()]
start_state = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
csp_search(start_state)

input()
