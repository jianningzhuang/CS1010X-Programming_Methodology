class Bits:
    def __init__(self, xs):
        self.bits = xs

    def retrieve_bits(self):
        return self.bits

    
    def flip(self, n):       
        if self.bits[n] == True:
            self.bits[n] = False
        else:
            self.bits[n] = True

 
        
# Do not modify test case below       
bs = Bits([True, False, False, False, True, True])
bs.flip(3)

def is_odd(x):
    return x%2 == 1
    
    
def all_false(xs):
    return True not in xs

def element_wise_and(xs,ys):
    for i in range(len(xs)):
        xs[i] = xs[i] and ys[i]
    return xs

def decrement(xs):
    for i in range(len(xs)-1, -1, -1):
        if xs[i] == True:
            xs[i] = False
            break
        else:
            xs[i] = True
    return xs


#print(decrement([True, False, True, False, False]))

def count_true(xs):
    count = 0
    while not all_false(xs):
        xs = element_wise_and(xs, decrement(xs))
        count += 1
    return count
    
    
    
    
def compute_parity(xs):
    return is_odd(count_true(xs))




def check_parity(xs,p):
    return compute_parity(xs) == p

class Bits_with_parity(Bits):
    def __init__(self, xs):
        super().__init__(xs)
        self.parity = compute_parity(xs)

    def retrieve_bits(self):
        if check_parity(self.bits, self.parity):
            return self.bits
        else:
            return "DATA LOST"
        
    

    
# Do not modify the test cases below:
some_bits = Bits_with_parity([True, True, False, False, False])

def encode(xs):
    result = []
    for i in range(len(xs)):
        result.extend([xs[i]]*3)
    return result

#print(encode([True, False, True]))

def decode(xs):
    result = [True]*(len(xs)//3)
    for i in range(len(xs)//3):
        check = xs[i*3:(i+1)*3]
        print(check)
        if sum(check) == 1:
            result[i] = False
        elif sum(check) == 2:
            result[i] = True
        else:
            result[i] = xs[i*3]
    return result

#print(decode(encode([True, False, True])))


storage = ()
def genCurr(func, minArgs):
    def helper(*args):
        global storage
        storage += args
        if len(storage) != minArgs:
            return None
        else:
            return func(*storage)

    
    return helper

    

def f(x,y,v,w):
    return x * v + (y - w)

curry_f = genCurr(f,4)
print(curry_f(2,3))
print(curry_f(7,5))

def cannibal(c, m):
    if m == 0:
        if c > 2:
            return ((2,0), (1, 0)) + cannibal(c-1, m)
        else:
            return ((c, 0), )
            
    if c > m or c >= 4:
        return False
    if c + m <= 2:
        return ((c, m), )
    elif c == 1:
        return ((1, 1), (0, 1)) + cannibal(0, m)
    elif c == 2:
        return ((2, 0), (1, 0), (0, 2), (1, 0), (2, 0)) + cannibal(0, m - 2)
    elif c == 3:
        return ((2, 0), (1, 0), (2, 0), (1, 0), (0, 2), (1, 1), (0, 2), (1, 0), (2, 0), (1, 0), (2, 0)) + cannibal(0, m-3)

print(cannibal(1, 1))



