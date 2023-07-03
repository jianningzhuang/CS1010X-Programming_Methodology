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
# Write your function here. It should return a rune.

def rune_2(pic1,pic2,n):
    pattern=scale(0.5,pic1)
    while n>1:
        pattern=overlay_frac((n-1)/n,pattern,beside(pic1,flip_vert(beside(pic2,pattern))))
        n=n-1
    return quarter_turn_right(pattern)
# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)        

stereogram(rune_2(make_cross(rcross_bb),sail_bb,5))

