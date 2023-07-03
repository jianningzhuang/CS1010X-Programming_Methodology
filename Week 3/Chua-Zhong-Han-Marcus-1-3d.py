#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def layer_1(pic):
    return scale(1/4,make_cross(stackn(2,pic)))

def layer_2(pic):
    return scale(1/2,make_cross(make_cross(stackn(2,pic))))

def layer_3(pic):
    return stack_frac(1/3,quarter_turn_right(stackn(3,make_cross(stackn(2,pic)))),stack(quarter_turn_right(stackn(3,make_cross(stackn(2,pic)))),quarter_turn_right(stackn(3,make_cross(stackn(2,pic))))))

def layer_4(pic):
    return make_cross(make_cross(make_cross(stackn(2,pic))))

def rune_1(pic):
    return overlay_frac(1/4,layer_1(pic),overlay_frac(1/3,layer_2(pic),overlay_frac(1/2,scale(3/4,layer_3(pic)),layer_4(pic))))



# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)


anaglyph(rune_1(rcross_bb))


