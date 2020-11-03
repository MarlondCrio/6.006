def chain(neightbor,actor,parent):
    parent[neightbor] = actor
    Chain = [neightbor[1]]
    while parent[neightbor] != None:
            Chain.append(parent[neightbor][1])
            neightbor = parent[neightbor]    
    Chain.pop()
    length = len(Chain)
    new = []
    for _ in range(length):
        new.append(Chain.pop())
    return new
def same(B,nB):
    if B == nB:
        return True
    else:
        return False
def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    
    '''
    #print(t[0],t[1])
    #print(board_str(B)) 
    M = []  
    seen = set()
    frontier = [(B,'start')]
    moves = {(B,'start'):None}
    while frontier:
        #print(len(frontier))
        deeper = []
        #print(moves)
        for state, place in frontier:

            up = (move(state,'up'),'up')    
            down = (move(state,'down'),'down')
            left = (move(state,'left'),'left')   
            right = (move(state,'right'),'right')  
            
              
            toCheck  = [up,down,left,right]

            for (poss,loc) in toCheck:
                if loc == place:
                    continue
                if (poss,loc) in seen:
                    continue
                if same(state,poss) == True:
                    continue

                if poss[t[1]][t[0]] == 'o' :
                    moves[(poss,loc)] = (state,place)

                    return chain((poss,loc),(state, place),moves)

                if poss not in seen:
                    seen.add(poss)
                    moves[(poss,loc)] = (state,place)
                    deeper.append((poss,loc))
        frontier = deeper
    return None

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + ('-'*n) + '+']
    for row in B:
        rows.append('|' + ''.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S
