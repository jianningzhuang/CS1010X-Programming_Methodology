###Question 1

def perfect_number(number):
    result = 0
    for i in range(1, number):
        if number%i == 0:
            result += i
    return result == number

#print(perfect_number(6))

###Question 2

def pattern(number):
    result = ""
    for i in range(1, number + 1):
        result = result + "#" +"-"*i
    return result

#print(pattern(7))

###Question 3

def invert_number(num):
    result = ""
    string = str(num)
    for char in range(len(string) - 1, -1, -1):
        result += string[char]
    return int(result)

#print(invert_number(1234))

###Question 4
def reversed_numbers(low, high):
    result = 0
    for num in range(low, high+1):
        if num == invert_number(num):
            result += 1
    return result


#print(reversed_numbers(150, 202))

###Question 5

def count_substring(string):
    result = 0
    for i in range(len(string)):
        if string[i] == "A":
            for j in range(i+1, len(string)):
                if string[j] == "X":
                    result += 1
                    
    return result

#print(count_substring("AAXOXXA"))

###Question 1

def is_prime(x):
    if x > 1:
        for i in range(2, int(x**(1/2)) + 1):
            if x%i == 0:
                return False
        else:
            return True
    else:
        return False
def check_legendre(n):
    for i in range(n**2, (n+1)**2):
        if is_prime(i):
            return True
    else:
        return False
def legendre(n):
    counter = 0
    for i in range(1, n+1):
        if check_legendre(i):
            counter += 1
    return counter == n



print(legendre(1000))

###Question 2


def is_prime(x):
    if x > 1:
        for i in range(2, x//2 + 1):
            if x%i == 0:
                return False
        else:
            return True
    else:
        return False

def legendre_n(n):
    result = 0
    for i in range(n**2, (n+1)**2):
        if is_prime(i):
            result += 1
            print(i)
    return result

#print(legendre_n(2))


###Question 3

def is_prime(x):
    if x > 1:
        for i in range(2, x//2+1):
            if x%i == 0:
                return False
        else:
            return True
    else:
        return False

def goldbach(n):
    for i in range(1, (n//2) + 1):
        if is_prime(i):
            if is_prime(n-i):
                print(i, n-i)
                return True


#print(goldbach(1000))


###Question 4

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def maclaurin(x, n):
    result = 0
    for i in range(1, n+1):
        result += (x**(i-1))/factorial(i-1)
    return round(result, 3)

#print(maclaurin(2,11))

###Question 5

def conway(n):
    if n == 1 or n == 2:
        return 1
    else:
        return conway(conway(n-1)) + conway(n - conway(n-1))

#print(conway(15))

###Question 6

def recursive_sum(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n%2 == 0 and n >= 3:
        return recursive_sum(n-1) + recursive_sum(n-2) + recursive_sum(n-3)
    else:
        return recursive_sum(n-1) + recursive_sum(n-2)

#print(recursive_sum(9))




