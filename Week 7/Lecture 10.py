##def map(fn, seq):
##    if seq == ():
##        return ()
##    else:
##        return (fn(seq[0]), ) + map(fn, seq[1:])
##
##def filter(pred, seq):
##    if seq == ():
##        return ()
##    elif pred(seq[0]):
##        return (seq[0], ) + filter(pred, seq[1:])
##    else:
##        return filter(pred, seq[1:])

a = (1,2,3,4,5,6)
b = [1,2,3,4,5,6]

c = map(lambda x: x**2, a)
d = map(lambda x: x+2, b)

#print(tuple(c))
#for e in c:
#    print(e)


###NIM

def make_stack():
    return []

def push(s, item):
    return s.append(item)

def pop_item(s):
    if is_empty(s):
        return None
    return s.pop()

def is_empty(s):
    return len(s) == 0

def handle_undo(game_state):
    old_state = pop_item(game_stack)
    if old_state:
        display_game_state(old_state)
        return human_move(old_state)
    else:
        print("no more previous moves!")
        return human_move(game_state)

def play(game_state, player):
    display_game_state(game_state)
    if is_game_over(game_state):
        announce_winner(player)
    elif player == "human":
        play(human_move(game_state), "computer")  #alternate between player and computer
    elif player == "computer":
        play(computer_move(game_state), "human")
    else:
        print("player wasn't human or computer: " , player) #error detection

def display_game_state(game_state):
    print("")
    print(" Pile 1: " + str(size_of_pile(game_state, 1)))
    print(" Pile 2: " + str(size_of_pile(game_state, 2)))
    print("")

def is_game_over(game_state):
    return total_size(game_state) == 0

def total_size(game_state):
    return size_of_pile(game_state, 1) + size_of_pile(game_state, 2) #can combine with is_game_over?

def announce_winner(player):
    if player == "human": #computer made last move, play passed in "human" before checking total_size
        print("you lose. better luck next time.")
    else:
        print("you win. congratulations.")

game_stack = make_stack()

def human_move(game_state):
    p = prompt("which pile will you remove from?")
    n = prompt("how many coins do you want to remove?")
    if int(p) == 0:
        return handle_undo(game_state)
    else:
        push(game_stack, game_state)
    return remove_coins_from_pile(game_state, int(n), int(p))

def prompt(prompt_string):
    return input(prompt_string)

def computer_move(game_state):
    pile = 1 if size_of_pile(game_state, 1) > 0 else 2
    print("computer removes 1 coin from pile " + str(pile)) #can be better AI
    return remove_coins_from_pile(game_state, 1, pile)

def make_game_state1(n, m): # bad ADT?
    return 10*n + m

def size_of_pile1(game_state, pile_number):
    if pile_number == 1:
        return game_state//10 #n
    else:
        return game_state%10 #m

def remove_coins_from_pile1(game_state, num_coins, pile_number): #what is the limitation: num_coins < n and m
    if pile_number == 1:
        return game_state - 10*num_coins
    else:
        return game_state - num_coins

def make_game_state(n, m): #tuple
    return (n, m)

def size_of_pile(game_state, p):
    return game_state[p-1]

def remove_coins_from_pile(game_state, num_coins, p):
    if p == 1:
        return make_game_state(size_of_pile(game_state, 1) - num_coins, size_of_pile(game_state, 2))
    else:
        return make_game_state(size_of_pile(game_state, 1), size_of_pile(game_state, 2) - num_coins)


###MAKING A STACK

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
    s = make_empty_stack()
    while inputs:
        if type(inputs[0]) == int:
            push_stack(s, inputs[0])
        else:
            a = pop_stack(s)
            b = pop_stack(s)
            if inputs[0] == "+":
                push_stack(s, b + a)
            elif inputs[0] == "-":
                push_stack(s, b - a)
            elif inputs[0] == "*":
                push_stack(s, b * a)
            elif inputs[0] == "/":
                push_stack(s, b / a)
        inputs = inputs[1:]
    return pop_stack(s)

#print(calculate((5, 2, '/', 4, '*')))















































































