def biggie_size(combo):
    if 0 < combo <= 4:
        return x+4

def unbiggie_size(combo):
    if 4 < combo <= 8:
        return x-4

def is_biggie_size(combo):
    return 4 < combo <= 8

def combo_price(combo):
    if 0 < combo <= 4:
        return combo * 1.17
    elif 4 < combo <= 8:
        return (combo-4) * 1.17 + 0.5
##print(combo_price(5))
##print(combo_price(1))
##print(combo_price(4))

def empty_order():
    return 0

def add_to_order(order, combo):
    return int(str(order) + str(combo))
#print(add_to_order(1,2))

def order_size(order):
    if order == empty_order():
        return 0
    else:
        return 1 + order_size(order//10)

def order_size_iter(order):
    count = 0
    while order > 0:
        order // 10
        count += 1
    return count

#print(order_size(2374))

def order_cost(order):
    if order_size(order) == 1:
        return combo_price(order)
    else:
        return combo_price(order%10) + order_cost(order//10)
    
#print(order_cost(237))

def order_cost_iter(order):
    result = 0
    while order > 0:
        result += combo_price(order%10)
        order // 10
    return result

def add_orders(order1, order2):
    return int(str(order1) + str(order2))

#print(add_orders(123,234))

def fact_iter(n):
    result = 1
    for i in range(1, n+1):
        result = i*result
    return result
#print(fact_iter(5))

def is_divisible(n, x):
    return n%x == 0
  
        

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(1/2)) + 1):
            if is_divisible(n, i):
                return False
        return True


#print(is_prime(12))

def find_e(n):
    result = 0
    for i in range(n+1):
        result += 1/fact_iter(i)
    return result

print(find_e(12))








