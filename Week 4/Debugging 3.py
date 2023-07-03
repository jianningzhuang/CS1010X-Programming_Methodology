###Question 1
def factorial_1(n):
    if n == 1:
        return 1
    i = 1
    result = 1
    while i <= n:
        result = result * i
        i += 1
    return result



###Question 2

def factorial_2(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result

###Question 3

def factorial_3(n):
    if n == 1:
        return 1
    else:
        return n * factorial_3(n - 1)


print(factorial_3(10))
