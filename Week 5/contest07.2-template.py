#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from more_lazy_susan import *

def create_solver(coins):
##    set_of_moves = ()
##    for move in moves(8):
##        set_of_moves += (move[:] + (0,)*(coins-8),)
##    sequence_of_moves = sequence(7, set_of_moves)
##    def solver(move_id):
##        move = sequence_of_moves[move_id%len(sequence_of_moves)]
##        return move
##    return solver


    set_of_moves = ()
    for move in moves(16):
        set_of_moves += (move[:coins],)
    sequence_of_moves = sequence(coins - 1, set_of_moves)
    def solver(move_id):

        if move_id%2 == 0:
            move = sequence_of_moves[move_id%len(sequence_of_moves)]
        else:
            if move_id%7 == 0:
                move = ([True] + [False])*(coins//2) + [False]*(coins%2)
            if move_id%7 == 1:
                move = ([True] + [False]*2)*(coins//3) + [False]*(coins%3)
            if move_id%7 == 3:
                move = ([True] + [False]*3)*(coins//4) + [False]*(coins%4)
            if move_id%7 == 5:
                move = ([True] + [False]*4)*(coins//5) + [False]*(coins%5)
            if move_id%7 == 2:
                move = [True]*3 + [False]*(coins - 3)
            if move_id%7 == 4:
                move = [True]*2 + [False]*(coins - 2)
            if move_id%7 == 6:
                move = [True] + [False]*(coins-1)
##            if move_id%4 == 0:
##                move = ([True] + [False])*(coins//2) + [True]*(coins%2)
##            if move_id%4 == 1:
##                move = [True]*5 + [False]*(coins - 5)
##            if move_id%4 == 2:
##                move = ([True] + [False])*(coins//4) + [False]*(coins - 2*(coins//4))
##            if move_id%4 == 3:
##                move = [True] + [False]*(coins-1)
        
                
        return move
    return solver
        

##    def solver(move_id):
##        if move_id%2 == 0:
##            move = ([True] + [False])*(coins//2) + [True]*(coins%2)
##        else:
##            move = [True] + [False]*(coins - 1)
##        return move
##    return solver

    
    
##    def solver(move_id):
##        if move_id%8 == 0:
##            move = ([True] + [False])*(coins//2) + [False]*(coins%2)
##        if move_id%8 == 1:
##            move = ([True] + [False]*2)*(coins//3) + [False]*(coins%3)
##        if move_id%8 == 3:
##            move = ([True] + [False]*3)*(coins//4) + [False]*(coins%4)
##        if move_id%8 == 5:
##            move = ([True] + [False]*4)*(coins//5) + [False]*(coins%5)
##        if move_id%8 == 7:
##            move = [True]*4 + [False]*(coins - 5)
##        if move_id%8 == 2:
##            move = [True]*3 + [False]*(coins - 5)
##        if move_id%8 == 4:
##            move = [True]*2 + [False]*(coins - 5)
##        if move_id%8 == 6:
##            move = [True] + [False]*(coins-1)
##            
##        return move
##    return solver
        

##def create_solver(coins):
##    # insert your code here
##    move = [True] + [False] * (coins - 1)
##    set_of_moves = ()
##    for move in moves(coins):
##        set_of_moves += (move[:coins], )
##    def solver(move_id):
##        move = [True] + [False] * (coins - 1)
##        for i in range(1, coins+1):
##            if move_id%(2**i) == (2**(i-1) - 1):
##                move = set_of_moves[i]
##
####        if move_id%2 == 0:
####            move = set_of_moves[1]
####        elif move_id%4 == 1:
####            move = set_of_moves[2]
####        elif move_id%8 == 3:
####            move = set_of_moves[3]
####        elif move_id%16 == 7:
####            move = set_of_moves[4]
####        elif move_id%32 == 15:
####            move = 
####        
##
##        return move
##
##    return solver


def sequence(n, set_of_moves):
    if n == 1:
        return (set_of_moves[1], )
    else:
        return sequence(n-1, set_of_moves) + (set_of_moves[n], ) + sequence(n-1, set_of_moves)


def moves(n):
    result = ((1, ), )
    i = 1
    while i < n:
        result1, result2 = (), ()
        for j in range(i):
            result1 += ((result[j] + result[j]), )
            
        for k in range(i):
            zero_row = (0, )*(i)
            result2 += ((result[k] + zero_row), )
            
        result = result1  + result2
        i *= 2
    return result



##set_of_moves = ()
##for move in moves(16):
##    set_of_moves += (move[:13], )
##print(set_of_moves)
##
##def sequence_of_moves(n):
##    if n == 1:
##        return (set_of_moves[1], )
##    else:
##        return sequence_of_moves(n-1) + (set_of_moves[n], ) + sequence_of_moves(n-1)
##
##print(sequence_of_moves(9))





# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
get_contest_score(create_solver, True)


##        move = [True] + [False]*(move_id%coins) + [True] + 
##        if move_id%2 == 0:
##            move = ([True] + [False])*(coins//2) + [True]*(coins%2)
##        elif move_id%4 == 1:
##            move = ([True]*2 + [False]*2)*(coins//4) +[True]*(coins%4)
##        elif move_id%8 == 3:
##            move = ([True] + [False]*3)*
