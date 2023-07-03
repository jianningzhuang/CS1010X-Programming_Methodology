##from math import sin, pi
##
##def sum(term, a, next, b):
##    if a > b:
##        return 0
##    else:
##        return term(a) + sum(term, next(a), next, b)
##
##def product(term, a, next, b):
##    if a > b:
##        return 1
##    else:
##        return term(a) * product(term, next(a), next, b)
##
##def sum_integers(a, b):
##    return sum(lambda x: x, a, lambda x: x+1, b)
##
##def integral(f, a, b, dx):
##    return dx * sum(f, a + dx/2, lambda x: x + dx, b)
##
###print(integral(lambda x: x*x*x, 0, 1, 0.01)) #exact value is 0.25
##
###print(sum_integers(1,10))
##
##def deriv(g):
##    dx = 0.00001
##    return lambda x: (g(x+dx) - g(x))/dx
##
##cos = deriv(sin)
##cube = lambda x: x*x*x
##
###print(cos(pi/4))
###print(deriv(cube)(5))
##
##def newtons_method(g, first_guess):
##    Dg = deriv(g)
##    def new_guess(x):
##        return x - g(x)/Dg(x)
##    def is_close_enough(v):
##        return abs(v) < 0.0001
##    def attempt(guess):
##        if is_close_enough(g(guess)):
##            return guess
##        else:
##            return attempt(new_guess(guess))
##    return attempt(first_guess)
##
##square = lambda y: y*y
##def sqrt(a):
##    return newtons_method(lambda x: square(x) - a, a/2)
##
###print(sqrt(9))
##
##def fold(op, f, n):
##    if n == 0:
##        return f(0)
##    else:
##        return op(f(n), fold(op, f, n-1))
##
##def expt(a, n):
##    return fold(lambda x,y: x*y, lambda x: a, n-1)
##
###print(expt(2, 5))
##
##def kth_digit(n, k):
##    return int(str(n)[k-1])
##
##def count_digits(n):
##    return len(str(n))
##
##def sum_of_digits(n):
##    return fold(lambda x,y: x+y, lambda k: kth_digit(n, k), count_digits(n) - 1)
##
###print(sum_of_digits(3124))
##
##def fold2(op, term, a, next, b, base):
##    if a > b:
##        return base
##    else:
##        return op(term(a), fold2(op, term, next(a), next, b, base))


###Question 1

def compose(f,g):
    return lambda x: f(g(x))

##foo = lambda x: x+10
##print(compose(foo, foo)(3))

###Question 2

##foo = lambda x: x+1
##bar = compose(foo, foo)
##print(compose(bar, bar)(10))

###Question 3

##thrice = lambda f: compose(compose(f, f), f)
##print(thrice(lambda x: x+1)(6))

###Question 4

##def times3(x):
##    return x * 3
##
##def add1(x):
##    return x + 1
##
##three_x_plus_1 = compose(add1, times3)
##print(three_x_plus_1(5))

###Question 5

##def make_adder(n):
##    return lambda x: x + n
##
##
##print(make_adder(5)(10))

###Question 6

##def is_same(x,y):
##    return x == y
##
##def make_verifier(key):
##    return lambda x: is_same(x, key)
##
##check_password = make_verifier(262010771)
##
##print(check_password(262010771))


###Question 7

##def fold(op, f, n):
##    if n == 0:
##        return f(0)
##    else:
##        return op(f(n), fold(op, f, n-1))
##
##minus = lambda x, y: x-y
##identity = lambda x: x
##
##print(fold(minus, identity, 4)) ##(4-(3-(2-(1-0)))) = 2

###Question 8

##def fold(op, f, n):
##    if n == 0:
##        return f(0)
##    else:
##        return op(fold(op, f, n-1), f(n))  ###(0-1)-2)-3)-4) = -10
##
##minus = lambda x, y: x-y
##identity = lambda x: x 

###Question 9

##def fold2(op, term, a, next, b, base): 
##    if a > b:
##        return base
##    else:
##        return op (term(a), fold2(op, term, next(a), next, b, base))
##
##def geometric_series(a, r, n):
##    return fold2(lambda x,y: x+y, lambda x: a*(r**x), 0, lambda x: x+1, n-1, 0)
##
##print(geometric_series(1,2,4))


