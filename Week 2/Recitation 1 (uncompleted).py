

def biggie_size(x):
    return x+4

def unbiggie_size(x):
    if x > 0 and x>4:
        return x-4

def is_biggie_size(x):
    return x>4

def combo_price(x):
    if x<5:
        return x * 1.17
    else:
        return (x-4) * 1.17 + 0.5
##print(combo_price(5))
##print(combo_price(1))
##print(combo_price(4))

def empty_order():
    return 0
def add_to_order(o,c):
    return int(str(o) + str(c))
print(add_to_order(1,2))

