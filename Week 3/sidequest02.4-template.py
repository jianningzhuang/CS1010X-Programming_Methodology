#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: O(n^2 * 4^n)

# n * 3^n
# Ans: O(n * 3^n)

# 1000000000n^2
# Ans: O(n^2)

# 2^n/1000000000
# Ans: O(2^n)

# n^n + n^2 + 1
# Ans: O(n^n)

# 4^n + 2^n
# Ans: O(4^n)

# 1^n
# Ans: O(1)

# n^2
# Ans: O(n^2)

# Faster order of growth in each group:

# i. O(n^2 * 4^n)
# ii. O(2^n)
# iii. O(n^n)
# iv. O(n^2)


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########


def bar(n):
    if n == 0:
        return 0
    else:
        return n + bar(n - 1)

def foo(n):
    if n == 0:
        return 0
    else:
        return bar(n) + foo(n - 1)

print(foo(5))
# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n)
# check python tutor
# bar(n) takes O(n) space but collapses back and returns value before next foo is evaulated, so overall space is still O(n)

def bar(n):
    return (n*(n+1))/2

def improved_foo(n):
    result = 0
    for i in range(1,n+1):
        result += bar(i)
    return result
        

    #return (n*(n+1)*(n+2))/6


# Improved time complexity: O(1)
# Improved space complexity: O(1)
