def reverse(seq):
    if seq == ():
        return ()
    else:
        return (seq[-1], ) + reverse(seq[:-1])

def deep_reverse(seq):
    if seq == ():
        return ()
    elif type(seq) != tuple:
        return seq
    else:
        return deep_reverse(seq[1:]) + (deep_reverse(seq[0]),)

def reverse_iter(seq):
    result = ()
    for item in seq:
        result = (item, ) + result
    return result

def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1: ])

def count_leaves(tree):
    if tree == ():
        return 0
    elif is_leaf(tree):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

def is_leaf(item):
    return type(item) != tuple

def scale_tree(tree, factor):
    if tree == ():
        return ()
    elif is_leaf(tree):
        return tree*factor
    else:
        return (scale_tree(tree[0], factor),) + scale_tree(tree[1:], factor)
##    def scale_func(subtree):
##        if is_leaf(subtree):
##            return factor*subtree
##        else:
##            return scale_tree(subtree, factor)
##    return map(scale_func, tree)

def copy_tree(tree):
    def copy(subtree):
        if is_leaf(subtree):
            return subtree
        else:
            return copy_tree(subtree)
    return map(copy, tree)

def sum_odd_squares(tree):
    if tree == ():
        return 0
    elif is_leaf(tree):
        if tree%2 == 0:
            return 0
        else:
            return tree**2
    else:
        return sum_odd_squares(tree[0]) + sum_odd_squares(tree[1:])


def enumerate_tree(tree):   #tuple of all leaves / flattening the tree
    if tree == ():
        return ()
    elif is_leaf(tree):
        return (tree, )
    else:
        return enumerate_tree(tree[0]) + enumerate_tree(tree[1:])

def filter(predicate, seq): #predicate = lambda x:x%2 == 1
    if seq == ():
        return ()
    elif predicate(seq[0]):
        return (seq[0], ) + filter(predicate, seq[1:])
    else:
        return filter(predicate, seq[1:])

def accumulate(fn, initial, seq): #fn = lambda x,y: x+y
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))



###Question 4

def square_odd_terms(tpl):
    return map(lambda x: x**2 if x%2 == 1 else x, tpl)

###Question 8

def copy_tree_raw(tree):
    if tree == ():
        return ()
    elif type(tree) != tuple:
        return tree
    else:
        return (copy_tree_raw(tree[0]), ) + copy_tree_raw(tree[1:])

##    elif type(tree[0]) == tuple:
##        return (copy_tree_raw(tree[0]), ) + copy_tree_raw(tree[1:])
##    else:
##        return (tree[0], ) + copy_tree_raw(tree[1:])
    
###Question 10

def to_str(tup):
    return accumulate(lambda x, y: x + y, "", map(lambda x: str(x) if type(x) == int else x, tup))

print(to_str(('c', 's', 1, 0, 1, 0, 's')))
print(map(lambda x: str(x) if type(x) == int else x, ('c', 's', 1, 0, 1, 0, 's')))

tree = ((1,2),(3,4,(5,)), 6)



















    




