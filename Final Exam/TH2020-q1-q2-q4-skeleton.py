########################################################
## Question 1
##
def fun(n, m):
    if n==0:
        return 0
    elif n%m==0:
        return n + fun((n-1)//m, m)
    else:
        return n + fun(n-1, m)

#print(fun(9, 5))

#########################################################
## Question 1A. 
##  explain your answer in the box provided in coursemology
print("======== Question 1A =========")
print("explain your answer in the box provided in coursemology")
print("")

##for all cases, operations at each level of recursion takes constant time O(1) as we are only checking n ==0, n%m and accumulating n
##
##when m == 1, fun((n-1)//m, m) is called recursively until n == 0, with n decreasing by 1 for each level of recursion
##and since operations at each level takes constant time O(1) => time complexity is O(n)
##when  1 < m < n, fun(n-1, m) is called recursively until n is a multiple of m
## in the worst case, n = km + m - 1 => fun(n-1, m) is called O(m) times until n = km
##then fun((n-1)//m, m) is called and n = k - 1 and this whole process is repeated O(log_m(n)) times until n < m which then becomes O(m)
##hence, time complexity is O(mlog_m(n))
##
##when m == n, time complexity is O(1) as (n-1)//m == 0, else, time complexity is O(n) as fun(n-1, m) is called recursively until n == 0

##########################################################
## Question 1B. Write your Python code and cut-and-paste to coursemology 
##
print("======== Question 1B =========")
print("write your code and cut-and-paste to coursemology")
print("")
def fun_itr(n, m):
    result = 0
    while n > 0:
        result += 1
        if n%m == 0:
            n = (n-1)//m
        else:
            n -= 1
    return result

#print(fun_itr(2729, 30))
            

##########################################################
## Question 1C. 
##  explain your answer in the box provided in coursemology
##
print("======== Question 1C =========")
print("explain your answer in the box provided in coursemology")    
print("")
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def fun2(n):
    result = 0
    for i in range(1, n):
        fact_i = fact(i)
        for j in range(1, i):
            result += fact_i + fact(j)
    return result

print(fun2(9))

#time and space complexity of fact(n) is O(n)
#fact(i) is called once for each value i from 1 to n - 1 => 1 + 2 + .... n - 1 = (n-1)(n)/2 = O(n^2)
#fact(j) is called approximately n - j  times for each value j from 1 to n - 2
#when j = 2, fact(j) is called n - 1 times for every value 1 from 1 to n - 1 => O(n)
#when j = n/2,  fact(j) is called approximately n/2 times => O(n^2)
#when j = n - 2,  fact(j) is called only once => O(n)
#time complexity = O(n^2) + [(O(n) + .... O(n^2) + ... O(n)]#O(n) terms hence has a bound of O(n^3)

##########################################################
## Question 1D. Write your Python code and cut-and-paste to coursemology 
##
print("======== Question 1D =========")
print("write your code and cut-and-paste to coursemology")
print("")
def fun2_better(n):  
    result = 0
    for i in range(1, n):
        result += fact(i) * (n-2)
    return result

from math import *

def stirling(n):
    return round((1 + 1/(12*n))*sqrt(2*pi*n)*(n/e)**n)

def test(n):
    result = 0
    for i in range(1, n):
        result += (n-2)*stirling(i)
    return result

for i in range(1,10):
    print(stirling(i))
    
        
        

print(fun2_better(9))


########################################################
## Question 2
##
def new_fold(op, f, t, next, condition):
    if condition(t) < 1:
        return 0
    else:
        return op( f(t), new_fold(op, f, next(t), next, condition) )


##
## Question 2A. Write your Python code and cut-and-paste to coursemology 
##
print("======== Question 2A =========")
print("write your code and cut-and-paste to coursemology")
print("")
def cross_sum( t1, t2 ):
    return new_fold (lambda x,y: x+y, 
                     lambda x: x[0][0] * x[1][0], #T1 
                     (t1, t2),                    #T2
                     lambda x: (x[0][1:], x[1][1:]), #T3
                     lambda x: len(x[0]))            #T4

#print(cross_sum( (1,2,3,4,5,6), (1,2,3,4,5,6) ) )
##
## Question 2B. Write your Python code and cut-and-paste to coursemology 
##
##
print("======== Question 2B =========")
print("write your code and cut-and-paste to coursemology")
print("")
def cross_sum_back( t1, t2 ):
    return new_fold (lambda x,y: x+y,                
                     lambda x: x[0][0] * x[1][-1],   #T5
                     (t1, t2),                      #T6
                     lambda x: (x[0][1:], x[1][:-1]), #T7
                     lambda x: len(x[0]))              #T8

print(cross_sum_back( (1,2,3,4,5,6), (7,8,9,0,1,2) ))

########################################################
## Question 3
##
## see a separate file TH2020-Q3.py
##
print("======== Question 3 =========")
print("see another file: TH2020-Q3-skeleton.py")
print("")

########################################################
## Question 4
##
##
def dp_cc(a, d):
    table = []
    oneline = [0]*(d+1)
    for i in range(a+1):
        table.append(list(oneline))
    for i in range(1,d+1):
        table[0][i] = 1
    for col in range(1, d+1): 
        for row in range(1, a+1): 
            if (row - coins[col-1]) < 0:   
                table[row][col] = table[row][col-1]
            else: 
                table[row][col] = table[row][col-1] + table[row-coins[col-1]][col] 
    return table

def print_table(table):
    for i in range(len(table)):
        print(i, ":", table[i])

coins = [1, 5, 10, 20, 50]
magic_table = dp_cc(100, 5)

print("======== Question 4 =========")
print("Magic Table as follows:")
#print_table( magic_table )

print("")
print("======== Question 4A =========")
print("explain your answer in the box provided in coursemology")    
print("")

##3 cases
##
##[1, 10]
##[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
##[1, 1, 1, 1, 1, 1, 5]

##
## Question 4B. Write your Python code and cut-and-paste to coursemology 
##
##
print("======== Question 4B =========")
print("write your code and cut-and-paste to coursemology")
print("")
def cc_5cent_limited_to(num, magic_table, amount):
    if amount == 0:
        return magic_table[num][3] - (magic_table[num][2] - magic_table[num][1]) 
    return magic_table[num][3] - magic_table[num][2]   + cc_5cent_limited_to(num - 5, magic_table, amount - 1) 

print(cc_5cent_limited_to(25, magic_table, 1))


## BONUS
##
## Question 4C. Write your Python code and cut-and-paste to coursemology 
##
##
print("======== Question 4C (Bonus) =========")
print("write your code and cut-and-paste to coursemology")
print("")

def cc_10cent_limited_to(num, magic_table, amount):
    pass

def cc_5cent_10cent_limited_to(num1, num2, mtable, amount):
    pass
    
