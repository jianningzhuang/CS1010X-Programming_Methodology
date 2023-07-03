#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def spiral_decay(pic, n):
    result = translate(0.45*cos(pi/2) ,0.45*sin(pi/2), scale(0.015, pic))


    for i in range(1, n+1):
        length = (0.45 - i/1900)
        result = overlay_frac(1/i, translate(length*cos(pi/2 + (2*pi*i)/360), length*sin(pi/2 + (2*pi*i)/360), scale(0.015, pic)), result)


    return result

hollusion(spiral_decay(circle_bb, 900))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