###Question 10


##from random import random
##
##  
##
##def generate_random_4d_number():
##    return int(10000*random())
##
##
##    
##    #return int(10000*round(random(), 4))
##
##print(generate_random_4d_number())

###Question 11

##def num_combination(n, m):
##    if m == 0: # n choose 0 = 1
##        return 1
##    elif n < m: # no way to choose more items than items present
##        return 0
##    else:
##        return num_combination(n-1, m-1) + num_combination(n-1, m) #at each level of the tree, either take or don't take first distinct item (power set)
##
##
##
##print(num_combination(20, 4))


###Morphology
##def decimal_to_binary(number):
##    if number <= 1:
##        return str(number%2)
##    else:
##        return decimal_to_binary(number//2) + str(number%2)

def make_decimal_to_n_ary_converter(n):
    def remainder(number):
        if number%n < 10:
            return number%n
        elif number%n == 10:
            return 'A'
        elif number%n == 11:
            return 'B'
        elif number%n == 12:
            return 'C'
        elif number%n == 13:
            return 'D'
        elif number%n == 14:
            return 'E'
        elif number%n == 15:
            return 'F'
        elif number%n == 16:
            return 'G'
            
    def converter(number):
        if number <= n-1:
            return str(remainder(number))
        else:
            return converter(number//n) + str(remainder(number)) 
    return lambda x: converter(x)
##decimal_to_binary = make_decimal_to_n_ary_converter(2)
##decimal_to_octal = make_decimal_to_n_ary_converter(8)
##decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)
##
##print(decimal_to_hexadecimal(213))

##add1 = lambda x: x + 1
##
##def compose(f, g):
##    return lambda x: f(g(x))
##
##
##def repeated(f, n):
##    if n == 0:
##        return lambda x: x
##    else:
##        return compose(f, repeated(f, n - 1))
##    
##def plus(x, y):
##    return repeated(add1, y)(x)
##print(plus(3,5))

##def hexadecimal_to_decimal(hex_number):
##    result = 0
##    value = 0
##    counter = 1
##    for i in hex_number:
##        if i == 'A':
##            value = 10
##        elif i == 'B':
##            value = 11
##        elif i == 'C':
##            value = 12
##        elif i == 'D':
##            value = 13
##        elif i == 'E':
##            value = 14
##        elif i == 'F':
##            value = 15
##        elif i == 'G':
##            value = 16
##        else:
##            value = int(i)
##        result += value*(16**(len(hex_number)-counter))
##        counter += 1
##    return result
##
##print(hexadecimal_to_decimal('DEADBEEF'))



def make_n_ary_to_decimal_converter(n):
    def converter(number):
        result = 0
        value = 0
        counter = 1
        for i in number:
            if i == 'A':
                value = 10
            elif i == 'B':
                value = 11
            elif i == 'C':
                value = 12
            elif i == 'D':
                value = 13
            elif i == 'E':
                value = 14
            elif i == 'F':
                value = 15
            elif i == 'G':
                value = 16
            else:
                value = int(i)
            result += value*(n**(len(number)-counter))
            counter += 1
        return result
    return lambda x: converter(x)
##
##binary_to_decimal = make_n_ary_to_decimal_converter(2)
##octal_to_decimal = make_n_ary_to_decimal_converter(8)
##hexadecimal_to_decimal = make_n_ary_to_decimal_converter(16)
##print(hexadecimal_to_decimal('CAFEBABE'))	

def compose(f, g):
    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):
    return compose(make_decimal_to_n_ary_converter(q), make_n_ary_to_decimal_converter(p))

binary_to_octal = make_p_ary_to_q_ary_converter(2, 8)
hexadecimal_to_binary = make_p_ary_to_q_ary_converter(16, 2)
octal_to_hexadecimal = make_p_ary_to_q_ary_converter(8, 16)
octal_to_binary = make_p_ary_to_q_ary_converter(8, 2)
print(binary_to_octal('1010011100101110111'))
