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

# Entry 2 of 3
# ============
# this program returns a repeated pattern that rises from the bottom while shrinking and rotating
def repeater(rune_0, rune_1, rune_2, rune_3, n):

    top_left = translate(-0.5, -0.5, rune_0)
    bottom_left = translate(-0.5, 0.5, rune_1)
    top_right = translate(0.5, -0.5, rune_2)
    bottom_right = translate(0.5, 0.5, rune_3)
    unit = beside(stack(top_left, bottom_left), stack(top_right, bottom_right))
    output = unit
    for i in range(1, (n + 1)):
        unit = eighth_turn_left(unit)
        output = overlay_frac(1/i, scale(1/i, unit), output)
    return output
        
        
anaglyph(repeater(circle_bb, nova_bb, rcross_bb, corner_bb,  20))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
#beside(stack(top_left, bottom_left), 
