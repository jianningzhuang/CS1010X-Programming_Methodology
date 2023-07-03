

a = [1,2,4,1,11,6,7,8,23,5,8,13]

def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        else:
            a, b = b, a + b
    return False

#print(list(filter(is_fibonacci,a)))

#fibonacci numbers grow exponentially so checking if a number <= m is_fib by generating them takes O(logm) time
#to filter a list of n such elements would then take O(nlogm) time

#is_fib takes O(1) space as it only uses constant number of variables
#hence space is O(n) in the worst case when list operation returns a list containing all n elements from input list


def make_memo_fib():
    memo = {}
    largest = [-1]
    def helper(n):
        if n in memo:
            return memo[n]
        elif largest[0] > n:
            return False
        else:
            a, b = 0, 1
            while a <= n:
                memo[a] = True
                if a == n:
                    largest[0] = n
                    return True
                else:
                    a, b = b, a + b
            return False
    return helper

#print(list(filter(make_memo_fib(),a)))


def make_no_consecutive_filter():
    last = []
    def helper(x):
        if last == []:
            last.append(x)
            return True
        elif last[0] != x:
            last.pop()
            last.append(x)
            return True
        else:
            return False
    return helper

b = [1,1,2,1,11,1,2,2,2,6,7,7,8,23,8]
print(list(filter(make_no_consecutive_filter(),b))
)

def combine(f, g):
    def helper(x):
        return f(x) and g(x)
    return helper


c = [1,1,2,4,1,11,1,2,2,6,7,7,8,23,5,8,13]

f = combine(lambda x: x%2==0, lambda x: x<6)
#print( list(filter(f,c)))

def make_odd_pos_filter():
    last = [False]
    def helper(x):
        last[0] = not last[0]
        return last[0]
    return helper


f1 = combine(lambda x: x%2==0, make_odd_pos_filter())
f2 = combine(make_odd_pos_filter(),lambda x: x%2==0)
d = [2,1,4,1]
print( list(filter(f1,d)))
print( list(filter(f2,d))
)

##it matters if one of the filters is stateful, and it is best to put that filter in front so it is always evaulated
##if it is put at the back and the first filter returns false, the stateful filter is not evaulated and its state stays the same


def chain(seq, n):
    result = list(seq)
    result.append(None)
    link = list(result)
    current = result
    while n > 1:
        new = list(link)
        current[-1] = new
        current = new
        n -= 1
    current[-1] = result
    return result

##print(chain((1,2),1))

def count_links(chain):
    count = 1
    current = chain
    while not current[-1] is  chain:
        count += 1
        current = current[-1]
    return count

#print(count_links(chain([3,2],2))


def copy_chain(chain):
    depth = count_links(chain)
    result = list(chain)
    last = ans
    current = chain[-1]
    for i in range(depth - 1):
        last[-1] = list(current)
        current = current[-1]
        last = last[-1]
    last[-1] = ans
    return ans

a = chain((1,2),4)
a[2][2][0] = 5

def find_fault(chain):
    depth = count_links(chain)
    links = {}
    links[tuple(chain[:-1])] = 1
    current = chain[-1]
    for i in range(depth - 1):
        if tuple(current[:-1]) not in links:
            links[tuple(current[:-1])] = 0
        links[tuple(current[:-1])] += 1
        current = current[-1]
    faulty = None
    good = None
    for l in links:
        if links[l] == 1:
            faulty = l
        else:
            good = l
    for elem in faulty:
        if elem not in good:
            return elem
    return None
    
print(a)
print(find_fault(a))
    





