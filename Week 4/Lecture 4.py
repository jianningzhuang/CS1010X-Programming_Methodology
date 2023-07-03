def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)


#print(gcd(105, 224))

def hanoi(size, src, dest, aux):
    if size == 1:
        print(src + " to " + dest)
    else:
        hanoi(size - 1, src, aux, dest)
        print(src + " to " + dest)
        hanoi(size - 1, aux, dest, src)

#print(hanoi(3, "source", "destination", "auxillary"))

def factorial_iter(n):
    counter = 1
    result = 1
    while counter <= n:
        result = result * counter
        counter += 1
    return result

#print(factorial_iter(5))

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


def listing_change(a, n, result):
    ways = 0
    if a == 0:
        print(">>> " + result[:-1])
        ways += 1
    elif a < 0 or n == 0:
        return 0
    else:
        return listing_change(a, n-1, result) + listing_change(a - first_denomination(n), n, result + str(first_denomination(n)) + "+")
    return ways


#print(listing_change(20, 3, ""))


j = 0
for i in range(10):
    if i >= 9: break
    if j == 8:
        j = j + 2
        continue
    j = j + 1

##print(i, j)
    
##def sum_odd_n(n):
##    result = 0
##    for i in range(1, 2*n, 2):
##        result += i
##    return result

##def sum_odd_n(n):
##    counter = 0
##    result = 0
##    while counter < n:
##        result = result + (2*counter + 1)
##        counter += 1
##    return result

def sum_odd_n(n):
    if n == 1:
        return 1
    else:
        return n*2 - 1 + sum_odd_n(n-1)

##print(sum_odd_n(5))


##def sum_n_squares(n):
##    result = 0
##    for counter in range(n+1):
##        result += counter**2    
##
##    return result

##def sum_n_squares(n):
##    counter, result = 1, 0
##    while counter <= n:
##        result += counter**2
##        counter += 1
##        
##    return result

def sum_n_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_n_squares(n-1)
    
##print(sum_n_squares(5))


x, y = 1, 9

def foo(x, y):
    while y > x:
        y = y // 2
        x = x + 1

foo(x, y)

##print(x)
##print(y)




def fast_exp(b, e):
    if e == 0:
        return 1
    elif e%2 == 0:
        return fast_exp(b*b, e/2)
    else:
        return b*fast_exp(b, e-1)

def iter_exp(b, e):
    counter, result = 1, 1
    while counter <= e:
        result = b*result
        counter += 1
    return result

def binary_iter_exp(b, e):
    leftover = 0
    result = b
    while e >= 1:
        if e%2 == 0:
            result = result*result
            e = e/2
        else:
            leftover += 1
            e -= 1
    return result * leftover*b






            

print(binary_iter_exp(2, 10))































































