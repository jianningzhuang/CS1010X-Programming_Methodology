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
def line_1(pic1):
    return quarter_turn_right(stackn(9,pic1))

def line_2(pic1,pic2):
    return quarter_turn_right(stack_frac(1/9,pic1,stack_frac(7/8,stackn(7,pic2),pic1)))

def line_3(pic1,pic2):
    return quarter_turn_right(stack_frac(1/9,pic1,stack_frac(1/8,pic2,stack_frac(5/7,stackn(5,pic1),stack_frac(1/2,pic2,pic1)))))

def line_4(pic1,pic2):
    return quarter_turn_right(stack_frac(1/9,pic1,stack_frac(1/8,pic2,stack_frac(1/7,pic1,stack_frac(3/6,stackn(3,pic2),stack_frac(1/3,pic1,stack_frac(1/2,pic2,pic1)))))))

def line_5(pic1,pic2,pic3):
    return quarter_turn_right(stack_frac(1/9,pic1,stack_frac(1/8,pic2,stack_frac(1/7,pic1,stack_frac(1/6,pic2,stack_frac(1/5,pic3,stack_frac(1/4,pic2,stack_frac(1/3,pic1,stack_frac(1/2,pic2,pic1)))))))))

def rune_1(pic1,pic2,pic3):
    return stack_frac(1/9,line_1(pic1),stack_frac(1/8,line_2(pic1,pic2),stack_frac(1/7,line_3(pic1,pic2),stack_frac(1/6,line_4(pic1,pic2),stack_frac(1/5,line_5(pic1,pic2,pic3),stack_frac(1/4,line_4(pic1,pic2),stack_frac(1/3,line_3(pic1,pic2),stack_frac(1/2,line_2(pic1,pic2),line_1(pic1)))))))))
# show(<your rune>)
                              
show(rune_1(rcross_bb,make_cross(nova_bb),make_cross(rcross_bb)))



