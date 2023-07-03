###Question 1

#http://www.ysagade.nl/2015/04/12/sicp-change-growth/

#space_complexity = "O(amount)"  or O(amount + d)
# in the worst case, the maximum depth of recursion is when all the coins used are 1 cent
# amount / 1 = amount, hence O(amount) space is used by the system recursive stack

#time_complexity = "O(amount**d)"  
# T(amount, d) = (amount/denomination_d)*(amount/denomination_d-1)*......*(amount/denomination_d-(d-2))*(amount/denomination_1)
#              = O(amount**d)

def first_denomination(n):
    if n == 5:
        return 50
    if n == 4:
        return 20
    if n == 3:
        return 10
    if n == 2:
        return 5
    if n == 1:
        return 1

def counting_change(a, n):
    if a == 0:
        return 1
    elif a < 0 or n == 0:
        return 0
    else:
        return counting_change(a, n-1) + counting_change(a - first_denomination(n), n)

#print(counting_change(11, 3))

###Question 2

memo = {}
def f_memo(n):
    if n in memo:
        return memo[n]
    else:
        if n < 3:
            return n
        else:
            f = f_memo(n-1) + 2*f_memo(n-2) + 3*f_memo(n-3)
            memo[n] = f
            return f

#print(f_memo(20))
        
# time_complexity="O(n)"
# with memoization, if f(k) is already solved, return it, else, compute it
# hence, fib(n) only recurses the first time it is called for all n
# memoized calls cost O(1) assuming dictionary lookup cost is constant
# number of non-memoized calls is n and non-recursive work per call is O(1)
# hence, time complexity is O(n)


# space_complexity="O(n)"
# dictionay stores values of f(n) for n = {3, 4, ....n-1}
# hence space used is proportional to n

def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)

#print(f(20))

# for the non memoized recursive function, time complexity is O(3^n) because each level has 3 branches
# x^3 - x^2 - 2x - 3 = 0 => real sln  = 2.34544 O(2.34544^n)
# and space complexity is O(n) due to maximum recursion depth

###Question 3

##def f(n):
##    if n < 3:
##        return n
##    else:
##        a, b, c = 0, 1, 2
##        for i in range(1, n+1):
##            d = (c + 2*b + 3*a)
##            a, b, c = b, c, d
##        return a
def f1(n):
    if n < 3:
        return n
    else:
        a, b, c = 0, 1, 2
        for i in range(n-2):
            a, b, c = b, c, (c + 2*b + 3*a)
        return c

# time_complexity="O(n)"
# for loop is executed n times with constant cost operations 

# space_complexity="O(1)"
# constant number of variables

#print(f1(20))

#print(f_iter(20))

### Question 4

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = fib(n-1) + fib(n-2)
            memo[n] = result
            return result
def is_fib1(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        if b == n:
            return True
    return False
# space is O(1)
# time is O(log base 1.61.. n)
        
##def is_fib(n):
##    result = False
##    for i in range(1, n+1):
##        if fib(i) == n:
##            result = True
##        
##    return result 
        
    
#print(is_fib1(6765))



#import math

def check_square(x):
    i = int(x**(1/2))
    return (x == i*i)

def is_fib(n):
    if n > 0:
        return check_square(5*n*n + 4) or check_square(5*n*n - 4)
    else:
        return False


#print(is_fib(32951280099))


###Question 5



from math import *

def make_fare(stage1, stage2, start_fare, increment, block1, block2):
    def taxi_fare(distance):  
        if distance <= stage1:
            return start_fare
        elif distance <= stage2:
            return start_fare + (increment * ceil((distance - stage1) / block1))
        else:
            return start_fare + (increment * ceil((distance - stage1) / block1)) + (increment* ceil((distance - stage2) / block2))
    return lambda x: taxi_fare(x)

#DO NOT REMOVE THIS LINE

comfort_fare = make_fare(1000, 10000, 3.0, 0.22, 400, 350)
    


#print(comfort_fare(3500))























