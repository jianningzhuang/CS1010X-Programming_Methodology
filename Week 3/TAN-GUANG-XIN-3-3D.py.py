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

# Entry 3 of 3
# ============
def repeater(rune, n):
    top_left = translate(-0.5, -0.5, rune)
    bottom_left = translate(-0.5, 0.5, rune)
    top_right = translate(0.5, -0.5, rune)
    bottom_right = translate(0.5, 0.5, rune)
    unit = beside(stack(top_left, bottom_left), stack(top_right, bottom_right))
    output = unit
    for i in range(1, (n + 1)):
        odd_even = i%2
        if odd_even == 0:
            output = overlay_frac(1/i, translate(0, -0.5, scale(1/i, unit)), output)
        else:
            output = overlay_frac(1/i, translate(0, 0.5, scale(1/i, unit)), output)
    return output
        
        
hollusion(scale(1/4, repeater(circle_bb, 6)))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
#beside(stack(top_left, bottom_left), 
