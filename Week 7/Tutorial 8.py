###Question 1

def make_widget():
    stuff = ["empty", "empty", 0]
    def oplookup(msg,*args):
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        elif msg == "stuff":
            return stuff
        else:
            raise Exception("widget doesn’t " + msg)
    return oplookup

widget = make_widget()

# widget takes in a command and possibly some values and executes different operations based on your command

widget("insert", 1)
widget("insert", 2)
widget("insert", 3)

# 2 is returned each time

##print(widget("insert", 1))
##print(widget("insert", 2))
##print(widget("insert", 3))
##print(widget("retrieve"))
##print(widget("retrieve"))
##print(widget("retrieve"))

###Question 2

def make_accumulator():
    result = [0]
    def current_sum(x):
        result[0] += x
        return result[0]
    return current_sum
        
    
### DO NOT MODIFY THIS ###
A = make_accumulator()
B = make_accumulator()

###Question 3

def make_monitored(f):
    result = [0]
    def mf(op):
        if op == "how-many-calls?":
            return result[0]
        elif op == "reset-count":
            result[0] = 0
        else:
            result[0] += 1
            return f(op)
    return mf
    
### DO NOT MODIFY THIS ###
def double(x):
    return 2 * x

d = make_monitored(double)

###Question 4

def make_monitored_extended(f):
    count = [0]
    def mf(*op):
        if not op:
            count[0] += 1
            return f()
        elif op[0] == "how-many-calls?":
            return count[0]
        elif op[0] == "reset-count":
            count[0] = 0
        else:
            count[0] += 1
            return f(*op)
    return mf

 
### DO NOT MODIFY THIS ###
def sum_numbers(*numbers):
    s = 0
    for n in numbers:
        s = s + n
    return s

monitored_sum_numbers = make_monitored_extended(sum_numbers)


###Question 5

def make_monte_carlo_integral(P,x1,y1,x2,y2):
    result = [0, 0] #num_success, num_trials
    def helper(*op):
        if op[0] == "run trials":
            result[1] += op[1]
            for i in range(op[1]):
                if lies_within(x1, y1, x2, y2):
                    result[0] += 1
        elif op[0] == "trials":
            return result[1]
        elif op[0] == "get estimate":
            return (result[0]/result[1]) * ((x2-x1)*(y2-y1))
    return helper
                

### DO NOT MODIFY THIS ###
import math
import random

def circle(x,y):
    return math.sqrt(x*x+y*y) < 1

circle_estimate = make_monte_carlo_integral(circle,-1,-1,1,1)

### The inrange function in testcases is used to check whether a value lies in a specified range.

def lies_within(x1, y1, x2, y2):
    x_coord = random.uniform(x1, x2)
    y_coord = random.uniform(y1, y2)
    return circle(x_coord, y_coord)

###Question 6

def translate(source,destination,string):
    translator = {}
    for i in range(len(source)):
        translator[source[i]] = destination[i]
    result = ""
    for char in string:
        if char in translator:
            result += translator[char]
        else:
            result += char
    return result

#print(translate("dikn","lvei","My tutor IS kind"))

###Question 7

def caesar_cipher(shift,string):
    source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    destination = ''
    for char in source:
        unicode = ord(char) + shift
        if ord(char) < 97:
            while unicode > 90:
                unicode -= 26
        else:
            while unicode > 122:
                unicode -= 26
        destination += chr(unicode)
    print(destination)
    
    return translate(source, destination, string)


#print(caesar_cipher(10,"abcd"))










































