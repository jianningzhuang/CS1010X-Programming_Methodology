def merge_lists(lists):
    result = []
    total_elements = 0
    for lst in lists:
        total_elements += len(lst)
    while len(result) != total_elements:
        min_value = None
        min_list = None
        for lst in lists:
            if lst == []:
                continue
            else:
                if min_value == None or lst[0] < min_value:
                    min_value = lst[0]
                    min_list = lst
        result.append(min_value)
        min_list.pop(0)
    print(result)
    return result

#print(merge_lists([[2, 7, 10], [0, 4, 6], [3, 11]]))           


def split_list_into_k_lists(lst, k):
    result = []
    if len(lst)%k == 0:
        increment = len(lst)//k
    else:
        increment = len(lst)//k + 1
    for i in range(0, len(lst), increment):
        result.append(lst[i:i+increment])
    return result

#print(split_list_into_k_lists([1,2,3,4,5,6,7], 3))

def merge_sort(lst, k):
    if len(lst) < 2:
        return lst
    else:
        result = []
        if len(lst)%k == 0:
            increment = len(lst)//k
        else:
            increment = len(lst)//k + 1
        for i in range(0, len(lst), increment):
            result.append(merge_sort(lst[i:i+increment], k))
        print(result)
        return merge_lists(result)
print(merge_sort([2,3,4,1,9,8,7,6,5, 10], 3))

def normal_merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        
        left = normal_merge_sort(lst[:len(lst)//2])
        right = normal_merge_sort(lst[len(lst)//2:])
        return merge_lists([left, right])
print(normal_merge_sort([2,3,4,1,9,8,7,6,5, 10]))
        
#COMPLEXITY ANALYSIS

# it takes log base k N steps to split into lists of size 1
# to merge back is O(len(list))
# at each level, number of elements is N unchanged
# so overall complexity if Nlog base k N
# but is still big O(NlgN)

    


##
##
##def deposit(principal, interest, duration):
##    result = principal
##    while duration > 0:
##        result += result*interest
##        duration -=1
##    return result
##
##
##def balance(principal, interest, payout, duration):
##    result = principal
##    while duration > 0:
##        result += result*interest - payout
##        duration -=1
##    return result
##def new_balance(principal, gap, payout, duration):
##    def remaining(interest):
##        return balance(deposit(principal, interest, gap-1), interest, payout, duration)
##    return lambda x: remaining(x)
##
##
##def find_cpf_rate():
##    interest = 0
##    while new_balance(166000, 121, 1280, 240)(interest) < 0:
##        interest += 0.000001
##    return round((1 + interest)**12 - 1, 4)
##print(find_cpf_rate())









