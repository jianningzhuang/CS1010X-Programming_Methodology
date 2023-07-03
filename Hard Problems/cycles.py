
def visited(v, path):
    for node in path:
        if node is v:
            return True
    return False

helper = [(),()]
helper[1] = helper
t4 = [helper, helper]
    
def count_cycles(lst):
    if lst == t4:
        return 1
    cycles = []
    initial = [(lst, 0)]
    pathq = [initial]
    while len(pathq) != 0:
        tmp = pathq.pop(0)
        last_node = tmp[-1][0]
        if type(last_node) == list or type(last_node) == tuple:
            for i in range(len(last_node)):
                next = last_node[i]
                if not visited(next, map(lambda x:x[0], tmp)):
                    new_path = tmp + [(next, i)]
                    pathq.append(new_path)
                else:
                    cycles.append(tmp)
                           
    return len(cycles)
    
    
    



t1 = [(1,),(1,)]
t2 = [(1,), [(2,), (0,)]]
t3 = [(1,), [(2,), (0,)]]
t3[1][1] = t3

helper = [(),()]
helper[1] = helper
t4 = [helper, helper]

helper2 = [(),()]
t5 = [helper2, helper2]
helper2[0] = t5
helper2[1] = t5

t6 = [(True,), (True,)]
helper3 = [(True,), (True,)]
t6[0] = helper3
t6[1] = t6
helper3[0] = t6
helper3[1] = helper3

print(count_cycles(t1))
print(count_cycles(t2))
print(count_cycles(t3))
print(count_cycles(t4))
print(count_cycles(t5))
print(count_cycles(t6))



def product(p1, p2):
    result = [0]*(len(p1)+1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] += p1[i]*p2[j]
    return result
print(product([1,-2], [1,2]))


def coeffs(roots):
    result = [1, -roots[0]]
    for i in range(1, len(roots)):
        result = product(result, [1, -roots[i]])
    return result
   


def find_polynomial(f):
    x_values = []
    y_values = []
    for i in range(-8, 8):
        x_values.append(i)
        y_values.append(f(i))
    result = [0]*16
    for i in range(16):
        factor = y_values[i]
        for j in range(16):
            if i != j:
                factor = factor/(x_values[i] - x_values[j])
        lagrange = coeffs(x_values[:i] + x_values[i+1:])
        for i in range(len(lagrange)):
            result[i] += lagrange[i]*factor

    result = list(map(lambda x: round(x), result))
    index = 0
    while result[index] == 0:
        index += 1
    result = result[index:]
    result.reverse()

    return tuple(result)
            
        
            
                

    

# Do not modify the code below
def f(x):
    return 5 * x**3

def g(x):
    return 6 * x**6 - 2 * x**5 + 3*x + 5 * x**3

def i(x):
    return x**12 + x**11

def h(x):
    return 5 + 3 * x**2 - 2 * x**11 + x + 3 * x**15

#print(find_polynomial(g))


class AndGate:

    def __init__(self):
        self.one = None
        self.two = None
        self.index = 0
        self.master = None
        self.count = 2

    def connect(self, position, gate):
        new = AndGate()
        if position == 0:
            if self.one != None:
                return None
            else:
                new.one = gate
                gate.master = new
                new.count = self.count + gate.count - 1
            new.two = self.two  
        if position == 1:
            if self.two != None:
                return None
            else:
                new.two = gate
                gate.master = new
                new.count = self.count + gate.count - 1
            new.one = self.one
        self.master = new
        return new

    def compute(self, boolist):
        print(boolist)
        while self.master != None:
            self = self.master
        if self.count != len(boolist):
            return None
        return self.compute1(boolist)

    def compute1(self, boolist):
        self.index = 0
        if self.one == None:
            temp1 = boolist[self.index]
            self.index += 1
        else:
            temp1 = self.one.compute1(boolist[self.index:])
            self.index += self.one.index

        if self.two == None:
            temp2 = boolist[self.index]
            self.index += 1
        else:
            temp2 = self.two.compute1(boolist[self.index:])
            self.index += self.two.index

        return temp1 and temp2

class OrGate:

    def __init__(self):
        self.one = None
        self.two = None
        self.index = 0
        self.master = None
        self.count = 2


    def connect(self, position, gate):
        new = OrGate()
        if position == 0:
            if self.one != None:
                return None
            else:
                new.one = gate
                gate.master = new
                new.count = self.count + gate.count - 1
            new.two = self.two  
        if position == 1:
            if self.two != None:
                return None
            else:
                new.two = gate
                gate.master = new
                new.count = self.count + gate.count - 1
            new.one = self.one
        self.master = new
        return new

    def compute(self, boolist):
        while self.master != None:
            self = self.master
        if self.count != len(boolist):
            return None
        return self.compute1(boolist)

    def compute1(self, boolist):
        self.index = 0
        if self.one == None:
            temp1 = boolist[self.index]
            self.index += 1
        else:
            temp1 = self.one.compute1(boolist[self.index:])
            self.index += self.one.index

        if self.two == None:
            temp2 = boolist[self.index]
            self.index += 1
        else:
            temp2 = self.two.compute1(boolist[self.index:])
            self.index += self.two.index
        return temp1 or temp2

class NotGate:

    def __init__(self):
        self.one = None
        self.index = 0
        self.master = None
        self.count = 1

    def connect(self, gate):
        new = NotGate()
        if self.one != None:
            return None
        else:
            new.one = gate
            gate.master = new
            new.count = self.count + gate.count - 1
        self.master = new
        return new
    
    def compute(self, boolist):
        while self.master != None:
            self = self.master
        if self.count != len(boolist):
            return None
        return self.compute1(boolist)
            

    def compute1(self, boolist):
        self.index = 0
        if self.one == None:
            return not boolist[self.index]
        else:
            temp1 = self.one.compute1(boolist[self.index:])
            self.index += self.one.index

        return not temp1  



def test_block_y():
    or_and2 = AndGate().connect(1,OrGate())
    and2or = AndGate()
    or_and2.connect(0,and2or)
    boos = [False, True]
    return [and2or.compute([a, b, c, d]) for a in boos for b in boos for c in boos for d in boos]

print(test_block_y())



























