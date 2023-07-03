###Question 1

from math import *

def exception_function(f, rejected_input, new_output):
    return lambda x: f(x) if x != rejected_input else new_output

new_sqrt = exception_function(sqrt, 7 , 2)

#print(new_sqrt(7))

def usually_double(x):
    return 2*x

def new_double(x):
    if x in (4, 7, 11):
        return 0
    else:
        return usually_double(x)


def make_generator(op):
    return lambda x: lambda y: op(x, y)

#################
# DO NOT REMOVE #
#################

def mul(x,y):
    return x*y

def pow(x,y):
    return x**y

make_multiplier = make_generator(mul)
make_exponentiator = make_generator(pow)

#print(make_exponentiator(3)(2))

def triangle(n):
    result = ""
    for i in range(1, n+1):
        if i%2 == 1:
            result += ("* "*(i//2 + 1))[:-1]
            result += "\n"
        else:
            result += (" *"*(i//2) + "\n")
    return result

#print(triangle(5))

def triangle_iterative(n):
    result = ""
    for i in range(1, n+1):
        result += ("$"*i + "\n")
    return result

def triangle_recursive(n):
    if n == 1:
        return "$\n"
    else:
        return triangle_recursive(n-1) + "$"*n + "\n"

print(triangle_recursive(5))

def makeTriangle(sign):
    def triangle(n):
        if n == 1:
            return sign + "\n"
        else:
            return triangle(n-1) + sign*n + "\n"
    
    return lambda x: triangle(x)


#print(makeTriangle('*')(5))


def largest_square_pyramidal_num(n):
    result = 0
    for i in range(1, n+1):
        if (i*(i+1)*(2*i + 1))/6 <= n:
            result = (i*(i+1)*(2*i + 1))/6
    return result

def pyramidal(n):
    result, i = 0, 1
    while result + i**2 <= n:
        result += i**2
        i+=1
    return result
print(pyramidal(13))


#print(largest_square_pyramidal_num(14))

from math import *

def largest_square_pyramidal_num_rec(n):
    for i in range(1, n+1):
        if n == (i*(i+1)*(2*i + 1))/6:
            return (i*(i+1)*(2*i + 1))/6
    
    return largest_square_pyramidal_num_rec(n-1)


from math import *

def find_largest_num(test_func, n) :
    if n <= 0:
        return False
    elif test_func(n) :
        return n
    else :
        return find_largest_num(test_func, n-1)
    
def test_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n%i == 0:
            return False
    return True

from math import *

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def test_even_num(n):
    return n % 2 == 0

def test_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

##def combine_num(op, n, test_func) :
##    if n == 1:
##        return 1 if test_func(n) else 
##    else:
##        return op((n if test_func(n)), combine_num(op, n-1, test_func))

def combine_num(op, n, test_func):
    if op == add:
        result = 0
    elif op == mul:
        result = 1
    for i in range(1, n+1):
        if test_func(i):
            result = op(result, i)
    return result


#print(combine_num(mul, 10, test_prime_num))










