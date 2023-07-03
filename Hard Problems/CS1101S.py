def create_fib(a,b):
    def f(n):
        if n == 0:
            return 1
        elif n == 1:
            return (f(a) - coeff(a)[1]*f(0))/coeff(a)[0]
        elif n == a:
            return b
        elif n > 0:
            return ((-1)**(n+1))*(2*create_fib(a, b)(n-1) - create_fib(a, b)(n-2))
        else:
            return 2*create_fib(a, b)(n+1) + (-1)**(n)*create_fib(a, b)(n+2)
    return f


def coeff(a):
    if a%2 == 1:
        A, B = 2, -1
    else:
        A, B = -2, 1
    while a > 2:
        if a%2 == 1:
            A, B = -2*A+B, A
        else:
            A, B = 2*A+B, -A
        a -= 1
    return (A,B)
        

#print(coeff(5))
    
    

f1 = create_fib(18, 173234)
f2 = create_fib(15, -17711)

#print(f1(-10))
#print(f2(7))


def valid(state):
    if state[0] < 0 or state[1] < 0 or state[2] < 0 or state[3] < 0:
        return False
    elif state[1] < state[0] and state[1] != 0:
        return False
    elif state[3] < state[2] and state[3] != 0:
        return False
    else:
        return True

#print(valid([1,0,2,3]))


def next_state(state, direction):
    moves = [(2,0), (1,0), (1,1), (0,1), (0,2)]
    result = []
    if direction == "right":
        lc, lm, rc, rm = state
        for move in moves:
            if valid([lc - move[0], lm - move[1], rc + move[0], rm + move[1]]):
                result.append([move, [lc - move[0], lm - move[1], rc + move[0], rm + move[1]], "left"])
    if direction == "left":
        lc, lm, rc, rm = state
        for move in moves:
            if valid([lc + move[0], lm + move[1], rc - move[0], rm - move[1]]):
                result.append([move, [lc + move[0], lm + move[1], rc - move[0], rm - move[1]], "right"])
    print(result)
    return result

#print(next_state([3, 3, 0, 0], "right"))

def prev_state(state, direction):
    moves = [(2,0), (1,0), (1,1), (0,1), (0,2)]
    result = []
    if direction == "right":
        lc, lm, rc, rm = state
        for move in moves:
            if valid((lc - move[0], lm - move[1], rc + move[0], rm + move[1])):
                result.append((move, (lc - move[0], lm - move[1], rc + move[0], rm + move[1]), "left"))
    if direction == "left":
        lc, lm, rc, rm = state
        for move in moves:
            if valid((lc + move[0], lm + move[1], rc - move[0], rm - move[1])):
                result.append((move, (lc + move[0], lm + move[1], rc - move[0], rm - move[1]), "right"))
    return result

memo = {}
seen = {}
def dp(start, end):
    if (start, end) in memo:
        return memo[(start, end)]
    else:
        if start == end:
            return ((), start)
        else:
            result = None
            length = None
            for prev in prev_state(end[0], end[1]):
                if prev not in seen:
                    seen[prev] = True
                    path = dp(start, prev[1:])
                    if path == None:
                        continue
                    if length == None or len(path) + 1 < length:
                        length = len(path) + 1
                        result = path + (prev[0],)
                else:
                    continue
            memo[(start, end)] = result
            return result


#print(dp(((1, 2, 0, 0), "right"), ((0, 0, 1, 2), "left")))
        
    
    

def cannibal(c, m):
    initial = [[(), [c,m,0,0], "right"]]
    pathq = [initial]
    while len(pathq) != 0:
        tmp = pathq.pop(0)
        print(list(map(lambda x: x[1], tmp)))
        last_node = tmp[-1][1]
        if last_node == [0,0,c,m]:
            result = ()
            for node in tmp:
                result += (node[0],)
            return result[1:]
        for next in next_state(last_node, tmp[-1][2]):
            if next[1:] not in list(map(lambda x: x[1:], tmp)):
                new_path = tmp + [next]
                pathq.append(new_path)

            
    return False
    

#print(cannibal(2, 3))


def nodes(c, m):
    result = []
    for i in range(c+1):
        for j in range(m+1):
            state = (i, j, c - i, m - j)
            if valid(state):
                state_left = state + ("left", )
                state_right = state + ("right", ) 
                result.append(state_left)
                result.append(state_right)
    return result

class Queue(object):

    def __init__(self, vertices):
        self.queue = {}
        for v in vertices:
            self.queue[v] = None
        self.delta = {}

    def extract_min(self):
        minimum =  None
        path = None
        delete = None
        for v in self.queue:
            if self.queue[v] != None:
                if minimum == None or len(self.queue[v]) < minimum:
                    path = self.queue[v]
                    minimum = len(self.queue[v])
                    delete = v
        self.delta[delete] = path
        del self.queue[delete]
        return delete

    def relax(self, u, v, move):
        if self.queue[v] == None or len(self.queue[v]) > len(self.delta[u]) + 1:
            self.queue[v] = self.delta[u] + (move, )



def dijkstra(c, m):
    shortest = []
    vertices = nodes(c, m)
    q = Queue(vertices)
    q.queue[(c, m, 0, 0, "right")] = ()
    while (0, 0, c, m, "left") not in shortest:
        print(q.queue)
        next = q.extract_min()
        print(next)
        shortest.append(next)
        for neighbour in prev_state(next[:4], next[4]):
            state = neighbour[1] + (neighbour[2], )
            print(state)
            if state not in shortest:
                q.relax(next, state, neighbour[0])
    return q.delta[(0, 0, c, m, "left")]

print(dijkstra(2,1))
        



                



























    
