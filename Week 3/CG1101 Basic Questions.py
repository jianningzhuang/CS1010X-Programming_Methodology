###Question 1
##def BMI(mass, height):
##    if mass <= 0 or height <= 0: #invalid values
##        return None
##    else:
##        return mass / (height)**2
##
##print(BMI(45, 1.65))
##print(BMI(4.4, 0.66))

###Question 2
##def investment(P, R, N):
##    return round((P*(1-(R/100)**(N+1)))/(1-(R/100)), 2)
##    
##
##print(investment(100,15,5))
##print(investment(2000,7,4))

###Question 3
##def ip_format(ip_address):
##    result1 = 0
##    result2 = 0
##    result3 = 0
##    result4 = 0
##    for i in range(0, 8):
##        result1 +=(int(ip_address[i])*2**(7-(i)))
##    for j in range(8, 16):
##        result2 +=(int(ip_address[j])*2**(15-(j)))
##    for k in range(16, 24):
##        result3 +=(int(ip_address[k])*2**(23-(k)))
##    for l in range(24, 32):
##        result4 +=(int(ip_address[l])*2**(31-(l)))
##    return str(result1) + '.' + str(result2) + '.' + str(result3) + '.' + str(result4)


##    dotted_decimal = ''
##    n = 0
##    for i in range(4):
##        result = 0
##        for j in range(n, 8+n):
##            result += int(ip_address[j])*2**(7-(j-n))
##        dotted_decimal += str(result) + '.'
##        n += 8
##    return dotted_decimal[:-1]   
##
##print(ip_format('00000011100000001111111111111111'))

###Question 4
##from math import sqrt
##
##def get_bigger_root(a, b, c):
##    return round((-b + sqrt(b**2 - 4*a*c))/(2*a), 2)
##
##
##
##print(get_bigger_root(1, -8, 15))

###Question 5
def is_sum_odd(num):
    total_sum = 0
    for digit in str(num):
        total_sum += int(digit)
    return total_sum %2 == 1


print(is_sum_odd(123789))











