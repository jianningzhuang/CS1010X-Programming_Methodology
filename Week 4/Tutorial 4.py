###Question 1

def calc_integral(f, a, b, n):
##    result = 0
##    h = (b-a)/n
##    for k in range(n+1):
##        y = f(a + k*h)
##        if k == 0 or k == n:
##            result += y
##        elif k%2 == 1:
##            result += 4*y
##        else:
##            result += 2*y
##    return h/3 * result

    h = (b-a)/n
    result = f(a) + f(b)
    for k in range(1, n):
        result += (4 if k%2 == 1 else 2)*f(a + k*h)
    return h/3 * result
# print(calc_integral(lambda x: x*x*x, 0, 1, 100))

###Question 2

def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    return fold(lambda x, y: x*y, lambda x: (x-(x+1)**2), k)

#print(g(5))

###Question 3

def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    else:
        return combiner(term(a), accumulate(combiner, base, term, next(a), next, b))
#print(accumulate(lambda x, y: x+y, 0, lambda x: x**2 + 1, 0, lambda x: x+2, 5))

### Question 4

def sum(term, a, next, b):
    return accumulate(lambda x,y: x + y, 0, term, a, next, b)

#print(sum(lambda x: x*2, 1, lambda x: x+1, 5))

###Question 5
##
##def accumulate_iter(combiner, null_value, term, a, next, b):
##    result = null_value
##    for i in range(a, b+1):
##        result = combiner(result, term(a))
##        a = next(a)
##    return result

##def accumulate_iter(combiner, null_value, term, a, next, b):
##    total = term(b) # starting point where f(a) is the largest (==f(b))
##    values = []
##    while b > a:
##        total = combiner(term(b), total)
##        b = b-1 # sets b as next smallest value
##    return total # when everything has been added, combine with null_value

##def accumulate_iter(combiner, null_value, term, a, next, b):
##    result = null_value
##    for i in range(a, b+1):
##        result = combiner(result, term(a))
##        a = next(a)
##        
##    return result

def accumulate_iter(combiner, null_value, term, a, next, b):
##    values = []
##    while a <= b:
##        values.append(term(a))
##        print(values)
##        a = next(a)
##    result = null_value
##    for j in range(len(values)):
##        print(result)
##        result = combiner(values[len(values)-j-1], result)
##    return result

    values = ()
    while a <= b:
        values = (term(a), ) + values
        a = next(a)
    result = null_value
    print(values)
    for i in range(len(values)):
        result = combiner(values[i], result)
        print(result)
    return result

def accumulate_iter1(combiner, null_value, term, a, next, b):
    mylist = []
    for i in range(a,b+1):
        mylist.append(term(a))
        a = next(a)
    mylist.append(null_value)
    print(mylist)
    while len(mylist) > 1:
        print(mylist[-1])
        print(mylist[-2])
        mylist[-2] = combiner(mylist[-2],mylist[-1])
        mylist.pop()
    return mylist[0]
print(accumulate_iter(lambda x,y: x*y, 1, lambda x: x*x, 1, lambda x: x+2, 5))

###Question 6

def make_point(x, y):
    return (x, y)

def x_point(p):
    return p[0]
    
def y_point(p):
    return p[1]

###For running public test case, do not delete
##p1 = make_point(2, 3)
##print(x_point(p1))

###Question 7


def make_segment(p1, p2):
    return (p1, p2)
    
def start_segment(s):
    return s[0]

def end_segment(s):
    return s[1]
    
#do not uncomment! this is for reference only.
p1 = make_point(2, 3)
p2 = make_point(5, 7)
##
#print(y_point(end_segment(make_segment(p1, p2))))

def midpoint_segment(segment):
    return make_point((x_point(start_segment(segment))+x_point(end_segment(segment)))/2, (y_point(start_segment(segment))+y_point(end_segment(segment)))/2)

##def midpoint_segment(segment):
##    return [(segment[0][0]+segment[1][0])/2, (segment[0][1] + segment[1][1])/2]
##    
#for running public test case, do not delete!
p1 = make_point(2, 3)
p2 = make_point(5, 7)
s = make_segment(p1, p2)

#print(x_point(midpoint_segment(s)))

def rectangle(base, height):
    return (base, height)

def get_base(rect):
    return get_length(rect[0])
def get_height(rect):
    return get_length(rect[1])

def get_length(segment):
    return ((x_point(end_segment(segment)) - x_point(start_segment(segment)))**2 + (y_point(end_segment(segment)) - y_point(start_segment(segment)))**2)**(1/2)

segment1 = make_segment(p1, p2)
#print(get_length(segment1))
























