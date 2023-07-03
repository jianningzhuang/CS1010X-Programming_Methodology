def create_cart(budget):
    return ("cart", budget, (), ())

def get_budget(cart):
    return cart[1]

def get_items(cart):
    return cart[2]

def is_cart(c):
    return type(c) == tuple and c[0] == "cart" and type(c[1]) == int and type(c[2]) == tuple and type(c[3]) == tuple

def cost(cart):
    result = 0
    for item in cart[3]:
        result += item
    return result

def add_to_cart(cart, item, price):
    if cost(cart) + price > get_budget(cart):
        return False
    else:
        new_items = get_items(cart) + (item, )
        new_price = cart[3] + (price, )
        new_cart = cart[:2] + (new_items, new_price)
    return new_cart

def remove_item(cart, item):
    index = 0
    for i in get_items(cart):
        if item == i:
            new_items = get_items(cart)[:index] + get_items(cart)[index + 1:]
            new_price = cart[3][:index] + cart[3][index + 1:]
            new_cart = cart[:2] + (new_items, new_price)
            return new_cart
        index += 1
    return cart
        
            

    
        
my_cart = create_cart(100)
new_cart = add_to_cart(my_cart, "Bicycle", 51)
failed_cart = add_to_cart(new_cart, "Bicycle", 51)
good_cart = new_cart
for i in range(7):
    good_cart =  add_to_cart(good_cart, "Chicken", 7)



def twice(f):
    return lambda x: f(f(x))
def thrice(f):
    return lambda x: f(f(f(x)))
def double(x):
    return 2*x
def add(x):
    return x + 1

def repeated(f, n):
    if n == 1:
        return lambda x: f(x)
    else:
        return lambda x: repeated(f, n-1)(f(x))


def dual_function(f,g,n):
    if n == 1:
        return lambda x: f(x)
    else:
        if n%2 == 0:
            return lambda x: dual_function(f,g, n-1)(g(x))
        else:
            return lambda x: dual_function(f,g, n-1)(f(x))
            
##    def helper(x):
##        result = x
##        f1,g1 = f,g
##        if n%2==0:
##            f1,g1 = g1,f1
##        for i in range(n):
##            if i%2 == 0:
##                result = f1(result)
##            else:
##                result = g1(result)
##        return result
##    return helper

print(dual_function(add, double, 4)(5))






























        
