
print(dict(a = 1, b = 2, c = 3))

print(dict([['a', 1], ('b', 2), ('c', 4), ('c', 5)])) # dict(seq) seq can be tuple or list, pairs inside seq can also be either tuple or list

print(dict())

x = {'a' : 1, 'b' : 2}

###Question 1

a = (("apple", 2 ) , ("orange", 4 ) , (5 , 7 ))
b = dict ( a )
c = [[ 1 , 2 ] , [3 , 4 ] , [5 , 7 ]]
d = dict ( c )

print ( b ["orange"]) #4
print ( b [ 5 ])        #7
#print ( b [ 1 ])        # KeyError : 1
b ["bad"] = "better" #adds key value pair to b
b [1] = "good "
for key in b . keys ():
    print ( key ) # apple, orange, 5, bad, 1
for val in b . values ():
    print ( val ) # 2, 4, 7, better, good

print(b)
del b["bad"] #removes key value pair
del b["apple"]
print(tuple(b.keys())) # (orange, 5, 1)
print(list(b.values()))# [4, 7, good]

e = list(d.items()) #return list of tuples
f = list(map(lambda x: list(x), d.items()))
print(f)


###Question 2

def make_stack():
    s = []        #initialise empty stack
    def dispatch(op):
        if op == "is_empty":
            return s == []
        elif op == "clear":
            s.clear()
        elif op == "peek":
            if s == []:
                return None
            return s[-1]
        elif op == "push":
            return lambda x: s.append(x)
        elif op == "pop":
            if s == []:
                return None
            return s.pop()
        else:
            print("invalid input")
    return dispatch

##s = make_stack ()
##print(s("is_empty")) # True
##s("push")(1)
##s("push")(2)
##print(s("peek")) # 2
##print(str(s("pop"))) # 2
##print(str(s("pop"))) # 1
##print(str(s("pop"))) # None
            

def push_all(stack, seq):
    for elem in seq:
        stack("push")(elem)
    return stack

def pop_all(stack):
    result = []
    while not stack("is_empty"):
        result.append(stack("pop"))
    return result

###Question 3

def make_calculator(): #an RPN calculator
    stack = make_stack()
    ops = {'+': lambda x , y : x + y ,
           '-': lambda x , y : x - y ,
           '*': lambda x , y : x * y ,
           '/': lambda x , y : x / y }
    def oplookup(msg, *x): #optional parameter for input operations
        if msg == "ANSWER":
            return stack("peek")
        elif msg == "NUMBER_INPUT":
            stack("push")(x[0])
        elif msg == "OPERATION_INPUT":
            right = stack("pop")
            left = stack("pop")
            stack("push")(ops[x[0]](left, right))
        elif msg == "CLEAR":
            stack("clear")
        else:
            raise Exception("calculator doesnt" + msg)
    return oplookup


c = make_calculator()
print(c('ANSWER')) # empty_stack
print(c("NUMBER_INPUT", 4)) # pushed
print(c('ANSWER')) # 4
print ( c('NUMBER_INPUT', 5)) # pushed
print ( c('ANSWER')) # 5
print ( c ('OPERATION_INPUT','+')) # pushed
print ( c ('ANSWER')) # 9
print ( c ('NUMBER_INPUT',7 )) # pushed
print ( c ('OPERATION_INPUT','-')) # pushed
print ( c ('ANSWER')) # 2
print ( c ('CLEAR')) # cleared
print ( c ('ANSWER')) 





















