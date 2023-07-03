#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

##def horizontal_stackn(n, pic):
##    return quarter_turn_right(stackn(n, quarter_turn_left(pic)))
##
##def sandwich(n, pic1, pic2):
##    return stack_frac(1/n, pic1, stack_frac((n-2)/(n-1), pic2, pic1))
##
##def egyptian(pic, n):
##    return sandwich(n, horizontal_stackn(n, pic), quarter_turn_right(sandwich(n, horizontal_stackn((n-2), quarter_turn_left(pic)) ,quarter_turn_left(pic))))
    

# Test
##show(stack_frac(1/5, quarter_turn_right(stackn((5-2), quarter_turn_left(sail_bb))), stack_frac((5-2)/(5-1), sail_bb, quarter_turn_right(stackn((5-2), quarter_turn_left(sail_bb))))) 

##def egyptian(pat, n):
##    #Creates one row with n pats, note that a row takes up 1/n of the image
##    def horizontal(n, pat):
##        return quarter_turn_right(stackn(n, quarter_turn_left(pat)))
##    #Combines everything together
##    #Stack the big pat at the bottom and a row of (n-2) small pats at the top
##    adding_rows_top = stack_frac(1 / (n-1), horizontal(n-2, pat), pat)
##    #Stack adding_rows_top at the top, and a row of (n-2) small pats at the bottom
##    adding_rows_bottom = stack_frac((n-1) /  n, adding_rows_top, horizontal(n-2, pat))
##    #Rotate adding_rows_bottom to the left, then stack rows of n small pats at the top
##    adding_rows_right = stack_frac(1 / (n-1), horizontal(n, quarter_turn_left(pat)), quarter_turn_left(adding_rows_bottom))
##    #Stack rows of n small pats at the bottom, then rotate adding_rows_right to the right
##    adding_rows_left = quarter_turn_right(stack_frac((n-1) / n, adding_rows_right, horizontal(n, quarter_turn_left(pat))))
##    return adding_rows_left

# your solution here

##########
# Task 1 #
##########

#n=5
#params= make_cross(rcross_bb)
##def stackn(params,n):
##    if n==1:
##        return params
##    else:
##        return stack_frac(1/n, params, stackn(params,n-1))

    
def side_1(params,n):
    return (stack_frac(1/(n-1),
                quarter_turn_right(stackn(n-2, params)),
                quarter_turn_right(params)))
#checking to see if side_1 works
#show(side_1(nova_bb,5))

def side_2(params,n):
    return (stack_frac(1/(n),
                quarter_turn_left(stackn(n-2, params)),
                turn_upside_down(side_1(params,n))))

#show(side_2(nova_bb,5))

def side_3(params,n):
   return(stack_frac(1/(n-1),
                quarter_turn_right(stackn(n, quarter_turn_left(params))),
                      quarter_turn_right(side_2(params,n))))

#show(side_3(nova_bb,5))

def side_4(params,n):
    return (stack_frac(1/n,
                 quarter_turn_right(stackn(n, quarter_turn_right(params))),
                turn_upside_down(side_3(params,n))))

#show(side_4(nova_bb,5))



def egyptian(params,n):
    return  turn_upside_down(side_4(params,n))

#show(egyptian(make_cross(rcross_bb), 9))
show(egyptian(heart_bb, 5))
##show(sandwich(5, quarter_turn_right(stackn((3), quarter_turn_left(sail_bb))), sail_bb))
##show(egyptian(5, sail_bb))
