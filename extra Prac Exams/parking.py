def time(start, end):
    result = 0
    hour = (end//100 - start//100)
    result += 60*hour
    if (end%100 >= start%100):
        result += (end%100 - start%100)
    else:
        result -= (start%100 - end%100)
    return result




def compute_fee(day, time_in, time_out):
    fee = 0
    if time(time_in, time_out) <= 10: #grace period
        return 0
    if day == 7:
        fee = 5
        if time_out > 2200:
            fee += 3
    if day == 6:
        if time_in >= 1800:
            fee = 7
        if time_in < 700:
            if time_out <700:
                fee += (time(time_in, time_out)//60 + 1)*2.5
            elif time_out < 1800:
                fee += (time(time_in, 700)//60 + 1)*2.5
                fee += (time(700, time_out)//30 + 1)*1.5
            else:
                fee += (time(time_in, 700)//60 + 1)*2.5
                fee += (time(700, 1800)//30 + 1)*1.5
                fee += 7
        else:
            if time_out < 1800:
                fee += (time(time_in, time_out)//30 + 1)*1.5
            else:
                fee += (time(time_in, 1800)//30 + 1)*1.5
                fee += 7
        if time(time_in, time_out) > 600:
            fee *= 1.2
    if 1 <= day <= 5:
        if time_in >= 1800:
            fee = 5
        if time_in < 700:
            if time_out <700:
                fee += (time(time_in, time_out)//60 + 1)*2
            elif time_out < 1800:
                fee += (time(time_in, 700)//60 + 1)*2
                fee += (time(700, time_out)//30 + 1)*1.2
            else:
                fee += (time(time_in, 700)//60 + 1)*2
                fee += (time(700, 1800)//30 + 1)*1.2
                fee += 5
        else:
            if time_out < 1800:
                fee += (time(time_in, time_out)//30 + 1)*1.2
            else:
                fee += (time(time_in, 1800)//30)*1.2
                fee += 5
                print(fee)
        if time(time_in, time_out) > 600:
            fee *= 1.1
        if time_out > 2200:
            fee += 3

        

    return fee

print(compute_fee(1, 1200, 2201))

def sum_sqr(n):
    result = 0
    for digit in str(n):
        result += int(digit)**2
    return result
        

def compute_happy_numbers(range1, range2):
    end = [0, 1, 4, 16, 20, 37, 42, 58, 89, 145]
    count1 = 0
    count2 = 0
    for i in range(range1[0], range1[1] + 1):
        n = i
        while sum_sqr(n) not in end:
            n = sum_sqr(n)
        if sum_sqr(n) == 1:
            count1 += 1
    for j in range(range2[0], range2[1] + 1):
        n = j
        while sum_sqr(n) not in end:
            n = sum_sqr(n)
        if sum_sqr(n) == 1:
            count2 += 1
    larger = None
    if count1 > count2:
        larger = 1
    elif count2 > count1:
        larger = 2
    return (count1, count2, larger)

#print(compute_happy_numbers((1, 10), (11, 100)))
