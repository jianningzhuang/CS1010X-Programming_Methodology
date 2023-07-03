from itertools import permutations

def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    result = []
    for i in range(len(lst)):
        chosen = lst[i]
        left = lst[:i] + lst[i+1:]
        for p in permutation(left):
            result.append([chosen] + p)
    return result



def value(word, dictionary):
    if dictionary[word[0]] == 0:
        return False
    result = 0
    for letter in word:
        result += dictionary[letter]
        result = result*10
    return result//10
        


def addition_puzzle(*args):

    digits = [0,1,2,3,4,5,6,7,8,9]
    
    result = {}
    for word in args:
        for letter in word:
            if letter not in result:
                result[letter] = None
    if len(result.keys()) > 10:
        return False
    if len(args) < 3:
        return False

    
    for possible in permutations(digits, len(result)):
#    for possible in permutation(digits):
        for letter in result:
            result[letter] = possible[0]
            possible = possible[1:]

        accum = []
        flag = True

        for word in args:
            if value(word, result) == False:
                flag = False
                break
            else:
                accum.append(value(word, result))
        if flag == False:
            continue

        if sum(accum[:-1]) == accum[-1]:
            return result
    return False

        

print(addition_puzzle('ANT', 'MAN', 'COOL'))
