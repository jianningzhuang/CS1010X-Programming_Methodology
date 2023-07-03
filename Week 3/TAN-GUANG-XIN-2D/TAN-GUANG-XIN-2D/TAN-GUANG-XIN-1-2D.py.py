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
# this program returns a cherquered flag pattern with 2 painters, of size n x n
def chequer(rune_0, rune_1, n):
    if n > 1:
        row_0 = rune_0
        row_1 = rune_1
        for i in range(0, (n-1)):
            odd_even = i % 2
            if odd_even == 0:
                row_0 = stack_frac((i + 1)/(i + 2), row_0, rune_1)
                row_1 = stack_frac((i + 1)/(i + 2), row_1, rune_0)
            else:
                row_0 = stack_frac((i + 1)/(i + 2), row_0, rune_0)
                row_1 = stack_frac((i + 1)/(i + 2), row_1, rune_1)
            
        row_0 = quarter_turn_right(row_0)
        row_1 = quarter_turn_right(row_1)
        output = row_0
        for a in range(0, n):
            odd_even = a % 2
            if odd_even == 0:
                output = stack_frac((a + 1)/(a + 2), output, row_1)
            else:
                output = stack_frac((a + 1)/(a + 2), output, row_0)
        return quarter_turn_left(output)
    else:
        return rune_0
show(chequer(black_bb, blank_bb, 8))


