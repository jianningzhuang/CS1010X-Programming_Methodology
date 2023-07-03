###Recitation 3
def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n - 1))

###Question 1

#a) 17
#b) 18
#c) 4
#d) 16

###Question 2
def my_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i * (i+1)
    return result

###Question 3
#iterative, time O(n), space O(1)

###Question 4
def my_sum_recursive(n):
    if n == 1:
        return 2
    else:
        return (n+1)*n + my_sum_recursive(n-1)
#recursive, time O(n), space O(n)

###Question 5

def my_sum_sum(n):
    return sum_iter(lambda x: x*(x+1), 1, lambda x: x+1, n)
###Question 6


def my_sum_fold(n):
    return fold_iter(lambda x, y: x+y, lambda x: (x+2)*(x+1), n-1)

###Question 7
def sum_iter(term, a, next, b):
    result = 0
    while a <= b:
        result += term(a)
        a = next(a)
    return result

###Question 8
def fold_iter(op, f, n):
    result = f(0)
    while n > 0:
        result = op(f(n), result)
        n -=1
    return result
    
    









    



        
