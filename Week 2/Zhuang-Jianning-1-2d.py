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

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def one_tile():
    return stack(black_bb, blank_bb)

def one_line():
    return stack_frac(1/50, black_bb, quarter_turn_right(stackn(6, one_tile())))
                      
def staggered():
    return stack(stack(one_line(), translate(-0.03, 0, one_line())), stack(translate(-0.06, 0, one_line()),translate(-0.03, 0, one_line())))

def are_the_lines_parallel():
    return stackn(3, staggered())

show(are_the_lines_parallel())

# show(<your rune>)



