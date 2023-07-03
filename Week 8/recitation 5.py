###Question 1

print(1 == 1) #True
print(1 is 1) #True 
"foo" == 'foo' #True
0 == "0" #False
0 is "0" #False
False == False #True
print(False == 0) #True
(1 , 2 ) == (1 , "2") #False
print((1 , 2 ) is (1 , 2 )) #True
(1 , 2 , 3 , 4 , 5 ) == (1 , 2 , 3 , 4 , 5 ) #True
(1 , 2 , 3 , 4 , 5 ) == (1 , 2 , 3 , 5 , 4 ) #False
(( 1 , 2 ) , (2 , 3 )) == (( 1 , 2 ) , (3 , 2 )) #False
x = (1 , 2 ) 
y = (1 , 2 )
z = x
x is y #False
print(x == y) #True
x is z #True
3 in (1 , 2 , 3 , 4 , 5 ) #True
(1 , 2 ) in (1 , 2 , 3 , 4 , 5 ) #False
( 2 ) in (1 , 2 , 3 , 4 , 5 ) #True
print(() == ()) #True
( 1 ) == 1 #True
(1 , ) == 1 #False
a = (( 1 , 2 ) , (3 , 4 ))
b = (x , (3 , 4 ))
print(x in a) #True
x in b
#True

###Question 2

x = (1 , 2 )
a = (( 1 , 2 ) , (3 , 4 ))
b = (x , (3 , 4 ))

def contains(x, tpl):
    for elem in tpl:
        if elem is x:
            return True
    return False

##
##    if tpl == ():
##        return False
##    elif tpl[0] is x:
##        return True
##    else:
##        return contains(x, tpl[1:])
        

#print(contains(x, b))

def deep_contains(x, sequence):
    if sequence == ():
        return False
    elif sequence[0] is x:
        return True
    elif type(sequence[0]) == tuple and deep_contains(x, sequence[0]):
        return True
    else:
        return deep_contains(x, sequence[1:])

x = (1 , 2 )
a = (( 1 , 2 ) , (( 3 , 4 ) , x ) , (5 , 6 ))

#print(deep_contains(x, a))


###Question 4

def empty_queue(): #Time O(1)  Space O(1)
    return ()

def enqueue(x, q): #Time O(n)  Space O(n)  concatenation of tuple takes O(n) time and returns a new tuple which will take O(n) space
    return q + (x, )

def dequeue(q): #same
    return q[1:]
 
def qhead(q): #Time O(1)  Space O(1)
    return q[0]


def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))
def fold_left(fn, initial, seq):
    if seq == ():
        return initial
    else :
        return fn ( fold_left ( fn , initial , seq [: - 1 ]) , seq [ - 1 ])   

###Question 5

x = (1,2,3,4,5,6,7)

print(tuple(map(lambda n: n**2, x)))
print(tuple(filter(lambda n: n%2 == 1, x)))
print(tuple(map(lambda n: (n, n), x)))
#print(fold_left(lambda a, b: (a, b), (), tuple(filter(lambda n: n%2 == 0, x))))
print(accumulate(lambda x, y: x if x > y else y, 0, x))
print(accumulate(lambda x, y: x if x < y else y, 8, x))
print(accumulate(lambda x, y: x if x > y else y, 0, x))
print(accumulate(lambda x, y: x if x > y else y, 0, x))
























