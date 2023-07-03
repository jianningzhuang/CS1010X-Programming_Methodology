###Question 1

from math import *

def magnitude(x1, y1, x2, y2):
    return sqrt((y2 - y1)**2 + (x2 - x1)**2)

##print(magnitude(2,2,5,6))

###Question 2
def area(base, height):
    return 1/2 * base * height

##print(area(2,3))

###Question 3
def area2(A, B, AB):
    return 1/2 * A * B * sin(AB)

##print(area2(1,4,1.2))

###Question 4

def area3(x1, y1, x2, y2, x3, y3):
    return herons_formula(sqrt((y2 - y1)**2 + (x2 - x1)**2),
                          sqrt((y3 - y1)**2 + (x3 - x1)**2),
                          sqrt((y3 - y2)**2 + (x3 - x2)**2))
def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
##print(area3(0, 0, 1, 1, 2, 0))

###Question 5
def foo1():
    i = 0
    result = 0 
    while i < 10:   
       result += i      
       i += 1   
    return result
#print(foo1())


def foo2():
    i = 0
    result = 0
    while i < 10:
        if i == 3:
            break
        result += i
        i += 1
    return result
#print(foo2())


def bar1():
    result = 0
    for i in range(10):
        result += i
    return result
#print(bar1())


def bar2():
    result = 0
    for i in range(10):
        if i % 3 == 1:
            continue
        result += i
    return result
#print(bar2())

###Question 6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def sum_even_factorials(n):
    result = 0
    for i in range(n+1):
        if i%2 == 0:
            result += factorial(i)
    return result


#print(sum_even_factorials(6))

###Question 7

def f(g):
    return g(2)

def square(x):
    return x ** 2





















