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

# Entry 3 of 3
# ============
# Write your function here. It should return a rune.
# show(<your rune>)

def rune_3(n,pic1):
    pattern=pic1
    for i in range(2,n):
        pattern=make_cross(stackn(i,pattern))
    return pattern

show(rune_3(3,rcross_bb))
