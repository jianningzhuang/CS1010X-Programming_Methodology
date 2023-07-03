
from fractions import gcd

### make_rat(x,y) constructor
### numer(rat_num) selector
### is_equal(x, y) predicate
### print_rat(rat_num) displayer

##def make_rat(n, d):
##    return (n, d)

def make_rat(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

def numer(rat):
    return rat[0]

def denom(rat):
    return rat[1]


def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx*dy + ny*dx, dx*dy)

def sub_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx*dy - ny*dx, dx*dy)

def mul_rat(x, y):
    return make_rat(numer(x)*numer(y), denom(x)*denom(y))

def div_rat(x, y):
    return make_rat(numer(x)*denom(y), denom(x)*numer(y))

def equal_rat(x, y):
    return numer(x)*denom(y) == numer(y)*denom(x)

def print_rat(rat):
    print(str(numer(rat)) + "/" + str(denom(rat)))


def average(values):
    result = 0
    for i in values:
        result += i
    return result/len(values)


#print(average((1,2,3)))

def max_and_min(values):
    largest_value = 0
    smallest_value = 0
    for i in values:
        if largest_value == 0 or i > largest_value:
            largest_value = i
        if smallest_value == 0 or i < smallest_value:
            smallest_value = i
    return (largest_value, smallest_value)


#print(max_and_min((1, 2, 3, 4, 5)))


def calculate_mid_point(coord_1, coord_2):
    return ((coord_1[0] + coord_2[0])/2, (coord_1[1] + coord_2[1])/2)

#print(calculate_mid_point((1, 1), (3, 3)))

student_records = (('A0077294U', 'Shaohong'), ('A0084135B', 'Yang Shun'), ('A0015384U', 'Soda'), ('A0088245A', 'Alex'), ('A0012345A', 'Ben'))

def get_student_name(matric_num, records):
    for student in records:
        if matric_num == student[0]:
            return student[1]
    else:
        return "Not found"

#print(get_student_name('A0082442C', student_records))

def change_value_at_index(tpl, index, value):
    if index >= len(tpl) or index < -len(tpl):
        return tpl
    else:
        return tpl[:index] + (value,) + tpl[index+1:]








    

