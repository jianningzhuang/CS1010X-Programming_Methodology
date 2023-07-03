def deep_reverse(lst):
    if lst == []:
        return []
    elif type(lst) != list:
        return lst
    else:
        return deep_reverse(lst[1:]) + [deep_reverse(lst[0])]

#print(deep_reverse([1,2,[3,4],[[5]],[6,[7,8],9]]))

def deep_sum(lst):
    if lst == []:
        return 0
    elif type(lst) != list:
        return lst
    else:
        return deep_sum(lst[0]) + deep_sum(lst[1:])

#print(deep_sum([1, [[[2, 3, 4, 5],6 ], 7], 8, [9, 10, [11]]]))


class Number(object):
    # complete the class definition #
    def __init__(self, num):
        self.num = num
    
    def plus(self, other):
        if self.value() == "Undefined" or other.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num + other.num)
        
    def times(self, other):
        if self.value() == "Undefined" or other.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num * other.num)
    
    def divide(self, other):
        if other.value() == 0:
            return Number("Undefined")
        elif self.value() == "Undefined" or other.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num // other.num)
    
    def minus(self, other):
        if self.value() == "Undefined" or other.value() == "Undefined":
            return Number("Undefined")
        return Number(self.num - other.num)
    
    def value(self):
        return self.num

    def spell(self):
        numeral = self.value()
        one_to_twenty = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        count = 0
        result = []
        while numeral > 0:
            count +=1
            result.append(numeral%10)
            numeral = numeral//10
            print(result)
        if count > 7:
            return "really large number"
        elif self.value() < 20:
            return one_to_twenty[self.value()]
        elif count == 2:
            return tens[result[1]] + " " + one_to_twenty[result[0]]
        elif count == 3:
            return one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
        elif count == 4:
            return one_to_twenty[result[3]] + " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
        elif count == 5:
            if self.value()%100000 < 20000:
                return one_to_twenty[(self.value()%100000)//1000] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
            else:
                return tens[result[4]] +one_to_twenty[result[3]] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
        elif count == 6:
            if self.value()%100000 < 20000:
                return one_to_twenty[result[5]] + " hundred and " + one_to_twenty[(self.value()%100000)//1000] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
            else:
                return one_to_twenty[result[5]] + " hundred and " + tens[result[4]] +one_to_twenty[result[3]] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
        else:
            if self.value()%100000 < 20000:
                return one_to_twenty[result[6]] + "million, " + one_to_twenty[result[5]] + " hundred and " + one_to_twenty[(self.value()%100000)//1000] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
            else:
                return one_to_twenty[result[6]] + "million, " +  one_to_twenty[result[5]] + " hundred and " + tens[result[4]] +one_to_twenty[result[3]] + \
                       " thousand, " + one_to_twenty[result[2]] + " hundred and " + tens[result[1]] + " " + one_to_twenty[result[0]]
            
def power_set(lst):
    if lst == []:
        return [[]]
    a = lst[0]
    rest = power_set(lst[1:])
    result = []
    for subset in rest:
        result.append([a] + subset)
    
    return result + rest



#print(power_set([1,2,3]))

##print(list(range(1, 9)))
##print(list(map(lambda x: 5*x, range(1, 13))))
##print(list(filter(lambda x: x%2 == 1, map(lambda x: x*x, list(range(1, 12))))))
##print(list(map(lambda x: x*x if x%2 == 1 else x//2, list(range(1,11)))))
##print(list(accumulate(lambda x, y: y + [x], [], list(filter(lambda x: x%3 != 0, map(lambda x: x*2 , list(range(1,11))))))))



def make_stack():
    stack = []
    def dispatch(op, *args):
        if op == "push":
            stack.append(args[0])
        elif op == "peek":
            return stack[-1]
        elif op == "pop":
            return stack.pop()
        elif op == "size":
            return len(stack)
        else:
            return "Invalid command"
    return dispatch


def prefix_infix(lst):
    stack = make_stack()
    for elem in lst:
        if type(elem) == list:
            stack("push", prefix_infix(elem))
        else:
            stack("push", str(elem))
    right = stack("pop")
    left = stack("pop")
    operand = stack("pop")
    return "(" + str(left) + " " + operand + " "+ str(right) + ")" 




#print(prefix_infix (['+', ['*', 5, 4], ['-', 2, 1]]) == "((5 * 4) + (2 - 1))" )

#print(prefix_infix(['-',['*',5,4],['-',['/',1,45],['+',1,1]]]) == '((5 * 4) - ((1 / 45) - (1 + 1)))')


def bubble_sort(lst):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print(lst)
                swap = True
    return lst

print(bubble_sort([5,1,4,2,8]))

def ten_ten_as(number):
    result = 0
    count = 0
    while number > 0:
        if count%2 == 0:
            result += number%10
        else:
            for digit in str((number%10)*2):
                result += int(digit)
        number = number//10
        count+=1
    return result

print(ten_ten_as(45223))

def split(n,lst):
    lst1 = []
    lst2 = []
    for elem in lst:
        if elem <= n:
            lst1.append(elem)
        else:
            lst2.append(elem)
    return [lst1, lst2]

print(split(5,[1,10,4,9,7,2,5,8,3,4,9,6,2]))

def peak(lst):
    def helper(low, high):
        if low == len(lst) - 1:
            return lst[len(lst)-1]
        elif high == 0:
            return lst[0]
        mid = (low + high)//2
        if lst[mid] < lst[mid-1]:
            return helper(low, mid - 1)
        elif lst[mid] < lst[mid+1]:
            return helper(mid + 1, high)
        else:
            return lst[mid]
    return helper(0, len(lst)-1)

#print(peak([1,2,3,4,3,2,3,4,3,2,1]))

def greedy_ascent(lst):
    def helper(x, y):
        if 0 < x < len(lst)- 1 and 0< y < len(lst)-1: #4 directions accesible, implement the edge cases/corner cases with some default direction
            print(lst[x][y])
            if lst[x][y] < lst[x][y+1]:
                return helper(x, y+1)
            elif lst[x][y] < lst[x+1][y]:
                return helper(x+1, y)
            elif lst[x][y] < lst[x][y-1]:
                return helper(x, y-1)
            elif lst[x][y] < lst[x-1][y]:
                return helper(x-1, y)
            else:
                return lst[x][y]

    return helper(1, 1)

print(greedy_ascent([[1,2,3,4], [2,3,4,3], [1,6,5,1], [1,1,1,1]]))



























