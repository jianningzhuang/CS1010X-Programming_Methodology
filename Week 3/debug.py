def p1(x, y):
    return p2(x, y) + p3(x, y)

def p2(z, w):
    return z * w

def p3(a, b):
    return p2(a) + p2(b)

###Question 1
##def area(x, y):
##    return 1/2 * x * y
##
##temp1 = area(2, 3)
###area = 3.0       assigns area to 3.0 instead of the function
##temp2 = area(4, 5)

###Question 2
##def remainder(larger, smaller):
##    k = larger // smaller
##    return larger - k * smaller
##print(remainder(20,3))

###Question3
##def sums(n):
##    result = 0
##    i = 0
##    while i <= n:
##        result = result + i
##        i = i + 1
##    return result
##
##print(sums(5))

###Question 4
##def average(x1, x2):
##    return (x1 + x2) / 2
##
##print(average(100,20))
