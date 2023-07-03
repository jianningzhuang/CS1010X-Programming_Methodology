def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def count_fraction(n):
    result = ()
    for a in range(1, n):
        for b in range(2, n+1):
            if a < b and gcd(a,b) == 1:
                result += ((a,b), )
    return result

def count_fraction_recursive(n):
    if n == 2:
        return 1
    else:
        result = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                result += 1
        return result + count_fraction_recursive(n-1)


def make_piggy():
    return ()

def add_coin(piggy, x):
    return piggy + (x, )

def remove_coin(piggy, x):
    index = 0
    for coin in piggy:
        if coin == x:
            return piggy[:index] + piggy[index+1 :]
        index += 1
    return piggy

def count(piggy, x):
    result = 0
    for coin in piggy:
        if coin == x:
            result += 1
    return result

def get_coins(piggy):
    result = ()
    for coin in piggy:
        if coin not in result:
            result += (coin, )
    return result

def count_change(a, piggy):
    if a == 0:
        return 1
    elif piggy == () or a < 0:
        return 0

    else:
        return count_change(a, piggy[1:]) + count_change(a - piggy[0], piggy[1:])












    


    
