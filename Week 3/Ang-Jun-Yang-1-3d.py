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

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.
def show_rune(x , y , depth,rune):

    if depth ==0:
        return rune
    x += 0.06
    return overlay_frac(1 / depth , translate(x , y , rune) ,  show_rune(x , y  , depth - 1 , rune))

def main():
    rotation = 0
    result = scale(0.05,circle_bb)
    for y in range(1 ,37):
        result = overlay_frac(y/36 , result , rotate(math.radians((y-1)*66) , show_rune(0,0, 8 , scale(0.05 , circle_bb))))
    return result 


# Use one of the following methods to display your rune:
##stereogram(main())
##anaglyph(main())
hollusion(main())
