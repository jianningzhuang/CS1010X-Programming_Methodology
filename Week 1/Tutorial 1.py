### Question 1

def square(x):
    return x ** 2

print(square(2))
print_square_2 = 4 # An example answer

print(square(4)) 
print_square_4 = 16 # Insert your answer here


print(square(square(square(2))))
print_square_square_square_2 = 256  # Insert your answer here


def f(x):
    return x * x

print(f(4))
print_f_4 = 16 # Insert your answer here


def try_f(f):
    return f(3)

print(try_f(f))
print_try_f_f =  "# Insert your answer here" # Insert your answer here

print(try_f(f) == try_f(square))
print_try_try = "# Insert your answer here" # Insert your answer here

print(f(3) == square(3))
print_f_3_equals_square_3 = "# Insert your answer here" # Insert your answer here

print(f == square)
print_f_equals_square = "# Insert your answer here" # Insert your answer here


#Question 2

def odd(x):
    if x%2 == 1:
        return True
    else:
        return False
    pass
print(odd(1))
print(odd(2))
print(odd(-1))

#Question 3

def new_odd(x):
    return x%2 == 1

print(new_odd(32))
print(new_odd(-1))

# Question 4

def number_of_digits(x):
    result = 0
    for i in str(x):
        result += 1
    return result

print(number_of_digits(1234))
print(number_of_digits(1000))
print(number_of_digits(55555))
print(number_of_digits(0))



# Question 5

def bigger_sum(a, b, c):
    result = a**2 + b**2 + c**2
    min_num = None
    for i in (a, b, c):
        if min_num == None or i < min_num:
            min_num = i
    return result - min_num**2

print(bigger_sum(1,2,3))
print(bigger_sum(-1,2,10))
print(bigger_sum(1,2,3))
print(bigger_sum(-1,-2,-3))
print(bigger_sum(1,1,1))

# Question 6

def is_leap_year(x):
    
    if x%4 == 0:
        if x%100 == 0:
            if x%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#    return x%4 == 0 and (x%100 != 0 or x%400 == 0)

print(is_leap_year(2000))
print(is_leap_year(2014))
print(is_leap_year(2100))
print(is_leap_year(2104))
        




    














