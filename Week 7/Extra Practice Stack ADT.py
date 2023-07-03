###Question 1

def make_stack(seq):
    result = []
    for elem in seq:
        result.append(elem)
    return result

def make_empty_stack():
    return make_stack([])

def is_empty_stack(stack):
    return len(stack) == 0


##########################################
#       Do not modify test code          #              
##########################################
s1 = make_empty_stack()                  #
s2 = make_stack((2, 4, 5))               #
s3 = make_stack([3, 5, 7, 8])            #
                                         #
is_empty1 = is_empty_stack(s1) #True	 #
is_empty2 = is_empty_stack(s2) #False	 #
is_empty3 = is_empty_stack(s3) #False    #
##########################################

def push_stack(stack, item):
    stack.append(item)

def pop_stack(stack):
    if is_empty_stack(stack):
        return None
    return stack.pop()
    
        
def peek_stack(stack):
    if is_empty_stack(stack):
        return None
    else:
        return stack[-1]
    
def clear_stack(stack):
    while not is_empty_stack(stack):
        pop_stack(stack)
    return stack

def calculate(inputs):
    result = make_empty_stack()
    while inputs:
        if type(inputs[0]) == int:
            push_stack(result, inputs[0])
        else:
            right = pop_stack(result)
            left = pop_stack(result)
            if inputs[0] == "+":
                push_stack(result, left + right)
            elif inputs[0] == "-":
                push_stack(result, left - right)
            elif inputs[0] == "*":
                push_stack(result, left * right)
            elif inputs[0] == "/":
                push_stack(result, left / right)
        inputs = inputs[1:]
    return pop_stack(result)


#print(calculate((1, 2, '+', 3, '*')))


###Question 2

##def make_postfix(expr):
##    if type(expr) != tuple:
##        return (expr, )
##    else:
##        return make_postfix(expr[0]) + make_postfix(expr[2]) + (expr[1], )

#print(make_postfix((3, '*', (1, '+', 2))))

###Question 3

def make_postfix(expr):
    if type(expr) != tuple:
        return (expr, )
    elif len(expr) == 5:
        return make_postfix(expr[0]) + make_postfix(expr[2]) + make_postfix(expr[4]) + (expr[1] + expr[3], )

    else:
        return make_postfix(expr[0]) + make_postfix(expr[2]) + (expr[1], )

#print(make_postfix(((1, '+', 2), '?', 4, ':', (2, '^', (3, '?', 6, ':', 2)))))

###Question 4


def calculate(infix):
    inputs = make_postfix(infix)
    result = make_empty_stack()
    while inputs:
        if type(inputs[0]) == int:
            push_stack(result, inputs[0])
        else:
            right = pop_stack(result)
            left = pop_stack(result)
            if inputs[0] == "+":
                push_stack(result, left + right)
            elif inputs[0] == "-":
                push_stack(result, left - right)
            elif inputs[0] == "*":
                push_stack(result, left * right)
            elif inputs[0] == "/":
                push_stack(result, left / right)
            elif inputs[0] == "^":
                if left > right:
                    push_stack(result, left)
                else:
                    push_stack(result, right)
            elif inputs[0] == "?:":
                parity = pop_stack(result)
                if parity%2 == 1:
                    push_stack(result ,left)
                else:
                    push_stack(result, right)
        inputs = inputs[1:]
    return pop_stack(result)

print(calculate((1, '?', 2, ':', 3)))














