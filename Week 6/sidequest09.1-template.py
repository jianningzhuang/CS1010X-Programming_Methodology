#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    result = []
    total_elements = 0
    for lst in all_lst:
        total_elements += len(lst)
    while len(result) != total_elements:
        min_value = None
        min_list = None
        for i in range(len(all_lst)):
            if all_lst[i] == []:
                continue
            if min_value == None or all_lst[i][0] < min_value:
                min_value = all_lst[i][0]
                min_list = all_lst[i]
        result.append(min_value)
        min_list.pop(0)
    return result
        

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]


###########
# Task 1b #
###########

def merge(lists, field):
    result = []
    total_elements = 0
    for lst in lists:
        total_elements += len(lst)
    while len(result) != total_elements:
        min_value, min_list, min_module = None, None, None
        for i in range(len(lists)):
            if lists[i] == []:
                continue
            if min_value == None or field(lists[i][0]) < min_value:
                min_value = field(lists[i][0])
                min_module = lists[i][0]
                min_list = lists[i]
        result.append(min_module)
        min_list.pop(0)
    return result

##def merge(lists, field):
##    # Your code here
##
##    if len(lists) == 1 :
##        return lists[0]
##    
##    else:
##        list1 = lists[0]
##        list2 = lists[1]
##        new_list = []
##        i,j = 0,0
##        while i < len(list1) and j < len(list2):
##            if field(list1[i]) < field(list2[j]):
##                new_list.append(list1[i])
##                i += 1
##            else:
##                new_list.append(list2[j])
##                j += 1
##        new_list += list1[i:] + list2[j:]
##    
##        return merge([new_list] +  lists[2:],field)
        


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########
from math import ceil

def merge_sort(lst, k, field):
    if len(lst) < 2:
        return lst[:]
    else:
        if len(lst)%k == 0:
            increment = len(lst)//k
        else:
            increment = len(lst)//k + 1
        result = []
        for i in range(0, len(lst), increment):
            result.append(merge_sort(lst[i:i+increment], k, field))
        
        return merge(result, field)

def merge_sort(lst, k, field):

    length = len(lst)//k
    new_lst = []
    for i in range(k):
        new_lst += sort(lst[:length])
        if lst:
            lst = lst[length:]
    new = merge(new_lst,field)
    return new


##def get_split_lists(lst,k):
##    if len(lst)%k == 0:
##        increment = len(lst)//k
##    else:
##        increment = len(lst)//k + 1
##    result = []
##    for i in range(0, len(lst), increment):
##        result.append(lst[i:i+increment])
##    return result
##
##def merge_sort(lst, k, field):
##    result_ls = []
##    if len(lst)<=1:
##        return lst
##    else:
##        split_list = get_split_lists(lst,k)
##        for i in split_list:
##            result_ls.append(merge_sort(i,k,field))
##    return merge(result_ls,field)


# For your own debugging
modules = read_json('modules_small.txt')
for module in merge_sort(modules, 2, module_code):
    print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
test('modules_small')
test('modules')
test('modules_empty')
