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
# Write your function here. It should return a rune.

def rune_3(pic1,pic2,n):
    if n==1:
        return stack(pic1,pic2)
    else:
        return overlay_frac((n-1)/n,eighth_turn_left(rune_3(pic1,pic2,n-1)),stack(pic1,pic2))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)


hollusion(rune_3(ribbon_bb,ribbon_bb,5))
