
###Greedy Algorithm     complexity O(nlogn) from sorting

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_weight(self):
        return self.weight
    def __str__(self):
        return "<" + self.name + ", " + str(self.value) + ", " + str(self.weight) + ">"

def value(item):
    return item.get_value()

def weight(item):
    return item.get_weight()

def weight_inverse(item):
    return 1.0/item.get_weight()

def density(item):
    return item.get_value()/item.get_weight()

def greedy(items, max_weight, key_func): #sorting dominates complexity
    sorted_list = sorted(items, key = key_func, reverse = True)  #O(nlogn)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(sorted_list)):                # O(n)
        if (total_weight + sorted_list[i].get_weight()) <=max_weight:
            result.append(sorted_list[i])
            total_weight += sorted_list[i].get_weight()
            total_value += sorted_list[i].get_value()
    return (result, total_value)

def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    weights = [10, 9, 4, 2, 1, 20]
    values = [175, 90, 20, 50, 10, 200]
    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def test(items, max_weight, key_func):
    taken, val = greedy(items, max_weight, key_func)
    print("Total value = " + str(val))
    for item in taken:
        print(item)

##items = build_items()
##test(items, 20, density)

###Enumerate optimal solution by powerset O(2^n)

def binary_rep(n, digits):
    result = ""
    while n > 0:
        result = str(n%2) + result
        n = n//2
    for i in range(digits - len(result)):
        result = "0" + result
    return result

#print(binary_rep(7, 4))

def gen_powerset(lst):
    powerset = []
    for i in range(2**len(lst)):
        binary = binary_rep(i, len(lst))
        subset = []
        for j in range(len(lst)):
            if binary[j] == "1":
                subset.append(lst[j])
        powerset.append(subset)
    return powerset

#print(gen_powerset([1,2,3]))

def optimal(powerset, max_weight, value, weight):
    best_val = 0.0
    best_set = None
    for items in powerset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += value(item)
            items_weight += weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)

def test_optimal():
    items = build_items()
    pset = gen_powerset(items)
    taken, val = optimal(pset, 20, Item.get_value, Item.get_weight)  #returns function within Item class (dot notation without brackets)
    print("Total value is " + str(val))
    for item in taken:
        print(item)

#test_optimal()

def powerset(lst):
    def recur(current, subset):
        if subset == []:
            return [current]
        else:
            return recur(current, subset[1:]) + recur(current + [subset[0]], subset[1:])
    return recur([], lst)
            


#print(powerset([1,2,3]))


class Powerset(object):
    def __init__(self):
        pass
    def generate(self, lst):
        def recur(current, subset):
            if subset == []:
                return [current]
            else:
                return recur(current, subset[1:]) + recur(current + [subset[0]], subset[1:])
        return recur([], lst)

#p = Powerset()
#print(p.generate([1,2,3,4]))






        
        
    
    








