#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    return flip_coins(table, get_table_state(table))

# test:
#t2_1 = create_table(2)
#solve_trivial_2(t2_1)
#print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t2_1_run = create_table(2)
#run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    return flip_coins(table, get_table_state(table))
    

# test:
##t4_2 = create_table(4)
##solve_trivial_4(t4_2)
##print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t4_2_run = create_table(4)
#run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

#t4_2_susan = create_table(4)
#Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if not check_solved(table):
        return flip_coins(table, (0, 1))

# test:
##t2_3 = create_table(2)
##solve_2(t2_3)
##print(check_solved(t2_3))

########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t2_3_run = create_table(2)
#run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    a_move, b_move, c_move = (1, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0)
    n4_algorithm = (a_move, b_move, a_move, c_move, a_move, b_move, a_move)
    for move in n4_algorithm:
        if not check_solved(table):
            flip_coins(table, move)
            

# test:
#t4_4 = create_table(4)
#solve_4(t4_4)
#print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t4_4_run = create_table(4)
#run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

#t4_4_susan = create_table(4)
#Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

##def set_of_moves(n):
##    if n == 1:
##        return ((1,),)
##    else:
##        for i in range(n//2):
##            zero_row = (0,)*(i+1)
##            return ((set_of_moves(n//2)[i] + set_of_moves(n//2)[i]), ) + ((set_of_moves(n//2)[i] + zero_row), )   

##set_of_moves = ((1, 1, 1, 1), (1, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0))


def solve(table):
    set_of_moves = moves(get_table_size(table))
    print(len(set_of_moves))
    def sequence_of_moves(n):
        if n == 1:
            return (set_of_moves[1], )
        else:
            return sequence_of_moves(n-1) + (set_of_moves[n], ) + sequence_of_moves(n-1)
    for move in sequence_of_moves(get_table_size(table) - 1):
        if not check_solved(table):
            flip_coins(table, move)

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
    print(result)
    return result


##def sequence_of_moves(n):
##    if n == 1:
##        return (set_of_moves[1], )
##    else:
##        return sequence_of_moves(n-1) + set_of_moves[n], ) + sequence_of_moves(n-1)


print(moves(16))
    


def generate_movelist(n): # Working
    base = (0,)
    numZeros = (2**n)/2
    if n == 2:
        return [(1,1,1,1),(1,0,1,0),(1,1,0,0),(1,0,0,0)]
    else:
        return [i*2 for i in generate_movelist(n-1)] + [i+base*int(numZeros) for i in generate_movelist(n-1)]
        
def solve1(table):
    n=0
    while 2**n < get_table_size(table):
        n+=1
    def generate_sequence(level,move_table, memo = {}):
        if level in memo:
            return memo[level]
        elif level == 2:
            sequence = (move_table[1],move_table[2],move_table[1])
            memo[level] = sequence
            return memo[level]
        else:
            memo[level] = generate_sequence(level-1,move_table,memo) + (move_table[level],) + generate_sequence(level-1,move_table,memo)
            return memo[level]
    if n == 1:
        if not check_solved(table):
            flip_coins(table,(1,0))
    else:
        move_list = generate_movelist(n) # Working
        level = (2**n)-1
        sequence = generate_sequence(level,move_list)
        for i in range(1,len(sequence)):
            if not check_solved(table):
                flip_coins(table, sequence[i])



# test:
t4_5 = create_table(4)
solve1(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve1(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve1(t16_5)
print(check_solved(t16_5))



# Note: It is not advisable to execute run() if the table is large.
