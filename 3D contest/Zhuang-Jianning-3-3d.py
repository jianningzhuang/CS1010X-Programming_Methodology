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

# Entry 3 of 3
# ============
# Write your function here. It should return a rune.

bun = translate(-0.05, -0.2, scale(0.35, image_to_painter("bun.png")))

cheese1 = translate(-0.13, -0.3, scale(0.15, image_to_painter("cheese.jpg")))

cheese2 = translate(-0.13, -0.15, scale(0.15, image_to_painter("cheese.jpg")))

cheese3 = translate(-0.13, 0, scale(0.15, image_to_painter("cheese.jpg")))


patty1 = translate(-0.08, -0.05, scale(0.3, image_to_painter("patty.png")))

patty2 = translate(-0.08, 0.1, scale(0.3, image_to_painter("patty.png")))

patty3 = translate(-0.08, 0.25, scale(0.3, image_to_painter("patty.png")))

def ideal_burger():
    return overlay_frac(1/8, bun,
                        overlay_frac(1/7, cheese1,
                                     overlay_frac(1/6, patty1,
                                                  overlay_frac(1/5, cheese2,
                                                            overlay_frac(1/4, patty2,
                                                                         overlay_frac(1/3, cheese3, patty3))))))


##show(ideal_burger())
anaglyph(ideal_burger())




# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)









