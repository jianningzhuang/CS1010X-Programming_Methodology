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
# ============
# Write your function here. It should return a rune.

def horizontal_stackn(n, pic):
    return quarter_turn_right(stackn(n, quarter_turn_left(pic)))

def sandwich(n, pic1, pic2):
    return stack_frac(1/n, pic1, stack_frac((n-2)/(n-1), pic2, pic1))

def pattern(n, pic1, pic2):
    return sandwich(n, horizontal_stackn(n, pic1), quarter_turn_right(sandwich(n, horizontal_stackn((n-2), quarter_turn_left(pic1)) ,quarter_turn_left(pic2))))

def sierpinski_carpet(pic1, pic2, m):
    result = pattern(3, pic1, pic2)
    while m > 1:
        result = pattern(3, result, pic2)
        m -=1
    return result


show(sierpinski_carpet(scale(0.25, black_bb), black_bb, 4))

# show(<your rune>)



