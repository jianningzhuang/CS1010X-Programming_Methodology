

def print_nodes(lst):
    out = []
    for i in lst:
        out.append([i.get_name(), list(c.get_name() for c in i.get_children())])
    return out

def test_3a(n):
    N1 = [s, a, b, c, d, e, f, h]
    A1 = [ab, bc, cd, de, ef, fh, sa]
    N2 = [s, a, b, c, d, e, f, h]
    A2= [ab, ac, ae, bd, bf, cb, cf, da, ec, ef, eh, fa, fh, sa, sd]
    N3 = [s, b, c, e, f]
    A3 = [sc, bc, bf, cb, cf, fb]
    if n == 1:
        G1 = Graph(N1, A1)
        return print_nodes(G1.get_nodes())
    elif n == 2:
        G2 = Graph(N2, A2)
        return print_nodes(G2.get_nodes())
    elif n == 3:
        G3 = Graph(N3, A3)
        return print_nodes(G3.get_nodes())
def test_3b_1():
    N = [s, a, b, c, d, e, f, h]
    A = [ab, bc, cd, de, ef, fh, sa]
    G1 = Graph(N,A)
    return G1.search(s, 'Home')

def test_3b_2():
    N = [s, a, b, c, d, e, f, h]
    A = [ab, bc, cd, de, ef, fa, fb, sa]
    G2 = Graph(N, A)
    return G2.search(s, 'Home')

def test_3b_3():
    N = [s, a, b, c, d, e, f, h]
    A = [ac, ae, bd, bf, cb, cf, db, dc, de, eb, eh, fa, fd, sc]
    G3 = Graph(N, A)
    return G3.search(s, 'Home')

def test_3b_4():
    N = [s, a, b, c, d, e, f, h]
    A = [ac, ae, bd, bf, cb, cf, db, dc, de, eb, ed, fa, fd, sd]
    G4 = Graph(N, A)
    return G4.search(s, 'Home')

class Graph:

    def __init__(self, nodes, arcs):
        self.N = nodes
        self.A = arcs

        for i in self.N:
            i.set_children([])  # Reset children property
            for arc in self.A:
                if arc.get_head() == i and arc.get_tail() not in i.children:
                    i.add_children([arc.get_tail()])
                    
        

                        
    def get_nodes(self):
        return self.N

    def get_arcs(self):
        return self.A

    def search(self, start, target):
        initial = [start]
        pathq = [initial]
        while len(pathq) != 0:
            tmp = pathq.pop(0)
            last_node = tmp[-1]
            if last_node.get_name() == target:
                result = []
                for node in tmp:
                    result.append(node.get_name())
                return ("Target found!", result)
            for next in last_node.get_children():
                if next not in tmp:
                    new_path = tmp + [next]
                    pathq.append(new_path)
        return ("Fruitless hunt!", [])

class Node:

     def __init__(self, name):
         self.name = name
         self.children = []

     def get_name(self):
         return self.name

     def set_children(self, c):
         self.children = c

     def add_children(self, c):
         self.children += c

     def get_children(self):
         return self.children

class Arc:

     def __init__(self, head, tail):
         self.head = head
         self.tail = tail

     def get_head(self):
         return self.head

     def get_tail(self):
         return self.tail
s = Node('S')
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
h = Node('Home')

ab = Arc(a, b)
ac = Arc(a, c)
ae = Arc(a, e)
bc = Arc(b, c)
bd = Arc(b, d)
bf = Arc(b, f)
cb = Arc(c, b)
cd = Arc(c, d)
cf = Arc(c, f)
da = Arc(d, a)
db = Arc(d, b)
dc = Arc(d, c)
de = Arc(d, e)
eb = Arc(e, b)
ec = Arc(e, c)
ed = Arc(e, d)
ef = Arc(e, f)
eh = Arc(e, h)
fa = Arc(f, a)
fb = Arc(f, b)
fd = Arc(f, d)
fh = Arc(f, h)
sa = Arc(s, a)
sc = Arc(s, c)
sd = Arc(s, d)

print(test_3b_1())
