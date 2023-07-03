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
# this program returns painters in a spiral decending downwards
def spiral(rune, n):
    from math import sin, cos, pi
    repeater = scale(2/n, rune)  # to scale down the rune to correct size

    sweep = (360/n) * (pi/180)  # angle swept out between reeating runes
    radius = 0.5 # the hypothenus for calculating x and y displacement
    output = repeater
    for i in range(1, n):
        angle = -(pi/2) + (i * sweep)
        x = -radius * cos(angle) * (1/(n-i+1))
        y = -radius * sin(angle) * (1/(n-i+1))
        output = overlay_frac(1/i, translate(x, y, repeater), output)

    return output
hollusion(spiral(circle_bb, 15))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
