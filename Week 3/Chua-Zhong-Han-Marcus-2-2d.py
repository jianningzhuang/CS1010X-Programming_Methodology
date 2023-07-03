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

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.
# show(<your rune>)

def rune_2(n,pic1,pic2,pic3,pic4):
    if n==1:
        return beside(stack(pic1,pic2),stack(pic3,pic4))
    else:
        return rune_2(n-1,beside(stack(pic1,pic2),stack(pic3,pic4)),beside(stack(pic1,pic2),stack(pic3,pic4)),beside(stack(pic1,pic2),stack(pic3,pic4)),beside(stack(pic1,pic2),stack(pic3,pic4)))

show(rune_2(3,heart_bb,rcross_bb,nova_bb,ribbon_bb))
