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
# ============
# Write your function here. It should return a rune.


def sandwich(n, pic1, pic2, pic3):
    return quarter_turn_left(stack_frac(1/n,
                                        quarter_turn_right(pic1),
                                        stack_frac((n-2)/(n-1), quarter_turn_right(pic2), quarter_turn_right(pic3))))

def five_heart_pattern():
    return scale(0.9, sandwich(3, stack(heart_bb, heart_bb),
                               scale_independent(1, 1/2, heart_bb),
                               stack(heart_bb, heart_bb)))

def ten_heart_pattern():
    return stack(five_heart_pattern(), turn_upside_down(five_heart_pattern()))

def number_one():
    return sandwich(3, blank_bb, black_bb, blank_bb)

def mosaic(pic1, pic2, pic3, pic4): 
    return stack(beside(pic4, pic1), beside(pic3, pic2))
def number_zero():
    return make_cross(mosaic(quarter_turn_right(translate(0.5, 0, number_one())), blank_bb, blank_bb, translate(0.5, 0, number_one())))
def number_ten():
    return stack(translate(-0.18, 0, beside(translate(0.4, 0, scale_independent(0.35, 0.55, number_one())), number_zero())), scale(0.7, heart_bb))

def ten_column():
    return stack(stack(number_ten(), blank_bb), blank_bb)

def black_ten_of_hearts():
    return sandwich(7, ten_column(), ten_heart_pattern(), turn_upside_down(ten_column()))

show(black_ten_of_hearts())

# show(<your rune>)





































