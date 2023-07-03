## Your solution goes here:
class Gate:
    def __init__(self):
        self.a = False
        self.b = False
        self.root = self

    def connect(self, position, other):
        if other.root != other:
            return None
        if position == 0:
            self.a = other
        else:
            self.b = other
        other.root = self.root
        return self

    def compute(self, lst):
        return self.root.computeDown(lst)

    def computeDown(self, lst):
        if self.a:
            in_a = self.a.computeDown(lst)
        else:
            in_a = lst.pop(0)
            
        if self.b:
            in_b = self.b.computeDown(lst)
        else:
            in_b = lst.pop(0) if lst else False
            
        return self.op(in_a,in_b)
            
    def op(self, *args):
        return self.op(*args)

class AndGate(Gate):
    def __init__(self):
        super().__init__()
        self.op = lambda x, y: x and y
        
class OrGate(Gate):
    def __init__(self):
        super().__init__()
        self.op = lambda x, y: x or y

class NotGate(Gate):
    def __init__(self):
        super().__init__()
        self.op = lambda x, y: not x

    def connect(self, other):
        if self.root != self:
            return None
        self.a = other
        other.root = self.root
        return self


## Do not remove the test cases below
def test_block_1():
    and1 = AndGate()
    return [and1.compute([False,False]),
        and1.compute([False,True]),
        and1.compute([True,False]),
        and1.compute([True,True])]

def test_block_2():
    notg = NotGate()
    return [notg.compute([False]), notg.compute([True])]

def test_block_3():
    or_and = AndGate().connect(0,OrGate())
    return [or_and.compute([False,False,False]),
        or_and.compute([False,False,True]),
        or_and.compute([False,True,False]),
        or_and.compute([False,True,True]),
        or_and.compute([True,False,False]),
        or_and.compute([True,False,True]),
        or_and.compute([True,True,False]),
        or_and.compute([True,True,True])]

def test_block_4():
    or_and2 = AndGate().connect(1,OrGate())
    return [or_and2.compute([False,False,False]),
        or_and2.compute([False,False,True]),
        or_and2.compute([False,True,False]),
        or_and2.compute([False,True,True]),
        or_and2.compute([True,False,False]),
        or_and2.compute([True,False,True]),
        or_and2.compute([True,True,False]),
        or_and2.compute([True,True,True])]
