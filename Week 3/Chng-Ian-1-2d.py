#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *
########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============

def my_rune(rune,n):
    small_rune = scale(2/n,rune)
    def find_point(i):
        return translate(sin(7*pi*i/100)/3,
                        cos(5*pi*i/100)/3,
                         small_rune)
    result = find_point(1)
    for i in range(2, n+1):
        result = overlay_frac(1/i, find_point(i), result)
    return result

    
show(my_rune(make_cross(rcross_bb),100))


