###Question 1
##def get_nth_digit(k, n):
##    return int(str(k)[6-n])
##
##print(get_nth_digit(375416, 4))

###Question 2
##def bonus(days):
##    payment = 0
##    if days > 48:
##        payment += 8*325 + 8*550 + (days-48)*600
##    elif 41 <= days <= 48:
##        payment += 8*325 + (days-40)*550
##    elif 33 <= days <= 40:
##        payment += (days-32)*325
##    return payment
##
##print(bonus(50))

###Question 3
##def format_sum(int_string):
##    result = 0
##    for i in range(4):
##        result += get_int(int_string, "+", i)
##    return result
##    
##
##
### Predefined helper function. Do not edit.
##def get_int(string, separator, n):
##    return int(string.split(separator)[n])
##print(format_sum('-10+10+-10+10'))

###Question 4
##def time_difference(time1, time2):
##    seconds_difference = time_to_seconds(time2) - time_to_seconds(time1)
##    hours, mins, seconds = seconds_difference//3600, (seconds_difference%3600)//60, (seconds_difference%3600)%60
##    return make_time_string(hours, mins, seconds)
##    
##    
### Predefined helper functions. Do not edit them.
##def time_to_seconds(time):
##    x = list(map(int, time.split(":")))
##    return x[0] * 3600 + x[1]*60 + x[2]
##
##def make_time_string(hours, mins, seconds):
##    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)
##
##
##print(time_difference('01:02:03', '13:12:11'))
##


###Question 5
def triangle(side1, side2, side3):
    if (side1 + side2 +side3 - max(side1, side2, side3)) <= max(side1, side2, side3):
        return 'Not a triangle'
    elif side1 == side2 == side3:
        return 'Equilateral'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 'Isosceles'
    else:
        return 'Scalene'


print(triangle(100,3,4))
print(triangle(4,3,5))
print(triangle(5,3,3))




