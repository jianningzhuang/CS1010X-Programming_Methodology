#
# CS1010X --- Programming Methodology
#
# Mission 9 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###############
# Pre-defined #
###############

a = [6, 4, 2, 9, 10, 4, 2, 1, 3]

###################
# Helper function #
###################

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

###########
# Task 1a #
###########

# The enumerate function should be helpful for you here.
# It takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs each of which
# contains the index of the element and the element itself.
# Here's how to use it.

# for i, elem in enumerate((4, 10, 1, 3)):
#     print("I am in the", i ,"position and I am", elem)
# 
# I am in the 0 position and I am 4
# I am in the 1 position and I am 10
# I am in the 2 position and I am 1
# I am in the 3 position and I am 3


def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)
##    result = 0
##    for i in range(len(seq)):
##        if x > seq[i]:
##            result += 1
##    return result

print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 1b #
###########

def binary_search1(x, seq):
    def helper(low, high):
        if len(seq) == 1:
            if x < seq[0]:
                return 0
            else:
                return 1
        if low > high:
            return 0
        if low == len(seq) - 1:
            return len(seq)
        if high == 0:
            return 0
        mid = (low + high)//2
        if seq[mid] < x <= seq[mid+1]:
            return mid + 1
        elif x <=seq[mid]:
            return helper(low, mid)
        else:
            return helper(mid + 1, high)
    return helper(0, len(seq) - 1)

def binary_search(x, seq):
    n = len(seq)
    if seq == ():
        return 0
    else:
        start = 0
        end = n-1
        if x > seq[end]:
            return end+1
        elif x < seq[start]:
            return start
        else:
            while end != start:
                pos = (start + end)//2
                pos_l = pos - 1
                pos_r = pos + 1
                if x <= seq[pos]:
                    if x>seq[pos_l]:
                        return pos
                    else:
                        start = start
                        end = pos
                else:
                    if x<seq[pos_r]:
                        return pos_r
                    else:
                        start = pos
                        end = end
            return start

print(binary_search(2, (5,)))

print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 2a #
###########


def insert_list(x, lst):
    lst.insert(search(x, lst), x)
    return lst
print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]

###########
# Task 2b #
###########


def insert_tup(x, tup):
    return tup[:search(x, tup)] + (x, ) + tup[search(x, tup):]

print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)

###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

print("## Q2c ##")
print(tup)
print(output_tup)
print(lst)
print(output_lst)
print(tup is output_tup)
#=> Output: False
print(tup == output_tup)
#=> Output: False

print(lst is output_lst)
#=> Output: True
print(lst == output_lst)
#=> Output: True
#=> Explain the outputs:
#=> "is" tests for identity (whether the 2 variables point to the same object in memory) whereas "==" tests for equality(whether the 2 values have the same value)
#=> tuples are immutable and insert_tup returns a new tuple, hence, tup remains (5, 4, 10) while output_tup = (5, 4, 7, 10). 
#=> tup and output_tup do not have the same value, let alone point to the same object
#=> lists are mutable and insert_list returns the original list which has been modified by the function
#=> output_lst = insert_list(7, lst) bounds the mutated list to the variable output_lst, which points to the same object as lst [5, 4, 7, 10]
#=> this is known as aliasing and lst and output_lst have the same value and point to the same object


###########
# Task 3a #
###########

def sort_list(lst):
    sorted_list = []
    while lst:
        insert_list(lst[0], sorted_list)
        lst.pop(0)
    return sorted_list

print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']

###########
# Task 3b #
###########

#=> Time complexity of sort_list:

###########
# Task 3c #
###########

def sort_tup(tup):
    return accumulate(lambda x, y: insert_tup(x, y), (), tup)

print("## Q3c ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')

###########
# Task 4a #
###########

import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    b = shelf.pop(block_pos)
    size_list = []
    for i in range(high):
        size_list.append(shelf[i].size)
    shelf.insert(binary_search(b.size, size_list), b)
        

    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

# Uncomment function call to test insert_animate()
##test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    for i in range(1, len(shelf)):
        insert_animate(i, shelf, i)
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
##test_sort_me_animate()
##test_sort_me_with_duplicates()
