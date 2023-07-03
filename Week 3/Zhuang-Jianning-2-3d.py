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

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.

def edge():
    return translate(0.5, 0, flip_horiz(sail_bb))

def triangle():
    return scale_independent(1, 3**(1/2)/4, scale(0.29, translate(0.25, 0, beside(edge(), translate(-0.5, 0, sail_bb)))))

def rhombus():
    return quarter_turn_left(stack_frac(1/3, quarter_turn_right(edge()), stack(black_bb, quarter_turn_left(edge()))))

def height():
    return stack_frac(1/3, translate(1/6, 0, rhombus()), stack(rhombus(), translate(-1/6, 0, rhombus())))

def sixty_degrees():
    return scale(0.25, scale_independent(2/(3**(1/2)), 1, height()))

def three_tiles():
    return flip_vert(rotate(pi/3, sixty_degrees()))

def six_tiles():
    return translate(-0.135, 0.25, overlay_frac(1/100, three_tiles(), translate(0.285, 0, three_tiles())))

def seven_tiles():
    return overlay_frac(1/100, six_tiles(), translate(0.3, 0.25, three_tiles()))

def without_tip():
    return overlay_frac(1/100, seven_tiles(), translate(-0.1, 0.065, sixty_degrees()))

def one_third():
    return overlay_frac(1/100, without_tip(), translate(-0.1, -0.122, triangle()))

def two_third():
    return translate(0.087, -0.01, rotate(-2*pi/3, one_third()))

def three_third():
    return translate(0.05, 0.069, rotate(-4*pi/3, one_third()))

def penrose_triangle():
    return overlay_frac(1/2, one_third(), overlay_frac(4/5, two_third(), three_third()))


hollusion(penrose_triangle())

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
