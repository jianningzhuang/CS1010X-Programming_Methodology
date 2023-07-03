#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 3 of 3
# this programe creates a v shaped arrangement of rune_0 on a specified
# background of rune_1 of size n x n for odd values of n
def v(rune_0, rune_1, n):
    rune_0, rune_1 = quarter_turn_left(rune_0), quarter_turn_left(rune_1)
    between = [1+(i*2) for i in range(0, n)]
    largest = 2 + 1 + (2 * (n-1))
    output = stackn(largest, rune_0)
    for i in range(0, (n-1)):
        gap = between[i]
        indent = (largest - 2 - gap)/2
        fill = stackn(indent, rune_0)
        middle = stackn(gap, rune_1)
        row = stack_frac((indent+gap)/largest, stack_frac(indent/(indent+gap), fill, middle), fill)
        output = beside(row, output)
    return quarter_turn_right(output)
    
            
                   
show(v(rcross_bb, black_bb, 10))
