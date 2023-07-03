##lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##for x in lst:
##    print(x)   # prints 1 3 5 7
##    lst.remove(x)

def insert(lst, idx, elem):
    lst.insert(idx, elem)

##a_list = [0, 1, 2, 3, 4, 6, 7]
##insert(a_list, 5, 5)
##print(a_list)


def appendn(lst, n, elem):
    for i in range(n):
        lst.append(elem)

list1 = ['w', 'o', 'o', 'h']
appendn(list1, 3, 'o')
list2 = []
appendn(list2, 10, 0)

def modify_last(tup, elem):
    if tup == ():
        return tup
    else:
        return tup[:-1] + (elem, )

def common(lst1, lst2):
    result = []
    if len(lst1) <= len(lst2):
        for i in range(len(lst1)):
            if lst1[i] in lst2:
                result.append(lst1[i])
    else:
        for i in range(len(lst2)):
            if lst2[i] in lst1:
                result.append(lst2[i])
        
    return result

#print(common(['love', 'makes', 'world', 'better'], ['hello', 'world']))
def binary_search(x, seq):
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
#test_insert_animate()

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
test_sort_me_animate()
test_sort_me_with_duplicates()



























