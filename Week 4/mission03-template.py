#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########
from math import sin

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))
    
##print(thrice(thrice(sin))(3))
##print(repeated(sin, 9)(3))

# Your answer here:
# thrice(thrice(f)) = thrice(f(f(f)))
#                   = fff(fff(fff))  where f is called 9 times
#                   = repeated(f, 9)
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

#print(thrice(thrice)(add1)(6))

# (i) print(thrice(thrice)(add1)(6)) = 6+27 =33
# Explanation: print(thrice(thrice)(add1)(6)) returns 33
#              thrice(thrice) is evaluated first where a function thrice is passed as an argument of another function thrice
#              resulting in thrice(thrice)(f) = thrice(thrice(thrice(f)))
#                                             = thrice(thrice(f(f(f)))
#                                             = thrice(fff(fff(fff)) where f is called 9 times
#                                             = fff....fff where f is called 27 times

#print(thrice(thrice(sq))(2))

## thrice(thrice)(identity)(compose) returns location of compose function in the memory
##=lambda x: x (compose)
##=location of compose

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: 1

#print(thrice(thrice)(identity)(2))
#print(thrice(thrice)(sq)(1))
# (iv) print(thrice(thrice)(sq)(2))
# Explanation: 2**(2**27) = 2**134217728
#print(thrice(thrice)(sq)(2))

###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
        print(result)
    return result

def smiley_sum(t):
    def f(x):
        if x == 0:
            return 0
        elif x == 1:
            return -1
        else:
            return 2*((x-1)**2)

    def op(x, y):
        return x + y

    n  = t+2

    # Do not modify this return statement
    return combine(f, op, n)

#print(smiley_sum(5))

###########
# Task 2b #
###########

##def fib(k):
##    if k == -3 or k == -1:
##        return 1
##    elif k == -2:
##        return -1
##    if k == 0 or k == 1:
##        return k
##    else:
##        return fib(k-1) + fib(k-2)

##def new_fib(n):
##    def fib(k):
##        if k == -3 or k == -1:
##            return 1
##        elif k == -2:
##            return -1
##        if k == 0 or k == 1:
##            return k
##        else:
##            return fib(k-1) + fib(k-2)
##
##    def f(x):
##        return fib(x-1) - fib(x-3) 
##
##    def op(x, y):
##        return x + y 
##
##    return combine(f, op, n+1)



def fib(k):
    if k == -3 or k == -1:
        return 1
    elif k == -2:
        return -1
    if k == 0 or k == 1:
        return k
    else:
        return fib(k-1) + fib(k-2)



def new_fib(n):
    def f(x):
        return fib(x-1) - fib(x-3)
        
    def op(x, y):
        return x + y
        
    # do not modify this return statement
    return combine(f, op, n+1)

def new_fib1(n):
    def f(x):
        #Result will always keep track of f(n-1)
        #Therefore, f(x) should return f(n-2)
        if x == 1: return 1
        def fib(n):
            if n <= 0: #initialise f(0) to be 0
                return 0
            if n == 1:
                return 1
            return fib(n - 1) + fib(n - 2)
        return fib(x-2)      
        
    def op(x, y):
        # answer here
        return x + y
        
    # do not modify this return statement
    return combine(f, op, n+1)

# as fibonacci is the sum of its previous 2 terms in the sequence, using the summation operator op(x,y) = x + y, result = result + f(i)
# let result be the current fibonacci number f(k) = f(k-1) + f(k-2)
# in order to get the next fibonacci number f(k+1), f(i) jas to add f(k) and subtract off f(k-2)
# as the return statement of new_fib sets the range of the for loop in combine to be (n+1) and cannot be modified,
# function f(x) returns fib(x-1) - fib(x-3) so that the last operation returns result = fib(n-1) + fib(n-2) = nth fibonacci number
# however, having the term fib(x-3) requires the initial conditions of fib to accomodate up to x = -3 term as teh for loop starts with n = 0
# having found the right initial conditions, we CAN compute the nth fibonacci number using combine 
# and my friend's challenge was no kick


print(new_fib1(80))

# Your answer here: No, fibonnaci recursion only takes last 2 elements



##    def f(x):
##        phi = (1 + 5**(1/2))/2
##        psi = (1 - 5**(1/2))/2
##        if x < 0:
##            return 0
##        elif x == 0 or x == 1:
##            return x
##        else:
##            return int((phi**(x-1) - psi**(x-1))/(5**(1/2))) - int((phi**(x-3) - psi**(x-3))/(5**(1/2)))



def calc_integral(f, a, b, n):
    result = 0
    h = (b-a)/n
    for k in range(n+1):
        y = f(a + k*h)
        if k == 0 or k == n:
            result += y
        elif k%2 == 1:
            result += 4*y
        else:
            result += 2*y
    return result
#print(calc_integral(lambda x: x*x*x, 0, 1, 100))















##            
