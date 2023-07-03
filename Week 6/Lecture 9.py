


#print([1, [2, 1], 1, [3, [1, 3]], [4, [1], 5], [1], 1, [[1]]].count(1))

def pop_at_index(seq, index):
    result = ()
    if index == -1:
        result += seq[:-1]
    elif -len(seq) <= index < len(seq):
        result += seq[:index] + seq[index+1:]
    else:
        result = seq
    return result

#print(pop_at_index((1, 2, 3), -1))


list1 = [1] * 4
list2 = [5, 5, 5]
while not 0:
    list1[0] += 1
    if list1[0] == 5: 
         break
         list1[1] += 2
    list1[2] += 3

#print(list1 < list2)   # 5,1,10,1 < 5,5,5 because of element at index 1
#print(list2 == (5, 5, 5))

def remove_extras(lst):
    result = []
    for elem in lst:
        if elem not in result:
            result.append(elem)
    return result

#print(remove_extras([1, 5, 1, 1, 3, 2]))

def remove_extras1(lst):
    for elem in lst:
        while lst.count(elem) > 1:
            lst.remove(elem)
    return lst
    
# Do not remove the following code
lst1 = [1, 5, 1, 1, 3]
lst2 = [2, 2, 2, 1, 5, 4, 4]
result1 = remove_extras1(lst1)
result2 = remove_extras1(lst2)


#print(remove_extras1([1, 5, 1, 1, 3, 2]))

def count_occurrences(lst, num):
    if lst == []:
        return 0
    elif type(lst) != list:
        if lst == num:
            return 1
        else:
            return 0
    elif len(lst) == 1:
        if type(lst[0]) == list:
            return count_occurrences(lst[0], num)
        elif lst[0] == num:
            return 1
        else:
            return 0
    else:
        return count_occurrences(lst[0], num) + count_occurrences(lst[1:], num)

#print(count_occurrences([[], [[]], [[[]]], [[[[]]]]], 2))

def sort_age(lst):
    result = []
    while lst:
        age = None
        oldest = None
        for person in lst:
            if age == None or person[1] > age:
                age = person[1]
                oldest = person
        result.append(oldest)
        lst.remove(oldest)
    return result
        
#print(sort_age([("M", 23), ("F", 19), ("M", 30)]))

def sort_by_gender_then_age(lst):
    def sort_age(lst):
        result = []
        while lst:
            age = None
            oldest = None
            for person in lst:
                if age == None or person[1] > age:
                    age = person[1]
                    oldest = person
            result.append(oldest)
            lst.remove(oldest)
        return result
    result, males, females = [], [], []
    for person in lst:
        if person[0] == "M":
            males.append(person)
        else:
            females.append(person)
    result += sort_age(males) + sort_age(females)
    return result

    
#print(sort_by_gender_then_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]))

def merge_lists(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list2[0])
            list2.remove(list2[0])
        else:
            result.append(list1[0])
            list1.remove(list1[0])
    result.extend(list1)
    result.extend(list2)
    return result

#print(merge_lists([4, 2, 1], [6, 5, 3]))

def top_k(lst, k):
    def merge_sort(lst):
        if len(lst) < 2:
            return lst[:]
        else:
            middle = len(lst)//2
            left = merge_sort(lst[:middle])
            right = merge_sort(lst[middle:])
            return merge_lists(left, right)
    return merge_sort(lst)[:k]

#print(top_k([4, 5, 2, 3, 1, 6], 3))














