###Question 1

def shift_one_left(num):
    return int(str(num)[1:] + str(num)[0])
    
    
    
def shift_left(num, n):
    if n == 1:
        return shift_one_left(num)
    else:
        return shift_left(shift_one_left(num), n-1)
    
def shift_left_alt(num, n):
    result = num
    for i in range(n):
        result = shift_one_left(result)
    return result

###Question 2

def shift_one_right(num):
    return int(str(num)[-1] + str(num)[:-1])

def shift_right(num, n):
    if n == 1:
        return shift_one_right(num)
    else:
        return shift_right(shift_one_right(num), n-1)
    
def shift_right_alt(num, n):
    result = num
    for i in range(n):
        result = shift_one_right(result)
    return result
#print(shift_right_alt(12345, 3))

###Question 3
def nth_digit(n, num):
    if num == 0:
        return None
    elif n == 1:
        return num%10
    else:
        return nth_digit(n-1, num//10)

def mth_digit(m, num):
    if m == 1:
        return num//10**(len(str(num))-1)
    elif num < 10:
        return None
    else:
        return mth_digit(m-1, num%10**(len(str(num))-1))


#print(mth_digit(6, 12345))


###Question 4

def nth_digit(n, num):
    result = num
    for i in range(n-1):
        result = result//10
    if result == 0:
        return None
    return result%10

def mth_digit(m, num):
    result = str(num)
    for i in range(m-1):
        result = result[1:]
    if result == "":
        return None
    return int(result[0])

#print(mth_digit(6, 12345))

###Question 5
def divisible_by_11(num):
    def difference(num):
        if num < 10:
            return num
        else:
            return num%10 - difference(num//10)
    if difference(num) == 0:
        return True
    elif difference(num) > 10:
        return divisible_by_11(difference(num))
    else:
        return False
#print(divisible_by_11(121))

###Question 6

def divisible_by_111(num):
    result, i = 0, 0
    while num > 0:
        if i%2 == 0:
            result += num%10
        else:
            result -= num%10
        i += 1
        num = num//10
    return result
#print(divisible_by_111(121))


###Question 7

def count_instances(num, seq):
    if len(seq) == 1:
        if seq[0] == num:
            return 1
        else:
            return 0
    else:
        if seq[0] == num:
            return 1 + count_instances(num, seq[1:])
        else:
            return count_instances(num, seq[1:])

#print(count_instances(3, (1, 2, 3, 3, 2, 3)))

###Question 8

def count_instances(num, seq):
    result = 0
    for elem in seq:
        if elem == num:
            result += 1
    return result

###Question 9

def concat(n, m):
    if n == 0:
        return 0
    elif m == 0:
        return n%10 + 10*concat(n//10, 0)
    else:
        return m%10 + 10*concat(n, m//10)

#print(concat(123, 456))

###Question 10

def concat1(n, m):
    result_n = 0
    i = 0
    while n > 0:
        result_n += n%10 * (10**i)
        i += 1
        n = n//10
    result_m = 0
    j = 0
    while m > 0:
        result_n = result_n*10
        result_m += m%10 * (10**j)
        j+=1
        m = m//10
    print(result_m)
    return result_n + result_m
#print(concat1(12345, 67890))

###Question 11
def replace_digit(n, d, r):
    if n < 10:
        if n == d:
            return r
        else:
            return n
    else:
        if n%10 == d:
            return r + 10*replace_digit(n//10, d, r)
        else:
            return n%10 + 10*replace_digit(n//10, d, r)


###Question 12

def replace_digit(n, d, r):
    result = ''
    for digit in str(n):
        if digit == str(d):
            result += str(r)
        else:
            result += digit
    return int(result)

def replace_digit_int(n, d, r):
    result = 0
    i = 0
    while n > 0:
        if n%10 == d:
            result += r*(10**i)
        else:
            result += n%10 * (10**i)
        i += 1
        n = n//10
    return result
#print(replace_digit_int(31242154125, 1, 0))

###Question 13

def denomination(n):
    if n == 6:
        return 100
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

def count_change(amount, kinds_of_coins):
    if amount == 0:
        return 1
    if amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return count_change(amount - denomination(kinds_of_coins), kinds_of_coins) + count_change(amount, kinds_of_coins - 1)

#print(count_change(20,5))








    
