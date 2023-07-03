def hamming_distances(dna_str_list):
    result = []
    for i in range(len(dna_str_list) - 1):
        for j in range(i + 1, len(dna_str_list)):
            if len(dna_str_list[i]) != len(dna_str_list[j]):
                return "Strings are of unequal length."
            else:
                result.append(distance(dna_str_list[i], dna_str_list[j]))
    return result
            


def distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

##print(hamming_distances(['ATTCC', 'CCATT']))
##print(hamming_distances(['CCATTGCC', 'ATGCCGCC', 'ATTGCCCC', 'TTACCCGT']))

def check_rotations(dna_str_list):
    result = []
    for i in range(len(dna_str_list)):
        count = 0
        for j in range(len(dna_str_list)):
            if i == j:
                continue
            elif len(dna_str_list[i]) != len(dna_str_list[j]):
                return "Strings are of unequal length."
            
            if rotation(dna_str_list[i], dna_str_list[j]) == 1:
                count += 1
                break
        result.append(count)
                    
    return result
    

def rotation(str1, str2):
    for i in range(len(str1)):
        if str1 == str2:
            return 1
        str1 = str1[1:] + str1[0]
    return 0


#print(check_rotations(['CCATTGCC', 'ATGCCGCC', 'ATTGCCCC', 'TTACCCGT']))


def get_century(year):
    century = year//100 + 1
    return "The year " + str(year) + " falls in the " + get_ordinal(century) + " century."

def get_ordinal(century):
    if (century%100)//10 == 1:
        ordinal = "th"
    elif century%10 == 1:
        ordinal = "st"
    elif century%10 == 2:
        ordinal = "nd"
    elif century%10 == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    return str(century) + ordinal

#print(get_century(1109))

# Define helper functions here:
def has_must_have_digit(must_have_digit, number):
    for i in str(number):
        if str(must_have_digit) == i:
            return True
    return False
    
def has_factor_digit(factor_digit, number):
    if number%factor_digit == 0:
        return True
    return False

def winners(factor_digit, must_have_digit, num_of_participants):
    count = 0
    for i in range(1, num_of_participants + 1):
        if has_must_have_digit(must_have_digit, i) and has_factor_digit(factor_digit, i):
            count += 1
    return count

#print(winners(3, 5, 100))


def spend(n, ffcost, hfcost):
    combi = []
    max_health = n//hfcost
    for i in range(max_health + 1):
        ff = (n - i*hfcost)//ffcost
        combi.append([ff, i, ff*ffcost + i*hfcost])
    combi.sort(key = lambda x: x[1], reverse = True)
    combi.sort(key = lambda x: x[2], reverse = True)
    print(combi)
    return tuple(combi[0][:2])



#print(spend(123, 13, 18))

def max_element(set1, set2):
    max_val = None
    for i in set1:
        if max_val == None or i > max_val:
            max_val = i
    for j in set2:
        if max_val == None or j > max_val:
            max_val = j
    return max_val



#print(max_element((5, 1, 2), (2, 4, 3)))

def is_equal_set(set1, set2):
    if len(set1) != len(set2):
        return False
    for elem in set1:
        for i in range(len(set2)):
            if elem == set2[i]:
                set2 = set2[:i] + set2[i+1:]
                break
    
    return set2 == ()

def union(set1, set2):
    result = ()
    for elem in set1:
        for i in range(len(set2)):
            if elem == set2[i]:
                set2 = set2[:i] + set2[i+1:]
                print(result)
                break
        result += (elem, )
    print(set2)
    result += set2
    print(result)
    return result

def symmetric_difference(set1, set2):
    result = ()
    copy = set1[:]
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                set2 = set2[:j] + set2[j+1:]
                copy = set1[:i] + copy[i+1:]
                break
    result += set2
    print(result)
    result += copy
    print(result)
    return result


print(is_equal_set(symmetric_difference((2, 1, 5), (2, 4, 3)), (1, 5, 3, 4)))










