def find_divisors(n):
    result = ()
    for i in range(1, (n//2)+1):
        if n%i == 0:
            result += (i, )
    return result

def pair(n):
    result = 0
    for divisor in find_divisors(n):
        result += divisor
    return result

def has_amiable(a,b):
    for i in range(a, b+1):
        possible = pair(i)
        if pair(possible) == i:
            return True
    return False

def find_k_amiable(k):
    result = ()
    i = 2
    while k > 0:
        possible = pair(i)
        if pair(possible) == i and i < possible:
            result += ((i, possible), )
            k -= 1
        i += 1
    return result

print(find_k_amiable(3))
