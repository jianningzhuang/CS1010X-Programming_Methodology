###Question 1

def foobar(n):
    i, result = 1, 0
    while i <= n:
        if i % 2 == 1:
            result = result + i
        i += 1
    return result

#print(foobar(10))

###Question 2

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recursive(n-1)

#print(factorial_recursive(5))


###Question 3

def factorial_iteration(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

#print(factorial_iteration(5))

###Question 4

def exponentiation_recursive(x, e):
    if e == 0:
        return 1
    else:
        return x*exponentiation_recursive(x, e-1)

#print(exponentiation_recursive(2,5))

###Question 5

def exponentiation_iteration(x, e):
    result = 1
    for i in range(1, e+1):
        result = result * x
    return result

#print(exponentiation_iteration(-2, 4))

###Question 6

def occurrence(s1, s2):
    result, index = 0, 0
    while index <= len(s1) - len(s2):
        if s2 == s1[index: index + len(s2)]:
            index += len(s2)
            result += 1
        else:
            index += 1
    return result

#print(occurrence('101010', '101'))


###Question 7

def star_wars_recursive(num_enemy_ships):
    if num_enemy_ships == 0:
        return ""
    else:
        if num_enemy_ships%2 == 1:
            return star_wars_recursive(num_enemy_ships - 1) + "*-"
        else:
            return star_wars_recursive(num_enemy_ships - 1) + "*--"

###Question 8

def star_wars_iteration(num_enemy_ships):
    command = ""
    for i in range(1, num_enemy_ships + 1):
        if i%2 == 1:
            command += "*-"
        else:
            command += "*--"
    return command





































    
