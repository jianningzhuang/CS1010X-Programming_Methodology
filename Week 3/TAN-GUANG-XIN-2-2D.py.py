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

# Entry 2 of 3
# this program returns a fractal pattern with 1 painter that extends in left and right directions for n
def double_fractal(rune, n):
    output_0 = quarter_turn_right(stackn(2**(n-1), rune))
    output_1 = quarter_turn_right(stackn(2**(n-1), rune))
    for i in range(2, n+1):
        row_0 = quarter_turn_right(stackn(2**(n - i), rune))
        output_0 = stack(output_0, row_0)
    for a in range(2, n):
        row_1 = quarter_turn_right(stackn(2**(n - a), rune))
        output_1 = stack(row_1, output_1)
    return quarter_turn_left(stack_frac(2/3, output_0, output_1))

show(double_fractal(ribbon_bb, 7))


