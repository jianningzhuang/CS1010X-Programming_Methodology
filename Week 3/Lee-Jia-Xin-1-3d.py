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
monster = image_to_painter("monster2.png")
step = beside(beside(flip_horiz(sail_bb), scale_independent(3,1,make_cross(rcross_bb))), beside(scale_independent(3, 1,make_cross(rcross_bb)), sail_bb))
stairs = overlay_frac(1/3, stack_frac(2/3, blank_bb, step), overlay(stack_frac(1/3, blank_bb, stack(step, blank_bb)), stack_frac(1/3, step, blank_bb)))
anaglyph(overlay_frac(3/4, stack_frac(1/4, blank_bb, stairs), quarter_turn_left(monster)))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
